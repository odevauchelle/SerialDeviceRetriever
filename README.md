# SerialDeviceRetriever

A convenience function based on [pySerial](https://pyserial.readthedocs.io/en/latest/pyserial.html) to find specific USB devices, such as Arduino boards.

## Usage

List available devices:

```python
from SerialDeviceRetriever import *

show_devices( manufacturer = 'Arduino' )
```

```console
hwid  =  USB VID:PID=2341:0043 SER=85935333337351D04041 LOCATION=4-2:1.0
vid  =  9025
pid  =  67
serial_number  =  85935333337351D04041
location  =  4-2:1.0
manufacturer  =  Arduino (www.arduino.cc)
product  =  None
interface  =  None
usb_device_path  =  /sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2
device_path  =  /sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2/4-2:1.0
subsystem  =  usb
usb_interface_path  =  /sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2/4-2:1.0
```


Find a specific device based on its serial number:

```python
print( find_devices( serial_number = '85935333337351D04041', strict = True ) )
```

```console
[{'device': '/dev/ttyACM0', 'name': 'ttyACM0', 'description': 'ttyACM0', 'hwid': 'USB VID:PID=2341:0043 SER=85935333337351D04041 LOCATION=4-2:1.0', 'vid': 9025, 'pid': 67, 'serial_number': '85935333337351D04041', 'location': '4-2:1.0', 'manufacturer': 'Arduino (www.arduino.cc)', 'product': None, 'interface': None, 'usb_device_path': '/sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2', 'device_path': '/sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2/4-2:1.0', 'subsystem': 'usb', 'usb_interface_path': '/sys/devices/pci0000:00/0000:00:1a.1/usb4/4-2/4-2:1.0'}]
```
