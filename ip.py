باشە، با کۆدێکی زۆر سادە دروست بکەین بۆ تاقیکردنەوە:

١. کۆدی تاقیکردنەوەی زۆر سادە:

```python
"""
سادەترین تاقیکردنەوە - Simple Test
"""

import requests
import json

# زانیاریەکان
TOKEN = "8134629384:AAFZfoxW5-C0i8R_R3M51HUjSkquZT-inCw"
CHAT_ID = "820421921"

print("=" * 50)
print("📱 TELEGRAM TEST - سادەترین تاقیکردنەوە")
print("=" * 50)

# تاقیکردنەوەی ١: پشکنینی بۆت
print("\n1. پشکنینی بۆت...")
try:
    bot_check = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe", timeout=10)
    print(f"   وەڵام: {bot_check.status_code}")
    
    if bot_check.status_code == 200:
        bot_data = bot_check.json()
        if bot_data.get("ok"):
            print(f"   ✅ بۆتەکەت: @{bot_data['result']['username']}")
        else:
            print(f"   ❌ کێشە: {bot_data.get('description')}")
    else:
        print(f"   ❌ کێشەی HTTP: {bot_check.status_code}")
except Exception as e:
    print(f"   ❌ کێشە: {e}")

# تاقیکردنەوەی ٢: ناردنی پەیام
print("\n2. ناردنی پەیام...")
try:
    # دروستکردنی پەیام
    message_data = {
        "chat_id": CHAT_ID,
        "text": "🧪 تاقیکردنەوە لە Python\n✅ کاتی ناردن: ١٠ چرکە"
    }
    
    # ناردن
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json=message_data,
        timeout=10
    )
    
    print(f"   وەڵام: {response.status_code}")
    print(f"   زانیاری: {response.text[:100]}")
    
    if response.status_code == 200:
        print("   ✅ سەرکەوتوو بوو! پەیام نێردرا.")
        print("   📱 ئێستا بچۆ بۆ Telegramەکەت!")
    else:
        print("   ❌ شکستی هێنا. وەڵام:")
        print(f"   {json.dumps(response.json(), indent=2)}")
        
except Exception as e:
    print(f"   ❌ کێشە: {e}")

print("\n" + "=" * 50)
print("تاقیکردنەوە تەواو بوو!")
print("=" * 50)
```

٢. تاقیکردنەوەی ترمیناڵ:

```bash
python3 -c "
import requests
TOKEN = '8134629384:AAFZfoxW5-C0i8R_R3M51HUjSkquZT-inCw'
CHAT_ID = '820421921'

print('🔧 تاقیکردنەوە...')
print('=' * 40)

# تاقیکردنەوەی سەرەکی
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
data = {
    'chat_id': CHAT_ID,
    'text': '🔔 تاقیکردنەوەی ڕاستەوخۆ لە ترمیناڵ!'
}

try:
    r = requests.post(url, json=data, timeout=10)
    print(f'وەڵام: {r.status_code}')
    
    if r.status_code == 200:
        print('✅ سەرکەوتوو بوو!')
        print('📱 بچۆ بۆ Telegramەکەت!')
    else:
        print(f'❌ شکستی هێنا: {r.text}')
        
except Exception as e:
    print(f'❌ کێشە: {e}')
"
```

٣. تاقیکردنەوەی CURL (زۆر سادە):

```bash
curl -s -X POST "https://api.telegram.org/bot8134629384:AAFZfoxW5-C0i8R_R3M51HUjSkquZT-inCw/sendMessage" \
  -H "Content-Type: application/json" \
  -d '{"chat_id": "820421921", "text": "TEST FROM CURL"}' \
  | python3 -c "import sys, json; data=json.load(sys.stdin); print('✅ Success!' if data.get('ok') else f'❌ Error: {data}')"
```

٤. کۆدی تەواو بۆ ناردنی زانیاری تۆڕ:

```python
"""
سیستەمی ناردنی زانیاری تۆڕ - Network Info Sender
"""

import socket
import requests
from datetime import datetime
import time

# زانیاریەکان
TOKEN = "8134629384:AAFZfoxW5-C0i8R_R3M51HUjSkquZT-inCw"
CHAT_ID = "820421921"

def get_network_info():
    """وەرگرتنی زانیاری تۆڕ"""
    info = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'public_ip': 'نەناسراو',
        'local_ip': 'نەناسراو',
        'system': 'نەناسراو'
    }
    
    # IP ناوخۆیی
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        info['local_ip'] = s.getsockname()[0]
        s.close()
    except:
        pass
    
    # IP گشتی
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        info['public_ip'] = response.text
    except:
        pass
    
    # سیستم
    try:
        import platform
        info['system'] = platform.system()
    except:
        pass
    
    return info

def send_to_telegram(message):
    """ناردنی پەیام بۆ Telegram"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        return response.status_code == 200
    except:
        return False

def main():
    """بەرنامەی سەرەکی"""
    print("🌐 سیستەمی زانیاری تۆڕ")
    print("=" * 40)
    
    # وەرگرتنی زانیاری
    print("\n🔍 وەرگرتنی زانیاری تۆڕ...")
    network_info = get_network_info()
    
    # پیشاندان
    print("\n📊 زانیاریەکان:")
    print(f"   کات: {network_info['time']}")
    print(f"   IP گشتی: {network_info['public_ip']}")
    print(f"   IP ناوخۆیی: {network_info['local_ip']}")
    print(f"   سیستم: {network_info['system']}")
    
    # دروستکردنی پەیام
    message = f"""🌐 ڕاپۆرتی تۆڕ
⏰ کات: {network_info['time']}
🌍 IP گشتی: {network_info['public_ip']}
🏠 IP ناوخۆیی: {network_info['local_ip']}
💻 سیستم: {network_info['system']}
    
✅ ئەمە تاقیکردنەوەیەکی سادەیە"""
    
    # پرسیار بۆ ناردن
    choice = input("\n📱 ئایا دەتەوێت بڕێتە Telegram؟ (بەڵێ/نەخێر): ").strip().lower()
    
    if choice in ['بەڵێ', 'yes', 'y', 'ب']:
        print("\n📤 ناردن بۆ Telegram...")
        
        if send_to_telegram(message):
            print("✅ سەرکەوتوو بوو! پەیام نێردرا.")
            print("📱 ئێستا بچۆ بۆ Telegramەکەت!")
        else:
            print("❌ شکستی هێنا. پەیام نەنێردرا.")
    else:
        print("\n👋 پەیام نەنێردرا.")
    
    print("\n" + "=" * 40)
    print("کۆتایی")

if __name__ == "__main__":
    main()
```

---

ئەنجامی کۆدی یەکەمم پێ بڵێ! پێویستە ببینین چ کێشەیەک هەیە.
