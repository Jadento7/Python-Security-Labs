# FOR localhost/lab USE ONLY

import socket # Imports Python's socket module so we can create network connetions to test ports

PORT_NAMES = { # Creats a dictionary that stores port numbers as keys and service names as values
    20 : "FTP Data",
    21 : "FTP Control",
    22 : "SSH",
    23 : "Telnet",
    25 : "SMTP",
    53 : "DNS",
    80 : "HTTP",
    110 : "POP3",
    443 : "HTTPS",
    445 : "SMB",
    3389 : "RDP"
}

target = "127.0.0.1" # Sets the target IP address as 127.0.0.1 which is the local computer or the localhost

for port, service in PORT_NAMES.items(): # Loops through each port number and its matching service name
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Creates a TCP socket and automatically closes it when its done
        s.settimeout(0.5) # Sets a 0.5 second timeout so the program does not hang too long on closed or filtered ports

        status = s.connect_ex((target, port)) # Tries to connect to the target IP and port and returns 0 if the connection succeeds

        if status == 0: # Checks if connect_ex returned 0 which means that the port is opened
            print(f"{port} IS OPEN. SERVICE: {service}") # Prints that the port is open and shows its service name
        else: # Runs if the port is not open
            print(f"{port} IS CLOSED. SERVICE: {service}") # Prints that the port is closed and shows its service name
