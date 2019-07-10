# hiLight

## API Documentation

base url: https://c2xolt5232.execute-api.eu-central-1.amazonaws.com/xxx

| URL | Request | Description | Request body example |
|-----|---------|-------------|--------------|
| /profiles | GET | List all user profiles (name, preference and bool to indicate if use custom mode) | - |
| /profiles | POST | Create a new user with JSON data (name, preference and use_custom_mode) | {"name":"Adam", "wert":80, "custom":"True"} |
| /profiles/name | GET | Get the info for a specific user (name) | {"name":"Adam"} |
| /profiles/name | PUT | Update a user's preference and/or mode with JSON data (name, preference and use_custom_mode) | {"name":"Adam", "wert":80, "custom":"True"} |
| /operationmode | GET | Get the current operation mode (demo or custom) | - |
| /operationmode | PUT | SET the current operation mode (demo or custom) | {"demo":"True"} |
