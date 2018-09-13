import variables.device as d

def check_device(nearby_devices):
    for addr, name in nearby_devices:
        if addr == d.deviceMacA and name == d.deviceName:
            return True
    return False
