# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To @ReshamOwner
# Update Channel @Digital_Botz & @DigitalBotz_Support
"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "20018243")
    API_HASH = os.environ.get("API_HASH", "81233670b0c1e1b726199bcd4ca3effc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8154879802:AAHi9doM-9du3nbjTXO7cXkS3eLBcZy80bI") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAtdNIABm8Jc5PIRNo599DWD3GDB7TYYNC8L-7uFZT-uUvUcXGWjaIO_lhgHuItABW5jT_RHxk-MfvBHBYMplwVEMa4rSqbvbhYmSBaL9Hmft4U2AW-WcqlHPkuJK93nUfJ7T4b2FWAKgRJzClJxtQqi3NKloktVRqDqz8P61U0XG5u6upNW9smq29tizEtSvRzd-mEna6WE3umc1Kc7ajInid0Fb2mjr4K_xQ2qfRBaZA8ltCyD8U8yekVXhRWtzq1O7cqxgupBBPcwh8YBTrtuSGiHD35zel2Jwz75luHgac4Q1VD9I7fovfSf4ZE07-QbRu-671ARK1WimL7fqoPAOQjQwAAAAHmEZc6AQ")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","cluster0")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://TelegramBots:TelegramBots@cluster0.ztttygj.mongodb.net/")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/dd0fbb16126ef132a76f2-1470dc1c3386a5a442.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7195674717').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002178664515"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6267863649 # calculation 6*1024*1024*1024=results
    
    #vforce subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "FOXMOVIESOFFICIALCHANNEL")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "FOXMOVIESOFFICIALCHANNEL")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """<b>Hᴇʏ, {}👋

Tʜɪs Is Aɴ Aᴅᴠᴀᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀғᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oғ Yᴏᴜʀ Fɪʟᴇ Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ Tʜɪs Bᴏᴛ Aʟsᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ

Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : \n<a href=https://t.me/UmeshGurjar1390>😊Dᴇᴠɪʟ Lᴜᴄɪғᴇʀ💞</b></a>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {@samples_renames_bot}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : {@FOXMOVIESOWNER}
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : {}
├📕 Lɪʙʀᴀʀy : {}
├✏️ Lᴀɴɢᴜᴀɢᴇ: {}
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: {}
├📊 ᴠᴇʀsɪᴏɴ: <a href=https://github.com/UmeshGurjar>{}</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
<b>•></b> /start Tʜᴇ Bᴏᴛ.

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Umeshgurjar9763>Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</b></a>
"""

    UPGRADE= """
•⪼ ★Pʟᴀɴs -  ⏳ Dᴀᴛᴇ  💸Pʀɪᴄᴇ.
•⪼ 🏆 Pʀᴏ - 𝟷 Mᴏɴᴛʜ -𝟷𝟽𝟿 - 𝟷𝟶𝟶ɢʙ
•⪼ 💎 Uʟᴛʀᴀ Pʀᴏ - 𝟷Mᴏɴᴛʜ 𝟷𝟿𝟿- 𝟷𝟶𝟶𝟶ɢʙ</b>

- Discount All Plans.19
    """
    THUMBNAIL = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>

<b>•></b> Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
"""
    CAPTION= """
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

Exᴀᴍᴩʟᴇ:- `/set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`
"""
    BOT_STATUS = """
⚡️ ʙᴏᴛ sᴛᴀᴛᴜs ⚡️

⌚️ ʙᴏᴛ ᴜᴩᴛɪᴍᴇ: `{}`
👭 ᴛᴏᴛᴀʟ ᴜsᴇʀꜱ: `{}`
💸 ᴛᴏᴛᴀʟ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs: `{}`
֍ ᴜᴘʟᴏᴀᴅ: `{}`
⊙ ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
"""
    LIVE_STATUS = """
⚡ ʟɪᴠᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ⚡

ᴜᴘᴛɪᴍᴇ: `{}`
ᴄᴘᴜ: `{}%`
ʀᴀᴍ: `{}%` 
ᴛᴏᴛᴀʟ ᴅɪsᴋ: `{}`
ᴜsᴇᴅ sᴘᴀᴄᴇ: `{} {}%`
ғʀᴇᴇ sᴘᴀᴄᴇ: `{}`
ᴜᴘʟᴏᴀᴅ: `{}`
ᴅᴏᴡɴʟᴏᴀᴅ: `{}`
V𝟹.𝟶.𝟶 [STABLE]
"""
    DIGITAL_METADATA = """
❪ SET CUSTOM METADATA ❫

- /metadata - Tᴏ Sᴇᴛ & Cʜᴀɴɢᴇ ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @GMoviesX" -metadata author="@umeshgurjar1390" -metadata:s:s title="Subtitled By :- @UmeshGurjar1390" -metadata:s:a title="By :- @UmeshGurjar1390" -metadata:s:v title="By:- @UmeshGurjar1390" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @GmoviesX
"""
    
    CUSTOM_FILE_NAME = """
<u>🖋️ Custom File Name</u>

you can pre-add a prefix and suffix along with your new filename

➢ /set_prefix - To add a prefix along with your _filename.
➢ /see_prefix - Tᴏ Sᴇᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /del_prefix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Pʀᴇғɪx !!
➢ /set_suffix - To add a suffix along with your filename_.
➢ /see_suffix - Tᴏ Sᴇᴇ Yᴏᴜʀ Sᴜғғɪx !!
➢ /del_suffix - Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Sᴜғғɪx !!

Exᴀᴍᴩʟᴇ:- `/set_suffix @GMoviesX`
Exᴀᴍᴩʟᴇ:- `/set_prefix @GMoviesX`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
    
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/Umeshgurjar1390>File-Rename-Bot</a>

• ❣️ <a href=https://t.me/UmeshGurjar1390>Dᴇᴠɪʟ Lᴜᴄɪғᴇʀ</a>
• ❣️ <a href=https://t.me/ganeshgurjar0069>Ganesh Gurjar</a> """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @Rkn_Bots" -metadata author="@RknDeveloper" -metadata:s:s title="Subtitled By :- @Rkn_Bots" -metadata:s:a title="By :- @Rkn_Bots" -metadata:s:v title="By:- @RknDeveloper" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @GmoviesX
"""
    
    RKN_PROGRESS = """<b>\n
╭━━━━❰UG PROCESSING...❱━➣
┣⪼ 📂 Sɪᴢᴇ : {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴘᴇᴇᴅ : {3}/s
┣⪼ ⏰️ ETA : {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
