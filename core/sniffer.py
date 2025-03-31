import pyshark
def start_sniffer(interface='Wlan0'):
    capture = pyshark.LiveCapture(interface=interface)
    print(f"Starting sniffer on interface {interface} with filters:")

    for packet in capture:
        try:
            field_names = packet.ip._all_fields
            field_values = packet.ip._all_fields.values()

            for field_name, field_value in zip(field_names, field_values):
                print(f"{field_name}: {field_value}")
                
                except Exception,AttributeError as error:
            print(f"Error processing packet: {error}")

if __name__ == "__main__":
    # Start the sniffer on the specified interface
    start_sniffer(interface='Wlan0')

