#!/usr/bin/env python3
"""
Correct IP Spoofer for Telegram
هەڵخەڵەتێنەری IP ڕاست بۆ تێلێگرام
"""

import requests
import random
import hashlib
from datetime import datetime

# ==================== CONFIG ====================
BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
CHAT_ID = "820421921"

class CorrectIPSpoofer:
    """هەڵخەڵەتێنەری IP ڕاست"""
    
    def __init__(self):
        self.bot_token = BOT_TOKEN
        self.chat_id = CHAT_ID
    
    def generate_valid_ipv4(self):
        """دروستکردنی IPv4 ڕاست"""
        # IPv4 ڕاستەقینە: هەر بەشێک 0-255
        return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    
    def generate_valid_ipv6(self):
        """دروستکردنی IPv6 ڕاست"""
        # IPv6 ڕاستەقینە: 8 بەش، هەر بەشێک 4 ژمارەیی
        parts = []
        for _ in range(8):
            # دروستکردنی 4 ژمارەیی hexadecimal
            part = format(random.randint(0x1000, 0xFFFF), 'x')
            parts.append(part)
        
        # لێکدان بە ":" 
        ipv6 = ":".join(parts)
        
        # کورتکردنەوەی IPv6 بە شێوەی ڕاست
        # نموونە: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
        return ipv6
    
    def generate_realistic_coordinates(self, country):
        """دروستکردنی GPS ڕاست"""
        coordinates = {
            "USA": {"lat_range": (25.0, 49.0), "lon_range": (-125.0, -65.0)},
            "UK": {"lat_range": (50.0, 59.0), "lon_range": (-8.0, 2.0)},
            "Germany": {"lat_range": (47.0, 55.0), "lon_range": (5.0, 15.0)},
            "France": {"lat_range": (41.0, 51.0), "lon_range": (-5.0, 9.0)},
            "Turkey": {"lat_range": (36.0, 42.0), "lon_range": (26.0, 45.0)},
            "UAE": {"lat_range": (22.0, 26.0), "lon_range": (51.0, 56.0)},
            "Iran": {"lat_range": (25.0, 40.0), "lon_range": (44.0, 63.0)},
            "Japan": {"lat_range": (24.0, 46.0), "lon_range": (122.0, 146.0)},
            "Australia": {"lat_range": (-44.0, -10.0), "lon_range": (113.0, 154.0)},  # ڕاستەقینە بۆ ئوسترالیا
            "Canada": {"lat_range": (42.0, 83.0), "lon_range": (-141.0, -52.0)},
            "China": {"lat_range": (18.0, 53.0), "lon_range": (73.0, 135.0)},
            "Brazil": {"lat_range": (-34.0, 5.0), "lon_range": (-74.0, -35.0)},
            "Russia": {"lat_range": (41.0, 82.0), "lon_range": (19.0, 190.0)},
            "India": {"lat_range": (8.0, 37.0), "lon_range": (68.0, 97.0)},
            "South Africa": {"lat_range": (-35.0, -22.0), "lon_range": (16.0, 33.0)},
        }
        
        if country in coordinates:
            lat_range = coordinates[country]["lat_range"]
            lon_range = coordinates[country]["lon_range"]
        else:
            # بۆ وڵاتە نەناسراوەکان
            lat_range = (-90.0, 90.0)
            lon_range = (-180.0, 180.0)
        
        lat = random.uniform(lat_range[0], lat_range[1])
        lon = random.uniform(lon_range[0], lon_range[1])
        
        return round(lat, 6), round(lon, 6)
    
    def generate_spoofed_info(self):
        """دروستکردنی زانیاری هەڵخەڵەتێنەری ڕاست"""
        # هەڵبژاردنی وڵات
        countries = {
            "USA": ["New York", "Los Angeles", "Chicago", "Miami", "Houston", "Phoenix"],
            "UK": ["London", "Manchester", "Birmingham", "Liverpool", "Glasgow"],
            "Germany": ["Berlin", "Munich", "Hamburg", "Cologne", "Frankfurt"],
            "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"],
            "Turkey": ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"],
            "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Al Ain"],
            "Iran": ["Tehran", "Mashhad", "Isfahan", "Karaj", "Shiraz", "Tabriz"],
            "Japan": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya"],
            "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],  # ڕاستەقینە
            "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
            "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"],
            "Brazil": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
            "Russia": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg"],
            "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
            "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria"],
        }
        
        country = random.choice(list(countries.keys()))
        city = random.choice(countries[country])
        
        # دروستکردنی IP ڕاستەکان
        fake_ips = []
        for _ in range(3):  # 3 IPv4
            fake_ips.append(self.generate_valid_ipv4())
        for _ in range(2):  # 2 IPv6
            fake_ips.append(self.generate_valid_ipv6())
        
        # GPS ڕاست
        lat, lon = self.generate_realistic_coordinates(country)
        
        # زانیاری تۆڕی ڕاست
        network_info = self.generate_realistic_network_info(country)
        
        return {
            'ips': fake_ips,
            'country': country,
            'city': city,
            'lat': lat,
            'lon': lon,
            'network': network_info,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def generate_realistic_network_info(self, country):
        """زانیاری تۆڕی ڕاست"""
        country_isps = {
            "USA": ["AT&T Internet", "Verizon Fios", "Comcast Xfinity", "Spectrum", "Google Fiber"],
            "UK": ["BT", "Virgin Media", "Sky Broadband", "TalkTalk", "EE"],
            "Germany": ["Deutsche Telekom", "Vodafone", "1&1", "O2", "Unitymedia"],
            "France": ["Orange", "SFR", "Free", "Bouygues Telecom"],
            "Turkey": ["Turk Telekom", "Turkcell", "Vodafone TR", "Türknet"],
            "UAE": ["Etisalat", "du", "Virgin Mobile UAE"],
            "Iran": ["Irancell", "Rightel", "MobinNet", "Shatel"],
            "Japan": ["NTT", "SoftBank", "KDDI", "Rakuten Mobile"],
            "Australia": ["Telstra", "Optus", "TPG", "Vodafone AU", "iiNet"],  # ڕاستەقینە
            "Canada": ["Bell Canada", "Rogers", "Telus", "Shaw", "Videotron"],
            "China": ["China Telecom", "China Mobile", "China Unicom"],
            "Brazil": ["Vivo", "Claro", "TIM Brasil", "Oi"],
            "Russia": ["Rostelecom", "MTS", "Beeline", "Megafon"],
            "India": ["Airtel", "Jio", "Vodafone Idea", "BSNL"],
            "South Africa": ["Vodacom", "MTN", "Telkom", "Cell C"],
        }
        
        country_vpns = {
            "USA": ["ExpressVPN", "NordVPN", "CyberGhost", "Private Internet Access"],
            "UK": ["Surfshark", "PureVPN", "Windscribe", "ProtonVPN"],
            "Germany": ["Hide.me", "ZenMate", "TunnelBear", "Avira Phantom"],
            "Japan": ["SoftEther VPN", "VPN Gate", "Radmin VPN"],
            "Australia": ["Ivacy", "CactusVPN", "SaferVPN"],
        }
        
        isp_list = country_isps.get(country, ["Global ISP", "International Network"])
        vpn_list = country_vpns.get(country, ["ExpressVPN", "NordVPN", "Surfshark"])
        
        devices = [
            ("iPhone 15 Pro", "iOS 17"),
            ("Samsung Galaxy S24", "Android 14"),
            ("Google Pixel 8", "Android 14"),
            ("Xiaomi 13", "Android 13"),
            ("Huawei P60", "HarmonyOS 3"),
            ("OnePlus 11", "Android 13"),
            ("iPad Pro", "iPadOS 17"),
            ("MacBook Pro", "macOS Sonoma"),
            ("Windows Laptop", "Windows 11"),
        ]
        
        device, os = random.choice(devices)
        
        browsers = [
            "Chrome 121",
            "Firefox 122", 
            "Safari 17",
            "Edge 121",
            "Opera 105",
            "Brave 1.60",
            "Vivaldi 6.5"
        ]
        
        return {
            'isp': random.choice(isp_list),
            'vpn': random.choice(vpn_list),
            'device': device,
            'os': os,
            'browser': random.choice(browsers),
            'network': random.choice(["WiFi", "4G", "5G", "Fiber", "Ethernet"]),
            'signal': f"{random.randint(65, 99)}%",
            'proxy': random.choice(["Disabled", "Enabled", "Auto"]),
            'ttl': random.randint(32, 255),
            'protocol': random.choice(["TCP", "UDP", "HTTP/2", "QUIC"]),
            'encryption': random.choice(["AES-256-GCM", "ChaCha20-Poly1305", "WireGuard"]),
            'dns': random.choice(["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]),
            'port': random.choice([80, 443, 8080, 8443, 53, 22])
        }
    
    def send_to_telegram(self):
        """ناردن بۆ تێلێگرام"""
        # دروستکردنی زانیاری
        info = self.generate_spoofed_info()
        
        # دروستکردنی پەیامی ڕاست
        message = self.create_correct_message(info)
        
        # ناردن
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {
                'chat_id': self.chat_id,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True
            }
            
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code == 200:
                # ناردنی پۆزیشن
                self.send_location(info['lat'], info['lon'])
                return True
            else:
                return False
                
        except Exception as e:
            print(f"❌ هەڵە: {e}")
            return False
    
    def create_correct_message(self, info):
        """دروستکردنی پەیامی ڕاست"""
        message = f"""
🎭 <b>CORRECT SPOOFED IP INFORMATION</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>📍 Valid IP Addresses:</b>
"""
        
        for i, ip in enumerate(info['ips'], 1):
            message += f"├ IP {i}: <code>{ip}</code>\n"
        
        # GPS ڕاست بۆ ئوسترالیا
        if info['country'] == "Australia":
            lat = random.uniform(-44.0, -10.0)  # ڕاستەقینە بۆ ئوسترالیا
            lon = random.uniform(113.0, 154.0)
            info['lat'] = round(lat, 6)
            info['lon'] = round(lon, 6)
        
        message += f"""
<b>🗺️ Realistic Location:</b>
├ Country: {info['country']}
├ City: {info['city']}
├ Coordinates: {info['lat']:.6f}, {info['lon']:.6f}
├ Google Maps: https://maps.google.com/?q={info['lat']},{info['lon']}
└ Accuracy: ~{random.randint(50, 5000)} meters

<b>📡 Network Information:</b>
├ ISP: {info['network']['isp']}
├ VPN: {info['network']['vpn']}
├ Device: {info['network']['device']}
├ OS: {info['network']['os']}
├ Browser: {info['network']['browser']}
├ Connection: {info['network']['network']}
└ Signal: {info['network']['signal']}

<b>🔧 Technical Details:</b>
├ Proxy: {info['network']['proxy']}
├ TTL: {info['network']['ttl']}
├ Protocol: {info['network']['protocol']}
├ DNS: {info['network']['dns']}
├ Port: {info['network']['port']}
└ Encryption: {info['network']['encryption']}

<b>⏰ Generated:</b> {info['timestamp']}
<b>🔒 Session ID:</b> {hashlib.md5(info['timestamp'].encode()).hexdigest()[:12]}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<i>🌐 Valid IP Spoofer • For Educational Purposes</i>
"""
        
        return message
    
    def send_location(self, lat, lon):
        """ناردنی پۆزیشن"""
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendLocation"
            payload = {
                'chat_id': self.chat_id,
                'latitude': lat,
                'longitude': lon,
                'horizontal_accuracy': random.randint(50, 1000)
            }
            
            requests.post(url, json=payload, timeout=5)
            
        except:
            pass

def main():
    """سەرەکی"""
    print("="*60)
    print("🎭 CORRECT IP SPOOFER FOR TELEGRAM")
    print("="*60)
    
    spoofer = CorrectIPSpoofer()
    
    print("\n🔧 دروستکردنی زانیاری ڕاستەقینە...")
    
    # ناردنی چەند پەیام
    for i in range(3):
        print(f"\n📤 ناردنی پەیامی {i+1}/3...")
        success = spoofer.send_to_telegram()
        
        if success:
            print(f"✅ پەیامی {i+1} نێردرا!")
        else:
            print(f"❌ پەیامی {i+1} شکستی هێنا!")
        
        if i < 2:
            import time
            time.sleep(2)
    
    print("\n✨ تەواو بوو! سەیری چاتی تێلێگرام بکە.")
    print(f"   Chat ID: {CHAT_ID}")
    print("   📍 3 پەیامی جیاواز نێردرا")

if __name__ == "__main__":
    main()
