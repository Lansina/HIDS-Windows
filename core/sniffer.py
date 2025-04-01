import pyshark
import logging
from detectors import detect_attacks  # Unified detector interface

# Use the same logger configuration
logger = logging.getLogger('detections_log')

def start_sniffer(interface='wlan0', bpf_filter= None):
    """
    Starts the packet sniffer on the specified interface.
    :param interface: The network interface to sniff on (default is 'wlan0').
    :param bpf_filter: A Berkeley Packet Filter (BPF) to filter packets at the capture level (default is 'ip').
    """
    try:
        # Initialize the packet capture with the specified interface and BPF filter
        capture = pyshark.LiveCapture(interface=interface, bpf_filter=bpf_filter)
        logger.info(f"Starting sniffer on interface {interface} with BPF filter '{bpf_filter}'...")

        # Continuously sniff packets from the network interface
        for packet in capture.sniff_continuously():
            try:
                # Forward the packet to detectors for analysis
                detect_attacks(packet)
            except Exception as e:
                # Log any errors that occur while processing a packet
                logger.error(f"Error processing packet: {e}")
    except Exception as e:
        # Log any critical errors that occur while starting or running the sniffer
        logger.critical(f"Critical error in sniffer: {e}")
    finally:
        # Notify the user that the sniffer has stopped
        logger.info("Sniffer stopped.")

if __name__ == "__main__":
    # Start the sniffer on the specified interface with a default BPF filter for IP packets
    start_sniffer(interface='Wlan0', bpf_filter=None)