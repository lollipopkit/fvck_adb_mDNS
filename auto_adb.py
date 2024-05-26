#!/usr/bin/env python3

import subprocess
import re
import sys

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

PRINT = True

def exec(args):
    return subprocess.run(args, capture_output=True, text=True)

def print(str):
    if PRINT:
        print(str)

def ok(str):
    print(f"{GREEN}{str}{RESET}")

def err(str):
    print(f"{RED}{str}{RESET}")

def find_adb_services():
    try:
        result = exec(['avahi-browse', '-rt', '_adb-tls-connect._tcp'])
        if result.returncode != 0:
            err("Can't exec avahi-browse")
            return None
        return result.stdout
    except Exception as e:
        err(f"Err: {e}")
        return None

def extract_ip_and_port(service_output):
    ip = re.findall(r'address = \[(.*?)\]', service_output)
    port = re.findall(r'port = \[(\d+)\]', service_output)
    if ip and port:
        unique_ip_ports = set(zip(ip, port))
        return list(unique_ip_ports)
    else:
        return None

def connect_to_adb(ip_port_list):
    for ip, port in ip_port_list:
        try:
            result = exec(['adb', 'connect', f'{ip}:{port}'])
            if result.returncode == 0:
                ok(f"Connected {ip}:{port}")
            else:
                err(f"Failed {ip}:{port}")
        except Exception as e:
            err(f"Err: {e}")

def main():
    print("Saerching...")
    service_output = find_adb_services()
    if not service_output:
        print("Can't find any adb services.")
        return

    ip_port_list = extract_ip_and_port(service_output)
    if not ip_port_list:
        print("Can't extract ip and port.")
        return

    print(f"Trying to connect to: {ip_port_list}")
    connect_to_adb(ip_port_list)

if __name__ == '__main__':
    args = sys.argv
    if '--no-print' in args:
        PRINT = False
    main()
