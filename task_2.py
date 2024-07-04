
import requests
import subprocess
import re
import json

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    subdomains = set()
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            subdomain = entry['name_value']
            subdomains.update(subdomain.split('\n'))
    return subdomains

def perform_nmap_scan(target):
    # Using subprocess to run nmap and capture the output
    result = subprocess.run(['nmap', '-sV', '-oX', '-', target], capture_output=True, text=True)
    return result.stdout

def gather_http_headers(target):
    url = f"http://{target}"
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
    except requests.RequestException as e:
        headers = str(e)
    return headers

def analyze_nmap_output(nmap_output):
    vulnerabilities = []
    # Basic check for outdated software versions
    outdated_services = re.findall(r'product="(.*?)" version="(.*?)"', nmap_output)
    for service in outdated_services:
        product, version = service
        vulnerabilities.append(f"Outdated software detected: {product} version {version}")
    return vulnerabilities

def main():
    domain = input("Enter the target domain: ")
    
    # Step 1: Information Gathering
    print("[*] Finding subdomains...")
    subdomains = find_subdomains(domain)
    print(f"Found subdomains: {subdomains}")
    
    for subdomain in subdomains:
        print(f"\n[*] Scanning subdomain: {subdomain}")
        
        print("[*] Performing port scan using Nmap...")
        nmap_output = perform_nmap_scan(subdomain)
        print(nmap_output)
        
        print("[*] Gathering HTTP headers...")
        headers = gather_http_headers(subdomain)
        print(headers)
        
        # Step 2: Security Audit
        print("[*] Analyzing Nmap output for vulnerabilities...")
        vulnerabilities = analyze_nmap_output(nmap_output)
        if vulnerabilities:
            for vulnerability in vulnerabilities:
                print(f"[!] Vulnerability found: {vulnerability}")
        else:
            print("[*] No vulnerabilities found.")

if __name__ == "__main__":
    main()
