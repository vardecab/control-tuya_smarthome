# control-tuya_smarthome

![Actively Maintained](https://img.shields.io/badge/Maintenance%20Level-Actively%20Maintained-green.svg)
<br>
![](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-blue)

>Python scripts that allow me to control Tuya-compatible smart Wi-Fi light bulbs & sockets at home. 

## Screenshots

![iTerm2_2021-10-05 02-50-34@2x](https://user-images.githubusercontent.com/6877391/135943559-f864c8ec-290e-4317-b127-f6262db4fb26.jpg)

## How to use 

Read [setup here](https://github.com/jasonacox/tinytuya#tinytuya-setup), then it should be pretty clear how to use this script.

I'm storing values in `constants.py` file which is excluded from this repo but you can hardcode these values if you want.

In:

```python
device = tinytuya.OutletDevice(constants.Lampki_device_ID, constants.Lampki_device_IP, constants.Lampki_device_key) # device = Lampki
```
replace: 
- `constants.Lampki_device_ID` to your `device_ID`, eg. `00000000000000000000`
- `constants.Lampki_device_IP` to your `device_IP`, eg. `192.168.1.200`
- `constants.Lampki_device_key` to your `device_key`, eg. `ab0000abc00bbaaa`

so it looks like this:
```python
device = tinytuya.OutletDevice('00000000000000000000', '192.168.1.200', 'ab0000abc00bbaaa') # device = Lampki
```

All these values can be taken from _Wizard_, [see more here](https://github.com/jasonacox/tinytuya#setup-wizard).

## Features

- Turn on a device 🟢
- Turn off a device 🔴

## Release History

- 0.1: Initial release with 4 devices; sensitive variables were hidden in another file.

## Versioning

Using [SemVer](http://semver.org/).

## License
![](https://img.shields.io/github/license/vardecab/control-tuya_smarthome)

## Acknowledgements

- [tinytuya](https://github.com/jasonacox/tinytuya)
- [Tuya IoT Platform](https://iot.tuya.com/)
- [How to get a value from a nested dictionary](https://stackoverflow.com/questions/25833613/safe-method-to-get-value-of-nested-dictionary)
- [Save secret stuff in a different file](https://stackoverflow.com/questions/6345840/whats-the-best-way-to-initialise-and-use-constants-across-python-classes)

## Contributing

![](https://img.shields.io/github/issues/vardecab/control-tuya_smarthome)

If you found a bug or want to propose a feature, feel free to visit [the Issues page](https://github.com/vardecab/control-tuya_smarthome/issues).
