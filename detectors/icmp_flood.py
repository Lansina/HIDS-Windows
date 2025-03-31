from core.sniffer import start_sniffer

def detect_icmp_flood(packet):
    """
    Detects ICMP flood attacks based on the number of ICMP packets received in a short time frame.
    """
    # Check if the packet is an ICMP packet
    if 'ICMP' in packet:
        # Increment the count for ICMP packets
        detect_icmp_flood.icmp_count += 1

        # Check if the count exceeds a threshold (e.g., 100 packets in 1 second)
        if detect_icmp_flood.icmp_count > 100:
            print("ICMP Flood Attack Detected!")
            detect_icmp_flood.icmp_count = 0  # Reset count after detection

