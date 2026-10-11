import os
import requests
import time

TOKEN = os.getenv("TOKEN")
WEB_APP_URL = "https://akashgurjar1202-stack.github.io/my-telegram-webapp/"

def send_message(chat_id, text, reply_markup=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(url, json=payload)

def main():
    if not TOKEN:
        print("Error: TOKEN nahi mila!")
        return

    print("Bot is running...")
    offset = 0
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset={offset}&timeout=30"
            response = requests.get(url).json()
            
            if "result" in response:
                for result in response["result"]:
                    offset = result["update_id"] + 1
                    
                    if "message" in result:
                        msg = result["message"]
                        chat_id = msg["chat"]["id"]
                        
                        # Agar user ne web app data bheja (Claim button click kiya)
                        if "web_app_data" in msg:
                            data = msg["web_app_data"]["data"]
                            if "claim_reward" in data:
                                send_message(chat_id, "🎉 Badhai ho! Aapka reward successfully claim ho gaya hai!")
                        
                        # Agar user ne /start bheja
                        elif "text" in msg and msg["text"] == "/start":
                            keyboard = {
                                "inline_keyboard": [[
                                    {
                                        "text": "🎨 Open Colorful Menu",
                                        "web_app": {"url": WEB_APP_URL}
                                    }
                                ]]
                            }
                            send_message(chat_id, "Welcome! Click the button below to open your colorful Telegram Mini App:", reply_markup=keyboard)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()
