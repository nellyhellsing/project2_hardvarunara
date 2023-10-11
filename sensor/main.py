import machine
import onewire
import ds18x20
import time
import json


# Open and load the configuration file (config.json)
temp_config = open("config.json")
config = json.load(temp_config)

# Initialize the one-wire data pin using the pin specified in the configuration
dat = machine.Pin(config["pin"])

# Initialize the DS18X20 temperature sensor on the one-wire
temp_sensor = ds18x20.DS18X20(onewire.OneWire(dat))

# Scan for DS18B20 temperature sensor devices on the one-wire
roms = temp_sensor.scan()

# Get the unique ID of the Raspberry Pi Pico in hexadecimal
id = machine.unique_id()
id_hex = id.hex()

# Loop to continuously measure and report temperature
while True:
    temp_sensor.convert_temp()
    
    # Delay for the specified interval before reading temperatures again
    time.sleep_ms(config["interval"]) 
    for rom in roms:
        roms_2 = hex(int.from_bytes(rom, "little"))
        print(id_hex[2:], roms_2[2:], temp_sensor.read_temp(rom), end=" ")
        print()  # Print a new line to separate readings
