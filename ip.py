#!/usr/bin/env python3
"""
IP Spoofer with Telegram
هەڵخەڵەتێنەری IP بۆ تێلێگرام
"""

import requests
import random
from datetime import datetime

# ==================== TELEGRAM CONFIG ====================
BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
CHAT_ID = "820421921"

class IPSpoofer:
    """هەڵخەڵەتێنەری IP"""
    
    def __init__(self):
        self.bot_token = BOT_TOKEN
        self.chat_id = CHAT_ID
    
    def generate_fake_ip(self):
        """دروستکردنی IP ساختەیی"""
        fake_ips = []
        
        # جۆری جیاوازی IP
        for _ in range(5):
            # IPv4 ساختەیی
            ipv4 = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            fake_ips.append(ipv4)
            
            # IPv6 ساختەیی
            ipv6 = ":".join([f"{random.randint(0x1000, 0xffff):x}" for _ in range(8)])
            fake_ips.append(ipv6)
        
        return fake_ips
    
    def generate_fake_location(self):
        """دروستکردنی شوێنی ساختەیی"""
        countries = {
            "USA": ["New York", "Los Angeles", "Chicago", "Miami"],
            "UK": ["London", "Manchester", "Liverpool"],
            "Germany": ["Berlin", "Munich", "Hamburg"],
            "France": ["Paris", "Marseille", "Lyon"],
            "Turkey": ["Istanbul", "Ankara", "Izmir"],
            "UAE": ["Dubai", "Abu Dhabi"],
            "Iran": ["Tehran", "Mashhad", "Isfahan"],
            "Japan": ["Tokyo", "Osaka", "Kyoto"],
            "Australia": ["Sydney", "Melbourne"],
            "Canada": ["Toronto", "Vancouver"]
        }
        
        country = random.choice(list(countries.keys()))
        city = random.choice(countries[country])
        
        # GPS ساختەیی
        if country in ["USA", "Canada"]:
            lat = random.uniform(25.0, 49.0)
            lon = random.uniform(-125.0, -65.0)
        elif country in ["UK", "Germany", "France"]:
            lat = random.uniform(35.0, 60.0)
            lon = random.uniform(-10.0, 40.0)
        elif country in ["Iran", "UAE", "Turkey"]:
            lat = random.uniform(25.0, 45.0)
            lon = random.uniform(25.0, 60.0)
        else:
            lat = random.uniform(-90.0, 90.0)
            lon = random.uniform(-180.0, 180.0)
        
        return {
            'country': country,
            'city': city,
            'lat': round(lat, 4),
            'lon': round(lon, 4),
            'coordinates': f"{lat:.4f}, {lon:.4f}"
        }
    
    def generate_fake_network_info(self):
        """زانیاری تۆڕی ساختەیی"""
        isps = [
            "AT&T Internet", "Verizon Fios", "Comcast Xfinity",
            "Spectrum", "Google Fiber", "T-Mobile 5G",
            "Vodafone", "Orange", "Deutsche Telekom",
            "Turkcell", "Etisalat", "MTN Irancell",
            "China Telecom", "NTT", "Telefonica"
        ]
        
        vpns = [
            "ExpressVPN", "NordVPN", "Surfshark",
            "CyberGhost", "Private Internet Access",
            "ProtonVPN", "Windscribe", "Hide.me"
        ]
        
        devices = [
            "iPhone 15 Pro", "Samsung Galaxy S24",
            "Google Pixel 8", "OnePlus 11",
            "Xiaomi 13", "Huawei P60"
        ]
        
        browsers = [
            "Chrome 121", "Firefox 122", "Safari 17",
            "Edge 121", "Opera 105", "Brave 1.60"
        ]
        
        return {
            'isp': random.choice(isps),
            'vpn': random.choice(vpns),
            'device': random.choice(devices),
            'browser': random.choice(browsers),
            'os': random.choice(["Windows 11", "macOS Sonoma", "Android 14", "iOS 17"]),
            'proxy': random.choice(["Enabled", "Disabled", "Unknown"]),
            'network': random.choice(["WiFi", "4G", "5G", "Fiber", "Ethernet"]),
            'signal': f"{random.randint(65, 99)}%"
        }
    
    def send_spoofed_info(self):
        """ناردنی زانیاری هەڵخەڵەتێنراو"""
        # دروستکردنی هەموو زانیارییەکان
        fake_ips = self.generate_fake_ip()
        location = self.generate_fake_location()
        network = self.generate_fake_network_info()
        
        # دروستکردنی پەیام
        message = f"""
🎭 <b>SPOOFED IP INFORMATION</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📍 Fake IP Addresses:</b>
"""
        
        for i, ip in enumerate(fake_ips[:5], 1):
            message += f"├ IP {i}: <code>{ip}</code>\n"
        
        message += f"""
<b>🗺️ Fake Location:</b>
├ Country: {location['country']}
├ City: {location['city']}
├ Coordinates: {location['coordinates']}
├ Google Maps: https://maps.google.com/?q={location['lat']},{location['lon']}
└ Accuracy: ~{random.randint(100, 5000)} meters

<b>📡 Network Info:</b>
├ ISP: {network['isp']}
├ VPN: {network['vpn']}
├ Device: {network['device']}
├ Browser: {network['browser']}
├ OS: {network['os']}
├ Network: {network['network']}
└ Signal: {network['signal']}

<b>🔧 Technical:</b>
├ Proxy: {network['proxy']}
├ TTL: {random.randint(32, 255)}
├ Protocol: {random.choice(['TCP', 'UDP', 'HTTP/2', 'QUIC'])}
└ Encryption: {random.choice(['AES-256', 'ChaCha20', 'WireGuard'])}

<b>⏰ Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<i>IP Spoofer • For Educational Purposes Only</i>
"""
        
        # ناردن بۆ تێلێگرام
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': False
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                print("✅ زانیاری هەڵخەڵەتێنراو بە سەرکەوتوویی نێردرا!")
                return True
            else:
                print(f"❌ هەڵە لە ناردن: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ هەڵە: {e}")
            return False

def main():
    """سەرەکی"""
    print("="*50)
    print("🎭 IP SPOOFER FOR TELEGRAM")
    print("="*50)
    
    spoofer = IPSpoofer()
    
    # ناردنی زانیاری هەڵخەڵەتێنراو
    print("\n🎭 دروستکردنی زانیاری هەڵخەڵەتێنراو...")
    success = spoofer.send_spoofed_info()
    
    if success:
        print("\n✨ تەواو بوو! سەیری چاتی تێلێگرام بکە.")
        print(f"   Chat ID: {CHAT_ID}")
    else:
        print("\n❌ نەتوانرا بنێردرێت!")

if __name__ == "__main__":
    main()
