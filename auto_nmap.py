import os
import subprocess

ip = input("[*] Enter the target: ")
file = input("[*] Enter the name of the file ")
ext = ".nmap"
name = file + ext

while True :
    port = input("[*] Do you want to scan all ports? ")

    if port.lower() == ("y") :
        nmap = subprocess.run(["nmap" , "-v", "-A", "-p-", "-T4", ip, "-oA", file])
        print(f"[*] Scan complete, file saved as {file}.nmap")
        break

    elif port.lower() == ("n") :
        nmap = subprocess.run(["nmap" , "-v", "-A", "-T4", ip, "-oA", file])
        print(f"[*] Scan complete, file saved as {file}.nmap")
        break

    elif port.lower() == ("q"):
        break

    else :
        print("[*] Please enter y or n! to exit press q")


while True:
    result = input("Do you want to investigate the results? ")
    
    if result.lower() == ("y"):
        subprocess.run(["less", name])       
        break

    elif result.lower() == ("n"):
        break
    
    else :
        print("Please answer y or n ")
        continue    


