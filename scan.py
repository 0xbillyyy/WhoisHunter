import socket
from ipwhois import IPWhois
from termcolor import colored
import pandas as pd
from datetime import datetime


class WhoisLookup:
    def __init__(self, domain: str):
        self.domain = domain
        self.ip = None
        self.results = None

    def fetch(self):
        try:
            # Resolve domain -> IP
            self.ip = socket.gethostbyname(self.domain)

            # RDAP Lookup
            obj = IPWhois(self.ip)
            self.results = obj.lookup_rdap()
            return True
        except Exception as e:
            print(colored("[!] Error: {} -> {}\n", "red").format(self.domain, e))
            return False

    def parse(self):
        if not self.results:
            return None

        data = {
            "domain": self.domain,
            "ip": self.ip,
            "asn": self.results.get("asn"),
            "provider": self.results.get("asn_description"),
            "country": self.results.get("asn_country_code"),
            "asn_date": self.results.get("asn_date"),
            "registrant_name": None,
            "registrant_address": None,
            "registrant_registered": None,
            "registrant_last_changed": None,
            "abuse_email": None,
            "abuse_phone": None,
        }

        for _, entity in self.results.get("objects", {}).items():
            roles = entity.get("roles", [])
            contact = entity.get("contact", {})

            #infone maszeh regist
            if "registrant" in roles:
                data["registrant_name"] = contact.get("name")
                if "address" in contact and contact["address"]:
                    data["registrant_address"] = contact["address"][0]["value"]

                #ambil tanggal regist
                for ev in entity.get("events", []):
                    if ev["action"] == "registration":
                        data["registrant_registered"] = ev["timestamp"]
                    elif ev["action"] == "last changed":
                        data["registrant_last_changed"] = ev["timestamp"]

            if "abuse" in roles:
                if contact.get("email"):
                    data["abuse_email"] = contact["email"][0]["value"]
                if contact.get("phone"):
                    data["abuse_phone"] = contact["phone"][0]["value"]

        return data


if __name__ == "__main__":
    print("""
    █   █ █  █ █▀▀█ ▀█▀ █▀▀▀ █  █ █  █ █▄ █ ▀█▀ █▀▀▀ █▀▀█ 
    █ █ █ █▀▀█ █  █  █  ▀▀▀█ █▀▀█ █  █ █ ▀█  █  █▀▀  █▄▄▀ 
    █▄▀▄█ █  █ █▄▄█  █  █▄▄█ █  █ █▄▄█ █  █  █  █▄▄▄ █  █     
    Copyright (c) 2025 0xbilly
    """)
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        domains = f.read().splitlines()

    results = []  #tampung untuk excel

    for d in domains:
        lookup = WhoisLookup(d)
        if lookup.fetch():
            info = lookup.parse()
            if info:
                results.append(info)

                print("Domain:", colored(info['domain'], "green", attrs=["bold"]))
                print("IP:", info['ip'])
                print("No ASN:", info['asn'])
                print("Provider:", info['provider'])
                print("Country:", info['country'])
                print("ASN Date:", info['asn_date'])
                print("Registrant Name:", info['registrant_name'])
                print("Registrant Address:", (info['registrant_address'] or "").replace("\n", " "))
                print("Registrant Registered:", info['registrant_registered'])
                print("Registrant Last Changed:", info['registrant_last_changed'])
                print("Abuse Email:", info['abuse_email'])
                print("Abuse Phone:", info['abuse_phone'])
                print()

    #simpan hasil di excel
    if results:
        now = datetime.now()
        name_file = "output/whois_output_" + now.strftime("%d_%m_%Y_%H_%M_%S")+".xlsx"
        df = pd.DataFrame(results)
        df.to_excel(name_file, index=False)
        print(colored(f"[+] Saved {len(results)} results to {name_file}", "cyan", attrs=["bold"]))
