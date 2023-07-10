import time
from struct import pack, unpack

import serial
import serial.tools.list_ports


class SensorsConfig:
    def __init__(self, acc_sens, acc_odr, gyr_sens, gyr_odr, bme_mode, selected_sensor):
        self.acc_sens = acc_sens
        self.acc_odr = acc_odr
        self.gyr_sens = gyr_sens
        self.gyr_odr = gyr_odr
        self.bme_mode = bme_mode
        self.selected_sensor = selected_sensor

    def to_bytes(self):
        bytes_to_send = pack(
            "BBBBBB",
            self.acc_sens,
            self.acc_odr,
            self.gyr_sens,
            self.gyr_odr,
            self.bme_mode,
            self.selected_sensor,
        )
        return b"CS" + bytes_to_send

    @classmethod
    def from_bytes(cls, bytes):
        acc_sens, acc_odr, gyr_sens, gyr_odr, bme_mode = unpack("bbbbb", bytes)
        return cls(acc_sens, acc_odr, gyr_sens, gyr_odr, bme_mode)

    def __str__(self):
        values = {
            "acc_sens": self.acc_sens,
            "acc_odr": self.acc_odr,
            "gyr_sens": self.gyr_sens,
            "gyr_odr": self.gyr_odr,
            "bme_mode": self.bme_mode,
            "selected_sensor": self.selected_sensor,
        }
        return "SensorsConfig(" + ", ".join(f"{k}={v}" for k, v in values.items()) + ")"


class EspSerialComs:
    def __init__(self):
        self.serial_port = self.find_serial_ports()
        self.connected = False
        if self.serial_port is None:
            return None
        self.baud_rate = 115200
        self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
        time.sleep(2)  # wait a bit more for device to boot up
        self.connected = True
        self.config = None

    def send(self, msg):
        if self.ser.isOpen():
            print(f"Sending: {msg};")
            if type(msg) == str:
                msg = msg.encode()
            self.ser.write(msg + b";")
        else:
            print("Serial port is not open!")

    def config_sensors(self, sensors_config, progresBar=None):
        self.config = sensors_config
        self.send(sensors_config.to_bytes())
        response = ""
        tries = 5
        while tries > 0:
            response = self.read()
            # remove "CF"
            response = response.replace("CF", "")
            num = int(response)
            if progresBar is not None:
                progresBar.setProperty("value", num)
                if num == 100:
                    return True
            tries -= 1
        return False

    def get_data_bmi270(self):
        if self.config.selected_sensor == 0:
            self.send(b"GA")
            try:
                response = self.ser.read(39)
                print(len(response))
                response = response[2:38]
                data = unpack("fffffffff", response)
                return data
            except Exception as e:
                print(e)
                return self.get_data_bmi270()

    def get_data_bme688(self):
        if self.config.selected_sensor == 1:
            self.send(b"GB")
            try:
                # four floats
                response = self.ser.read(19)
                print(len(response))
                response = response[2:18]
                data = unpack("ffff", response)
                return data
            except Exception as e:
                print(e)
                return self.get_data_bme688()

    def read(self, in_bytes=False):
        while True:
            if self.ser.in_waiting > 0:
                message = self.ser.read_until(b"\x00")
                message = message[:-1]
                print("message", message)
                if in_bytes:
                    return message
                return message.decode("utf-8", "replace")

    def find_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        esp_port = None
        for port in ports:
            if "CP2102" in port.description:
                esp_port = port.device
        return esp_port
