import subprocess
from termcolor import colored
import pyfiglet
import re


def print_banner():
    banner = pyfiglet.figlet_format("DIESY")
    print(colored(banner, 'cyan'))
    print(colored("For Mohammed Ilkhadry\n", 'yellow'))
    print(colored("Open Vulnerability Scanning Tool\n", 'green'))


vulnerable_services = {
    "OpenSSH 7.2p2": "CVE-2016-3115",
    "vsftpd 2.3.4": "CVE-2011-2523",
    "Apache 2.4.49": "CVE-2021-41773",
    "Microsoft IIS httpd 7.5": "CVE-2010-2730",
}


def scan_target(target):
    print(f"\nجاري التحقق {target}...\n")
    try:
        result = subprocess.check_output(["nmap", "-sV", target], text=True)

        print(result)  
        
        lines = result.split("\n")
        print(colored("\n[+] Results:", "cyan"))

        for line in lines:
            if re.search(r"^[0-9]+/", line):  
                if any(service in line for service in vulnerable_services):
                    for service, cve in vulnerable_services.items():
                        if service in line:
                            print(colored(f"{line} | Potential vulnerabilities: {cve}", "red"))
                else:
                    print(line)

    except FileNotFoundError:
        print(colored("Error Requirements Not Found", "red"))
    except subprocess.CalledProcessError as e:
        print(colored("Error during operation", "red"))
        print(e)

if __name__ == "__main__":
    print_banner()
    target = input("Enter IP address or domain name: ")
    scan_target(target)
