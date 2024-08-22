# device_info.py
import platform

def get_device_info():
    info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return info

if __name__ == "__main__":
    device_info = get_device_info()
    for key, value in device_info.items():
        print(f"{key}: {value}")
