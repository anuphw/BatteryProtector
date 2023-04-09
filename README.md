# BatteryProtector
Get notification when your laptop battery is almost full or empty

I recently had to change my laptop battery because it was swolen. One of the main reasons for it that I never unplug the charger. So I created a telegram bot to notify me when the battery is almost full or empty. 

I created a cronjob that runs the bot script whenever my laptop restarts.

#####  Installation:

```bash
git clone https://github.com/anuphw/BatteryProtector.git
cd BatteryProtector
python -m venv venv
source venv/bin/activate
pip install telebot
```

- You need to [create a telegram bot](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
- [Find your own chat id](https://www.alphr.com/find-chat-id-telegram/)
- Change TOKEN and MY_CHAT_ID in the battery_bot.py

```bash
python battery_bot.py
```
