import base64

ip="192.168.100.10" 
port="4444" 
key = b"X" * 32

def encrypt(data):
    return base64.b64encode(bytes(a ^ b for a, b in zip(data.encode(), (key *(len(data) // len(key) + 1))[:len(data)]))).decode()

print("ENCRYPTED_HOST_BASE64 =", encrypt(ip))
print("ENCRYPTED_PORT_BASE64 =", encrypt(port))

