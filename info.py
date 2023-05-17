import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('BQGZ4aYAb7SbzAcwkRxG_ICO_fcDZMR6BIO3vIKApsfqKWJT-2-_oaEVmxn1CXvx-hi9s14_ennY0WMclgKkTQaFT-aQqN4HSt5BdRQJ6B99Er0pmAR5iij29Axu0RGVP8Zf3YqX7_hHFxYKkPm0MwpEjGvRNQT8ZqQssm2mcMF1O2sM5CI3YA7JgkYuOJeDKtNiyOXr0Y_kKp-tQaiUYkFq-D1jrHoNzHS2oMBU77b10gFiZHIBDD0kd4x9-17HB4OG-33qjcMMUPbFv-dkpYDueIX8HerB0v2yb6OItXiXq7rAuJX_mj5-yGt_eOSq275A4iMUDH1DzeM4WAAaiB4QZAIXvwAAAAFnifBOAA', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['26861990'])
API_HASH = environ['0592761ae3a24dcf709d85ab87bc12b9']
BOT_TOKEN = environ['0592761ae3a24dcf709d85ab87bc12b9']
USERBOT_STRING_SESSION = environ.get('BQGZ4aYAb7SbzAcwkRxG_ICO_fcDZMR6BIO3vIKApsfqKWJT-2-_oaEVmxn1CXvx-hi9s14_ennY0WMclgKkTQaFT-aQqN4HSt5BdRQJ6B99Er0pmAR5iij29Axu0RGVP8Zf3YqX7_hHFxYKkPm0MwpEjGvRNQT8ZqQssm2mcMF1O2sM5CI3YA7JgkYuOJeDKtNiyOXr0Y_kKp-tQaiUYkFq-D1jrHoNzHS2oMBU77b10gFiZHIBDD0kd4x9-17HB4OG-33qjcMMUPbFv-dkpYDueIX8HerB0v2yb6OItXiXq7rAuJX_mj5-yGt_eOSq275A4iMUDH1DzeM4WAAaiB4QZAIXvwAAAAFnifBOAA')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://jayvora:1850@cluster.t5ql7o3.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['Cluster']
COLLECTION_NAME = environ.get( 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
