from detectors.icmp_flood import detect_icmp_flood
# from detectors.syn_flood import detect_syn_flood  # Import other detectors as needed
# from detectors.icmp_flood import detect_icmp_flood  # Import the ICMP flood detector
# from detectors.dns_tunneling import detect_dns_tunneling  # Import the DNS tunneling detector
# from sus_ports import detect_sus_ports  # Import the list of suspect ports
# from banned_geo_ips import detect_banned_geo_ips  # Import the banned geo IPs detector

def detect_all_attacks(packet):
    
    detect_icmp_flood(packet)
#     # Add other detection functions here as needed