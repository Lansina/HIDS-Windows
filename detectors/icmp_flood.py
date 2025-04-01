from collections import defaultdict
import time
import logging

logger = logging.getLogger('detections_log')

icmp_tracker = defaultdict(list)

def detect_icmp_flood(packet):
 
    if 'ICMP' in packet:
        src_ip = packet.ip.src
        current_time = time.time()

        icmp_tracker[src_ip].append(current_time)
        icmp_tracker[src_ip] = [t for t in icmp_tracker[src_ip] if current_time - t < 1]  # Keep only timestamps within the last second

        if len(icmp_tracker[src_ip]) > 100:
            logger.warning(f"ICMP flood detected from {src_ip}")

