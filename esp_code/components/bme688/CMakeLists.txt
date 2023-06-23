idf_component_register(SRCS "bme68x.c" "i2c_simple_main.c"
                       INCLUDE_DIRS "include"
                       REQUIRES driver esp_timer)

