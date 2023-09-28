import machine
import onewire
import ds18x20
import time
import json

temp_config = open("config.json")

config = json.load(temp_config)


# the device is on GPIO12
dat = machine.Pin(config["pin"])

# create the onewire objectd
ds = ds18x20.DS18X20(onewire.OneWire(dat))

roms = ds.scan()
id = machine.unique_id()

id_hex = id.hex()


# scan for devices on the bus


# loop 10 times and print all temperatures
while True:
    ds.convert_temp()
    time.sleep_ms(config["interval"])
    for rom in roms:
        roms_2 = hex(int.from_bytes(rom, "little"))
        print(id_hex[2:], roms_2[2:], ds.read_temp(rom), end=" ")
        print()
