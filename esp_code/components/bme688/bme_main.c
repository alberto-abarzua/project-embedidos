#include <bme68x.h>
#include <esp_system.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <stdio.h>
#include <string.h>
#include "esp_log.h"
#include "driver/uart.h"

#define PORT 1
#define I2C_MASTER_SCL_IO GPIO_NUM_27  // GPIO pin
#define I2C_MASTER_SDA_IO GPIO_NUM_26  // GPIO pin
#define BME_ADDR 0x76
#define BUF_SIZE (124)

#ifndef APP_CPU_NUM
#define APP_CPU_NUM PRO_CPU_NUM
#endif

#define REDIRECT_LOGS 1  // set to 0 to view logs on UART0

uint8_t bme_mode = 0;  // 0 paralel 1 forced

int serial_read_bme(char *buffer) {
    char *ptr = buffer;
    while (true) {
        // Try to read a byte with a timeout of 0
        int len = uart_read_bytes(UART_NUM_0, (uint8_t *)ptr, 1, 0);
        if (len == 1) {
            if (*ptr == ';') {
                // End of message
                return ptr - buffer;
            }
            ptr++;
            if (ptr - buffer >= BUF_SIZE) {
                // Buffer is full
                return -1;
            }
        } else if (len == -1) {
            // An error occurred
            return -1;
        } else {
            // No data available
            return -1;
        }
    }
}

int serial_write_bme(const char *to_send, int len) {
    char *to_send_with_semicolon = (char *)malloc(
        sizeof(char) * (len + 1));  // Extra space for the semicolon
    memcpy(to_send_with_semicolon, to_send, len);  // Copy the original data
    to_send_with_semicolon[len] = '\0';
    int txBytes =
        uart_write_bytes(UART_NUM_0, to_send_with_semicolon,
                         len + 1);  // len + 1 to include the semicolon
    free(to_send_with_semicolon);
    return txBytes;
}

void bme680_test(void *pvParameters) {
    bme680_t sensor;
    memset(&sensor, 0, sizeof(bme680_t));
    // serial_write_bme("CF10", 4);

    ESP_ERROR_CHECK(bme680_init_desc(&sensor, BME_ADDR, PORT, I2C_MASTER_SDA_IO,
                                     I2C_MASTER_SCL_IO));

    // init the sensor
    ESP_ERROR_CHECK(bme680_init_sensor(&sensor));
    // serial_write_bme("CF20", 4);

    // Changes the oversampling rates to 4x oversampling for temperature
    // and 2x oversampling for humidity. Pressure measurement is skipped.
    bme680_set_oversampling_rates(&sensor, BME680_OSR_4X, BME680_OSR_NONE,
                                  BME680_OSR_2X);
    // serial_write_bme("CF30", 4);

    // Change the IIR filter size for temperature and pressure to 7.
    bme680_set_filter_size(&sensor, BME680_IIR_SIZE_7);

    // Change the heater profile 0 to 200 degree Celsius for 100 ms.
    bme680_set_heater_profile(&sensor, 0, 200, 100);
    bme680_use_heater_profile(&sensor, 0);
    // serial_write_bme("CF50", 4);

    // Set ambient temperature to 10 degree Celsius
    bme680_set_ambient_temperature(&sensor, 10);

    // as long as sensor configuration isn't changed, duration is constant
    uint32_t duration;
    bme680_get_measurement_duration(&sensor, &duration);
    // serial_write_bme("CF100", 5);

    TickType_t last_wakeup = xTaskGetTickCount();

    bme680_values_float_t values;
    char buf[100];
    while (1) {
        // trigger the sensor to start one TPHG measurement cycle
        if (bme680_force_measurement(&sensor) == ESP_OK) {
            // passive waiting until measurement results are available
            vTaskDelay(duration);

            // get the results and do something with them
            if (bme680_get_results_float(&sensor, &values) == ESP_OK)
                ESP_LOGI(
                    "bme-test",
                    "BME680 Sensor: %.2f °C, %.2f %%, %.2f hPa, %.2f Ohm\n",
                    values.temperature, values.humidity, values.pressure,
                    values.gas_resistance);
        }
        // passive waiting until 1 second is over
        int len;

        len = serial_read_bme(buf);
        if (len > 0) {
            if (buf[0] == 'G' && buf[1] == 'B') {  // get BME values
                // write values to buf and send them
                int loc = 2;
                // temperature
                memcpy(buf + loc, &values.temperature, sizeof(float));
                loc += sizeof(float);
                // humidity
                memcpy(buf + loc, &values.humidity, sizeof(float));
                loc += sizeof(float);
                // pressure
                memcpy(buf + loc, &values.pressure, sizeof(float));
                loc += sizeof(float);
                // gas_resistance
                memcpy(buf + loc, &values.gas_resistance, sizeof(float));
                loc += sizeof(float);
                serial_write_bme(buf, loc);
            }
        }
        vTaskDelayUntil(&last_wakeup, pdMS_TO_TICKS(1000));
    }
}

void bme_main(uint8_t mode) {
    bme_mode = mode;
    ESP_ERROR_CHECK(i2cdev_init());
    xTaskCreatePinnedToCore(bme680_test, "bme680_test",
                            configMINIMAL_STACK_SIZE * 8, NULL, 5, NULL,
                            APP_CPU_NUM);
}
