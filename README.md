# hiLight

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
|  | PUT | Set the window values | {"0":100,"1":100, ..., "5":100 } |

