blacklisted_ips = {"192.168.1.50", "10.0.0.99", "185.220.101.5", "172.16.0.5"}


raw_logs = [ 
"2026-06-02 10:01:22 - IP: 192.168.1.20 - Action: LOGIN_SUCCESS", 
"2026-06-02 10:02:05 - IP: 192.168.1.50 - Action: LOGIN_FAILED", 
"2026-06-02 10:03:11 - IP: 172.16.0.5 - Action: LOGIN_FAILED", 
"2026-06-02 10:03:45 - IP: 172.16.0.5 - Action: LOGIN_FAILED", 
"2026-06-02 10:04:12 - IP: 172.16.0.5 - Action: LOGIN_FAILED", 
"2026-06-02 10:05:00 - IP: 192.168.1.20 - Action: LOGIN_SUCCESS" 
]

failed_login_attempts = {}
events = []

for log in raw_logs:
    if "LOGIN_FAILED" in log:
        parts = log.split(' - ')
        ip_part = parts[1]
        # parts[1].replace("IP: ","")
        # parts[1].split()[1].strip()
        ip_address = parts[1].replace("IP: ","")
        timestamp = parts[0]

        alert_event = (timestamp, ip_address, "SUSPICIOUS")
        events.append(alert_event)
        # print(ip_address)

        failed_login_attempts[ip_address] = failed_login_attempts.get(ip_address,0) + 1

for ip, count in failed_login_attempts.items():
    if ip in blacklisted_ips and count > 1:
        print(f"ALERT: Suspicious activity from blacklisted IP: {ip}")

print(f"Events: {events}")
# print(f"failed Login counts: \n{failed_login_attempts}")