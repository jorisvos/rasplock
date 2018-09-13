import bluetooth

def find_device():
    print("looking for devices...")
    nearby_devices = bluetooth.discover_devices(duration=2, lookup_names=True)

    print("found %d devices" % len(nearby_devices))
    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))

    return nearby_devices
