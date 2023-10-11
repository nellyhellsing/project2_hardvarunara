import machine
import onewire
import ds18x20
import time
import json

temp_config = open("config.json")

config = json.load(temp_config)

dat = machine.Pin(config["pin"])

temp_sensor = ds18x20.DS18X20(onewire.OneWire(dat))

roms = temp_sensor.scan()

id = machine.unique_id()

id_hex = id.hex()

while True:
    temp_sensor.convert_temp()
    time.sleep_ms(config["interval"])
    for rom in roms:
        roms_2 = hex(int.from_bytes(rom, "little"))
        print(id_hex[2:], roms_2[2:], temp_sensor.read_temp(rom), end=" ")
        print()
