import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6125371162:AAEDZyFcOmjFtmef6ZYDsGjNu8sx-tm8uG4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJQBu62HpA2DqxX4yUkDpXAUZ7jKfNUuuXO5V8Zfyn2aaH0-VVxqR-LKV6hFBdi5V8KopLDc-vn7ENNdMVgzivm-QOrh0M6YSCaLTXrAREe58pBaVKf1SANb8W1AzjBAMylrlngXxik7PTRP8rwTqR1Vofx529SDmQMbdsv5PV40eHo-RIuIMzez78JtuOcZVk-wP4YK22iA5zRS7wa9l9xjPfYxUYWuJ2_rYuC6ex1uyBaWxwBu3r7CewNxiNyKv4lWdX1vUuh3pS-ZdJ6LBhMcxAjuVC9z9kox4B30N10YiRaF-7fbCnMU_yEe97u67rjlRFSRSsT_qO4rQMxZmxF-uYE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
