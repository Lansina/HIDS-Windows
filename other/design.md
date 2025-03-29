--------------------------------------------
🧪 Detection Goals — Phase 1

- Detect outbound or inbound IPs from restricted countries
- Identify traffic on sensitive ports (21, 23, 445, 3389)
- Flag repeated SYNs indicating port scanning
- Detect beaconing or DNS tunneling patterns
- Look for traffic from tools with abnormal user agents (e.g. curl/sqlmap)
- Monitor for unusual outbound/inbound data spikes

HIDS-Windows/
├── core/                    # Core logic of the HIDS system
│   ├── sniffer.py           # Captures network packets using pyshark
│   ├── geo_checker.py       # Performs GeoIP lookups to detect risky countries
│   ├── rules_engine.py      # Calls detection logic for known attack patterns
│   └── logger.py            # Logs flagged events and manages output files
│
├── detectors/              # (Optional) Attack detection modules
│   ├── syn_flood.py         # Detects SYN flood behavior
│   ├── port_scan.py     # Detects possible DNS tunneling traffic
│   └── sus_ports.py        # Detects suspicious HTTP user agents
│     ---icmp_flood.py
├── tests/                  # (Future) Unit tests or stress test simulations
│   └── test_packets.py      # Example test script with mock packets
│
├── logs/                   # Stores runtime logs and alerts
│   └── detections.log       # Detailed alert logs with timestamp and reasons
│
├── flagged_ips.txt         # Quick list of flagged IPs for review/blocking
├── GeoLite2-Country.mmdb   # GeoIP2 database file for country lookups
├── main.py                 # Main entry point that ties all modules together
├── requirements.txt        # Lists all pip dependencies (e.g., pyshark, geoip2)
├── .gitignore              # Ignores venv, logs, cache, and sensitive files
└── README.md or design.md  # Markdown file explaining project design