# hiLight

hiLight is an automatic control system for smart windows. Using sensors and custom preferences, we ensure the perfect lighting for each employee in the office.

## Magic behind

![magic behind](https://i.imgur.com/HoE6zqv.png)

## Components

- [Frontend](https://github.com/manuel-lang/hiLight/tree/master/hilight): Setting custom lighting preferences and controlling smart windows directly if enabled.
- [Person detector](https://github.com/manuel-lang/hiLight/tree/master/demo_person): Automatic people detection on the outside of the window. Darkens the windows if people are detected.
- [Controlling](https://github.com/manuel-lang/hiLight/tree/master/iot): Control scripts for smart windows that can for instance be run from a Raspberry Pi.
- [Beacon scanner](https://github.com/manuel-lang/hiLight/blob/master/blescan.py): Detecting which person is in the office and at what distance of the windows.

## API Documentation

base url: https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx

| URL | Request | Description | Request body example |
|-----|---------|-------------|--------------|
| /profiles | GET | List all user profiles (name, preference and bool to indicate if use custom mode) | - |
|| POST | Create a new user with JSON data (name, preference and use_custom_mode) | {"name":"Adam", "wert":80, "custom":"True"} |
| /profiles/{name} | GET | Get the info for a specific user (name) | - |
| | PUT | Update a user's preference and/or mode with JSON data (name, preference and use_custom_mode) | { "wert":80, "custom":"True"} |
| /operationmode | GET | Get the current operation mode (demo or custom) | - |
|  | PUT | Set the current operation mode (demo or custom) | {"paint": "True", "detection": "True"} |
| /activeuser | GET | Get the currently active user's name | - |
|  | PUT | Set the currently active user's name | {"username":"Adam"} |
| /winstate | GET | Get all current window values | - |
|  | PUT | Set the window values | [{"0":100},{"1":100}, ..., {"5":100 }] |

