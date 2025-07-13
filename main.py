import os
import requests
from datetime import datetime

# توکن ربات تلگرام و ID عددی چت شما
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "123456789")  # اینجا آی‌دی عددی خودت رو بذار

def get_fake_signal():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return f"🟢 سیگنال خرید EURUSD | زمان: {now} UTC\n⏳ تایم‌فریم: 15M\n📈 RSI: 28\n✅ کندل برگشتی شناسایی شد"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(url, data=data)
    return r.ok

if __name__ == "__main__":
    signal = get_fake_signal()
    if send_telegram_message(signal):
        print("سیگنال با موفقیت ارسال شد ✅")
    else:
        print("❌ ارسال سیگنال به مشکل خورد.")
