# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""
#Contact = getenv("Contact", "")
API_ID = int(getenv("API_ID", "26468828"))
API_HASH = getenv("API_HASH", "4693513c08d1ac6af15f95b116c29478")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7517045929").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://chiruedizz:WmzSiQlS35fLDImn@cluster0.4o4zl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002621909293")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002487744426"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "modijiurl.com")
AD_API = getenv("AD_API", "71d8d386c59be6d3190202f69ff68e182c17bceb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
