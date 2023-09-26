import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()

if not roms:
    raise RuntimeError(" Found no:")



while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(ds_sensor.read_temp(rom))
    time.sleep(5)

