import os
import json
from Firewall import Firewall

CSV_FILE = "test.csv"

def main():
    fw = Firewall(CSV_FILE)
    fw.construct_knowledge_base()
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
    
if __name__ == "__main__":
    main()
