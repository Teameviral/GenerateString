from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴀʟᴏ {}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ

sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ {}

ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴘᴇʀᴄᴀʏᴀ ʙᴏᴛ ɪɴɪ, 
1) ɢᴀᴜsᴀʜ ʙᴀᴄᴀ ᴘᴇsᴀɴ ɪɴɪ
2) ʙʟᴏᴋɪʀ ʙᴏᴛ ᴀᴛᴀᴜ ᴅᴇʟᴇᴛᴇ ᴄʜᴀᴛ

ʙᴏᴛ ɪɴɪ ʙᴇᴋᴇʀᴊᴀ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀɴᴛᴜ ᴋᴀᴍᴜ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴠɪᴀ ʙᴏᴛ. ʀᴇᴋᴏᴍᴇɴᴅᴀsɪ ᴊɪᴋᴀ ɪɴɢɪɴ ᴍᴇɴɢᴀᴍʙɪʟ sᴛʀɪɴɢ ɢᴜɴᴀᴋᴀɴ ᴀᴋᴜɴ ʟᴀɪɴ, ᴀɢᴀʀ ᴛɪᴅᴀᴋ ᴅᴇʟᴀʏ. ᴛᴇʀɪᴍᴀᴋᴀsɪʜ
ʙʏ @Mafia_TobaTZ
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💢 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 💢", callback_data="generate")],
        [InlineKeyboardButton(text="💢 Kembali 💢", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("💢 Start Generating Session 💢", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("💢 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 💢", callback_data="generate")],
        [InlineKeyboardButton("💢 ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ 💢", url="https://t.me/Mafia_TobaTZ")],
        [
            InlineKeyboardButton(" ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ❔", callback_data="help"),
            InlineKeyboardButton("💢 ᴀʙᴏᴜᴛ 💢", callback_data="about")
        ],
        [InlineKeyboardButton("↗️ ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴ ↗️", url="https://t.me/SharingUserbot")],
    ]

    # Help Message
    HELP = """
💢 **Available Commands** 💢

/about - 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗕𝗼𝘁 𝗶𝗻𝗶
/help - 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲
/start - 𝗠𝘂𝗹𝗮𝗶 𝗕𝗼𝘁
/generate - 𝗠𝘂𝗹𝗮𝗶 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻
/cancel - 𝗠𝗲𝗺𝗯𝗮𝘁𝗮𝗹𝗸𝗮𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀
/restart - 𝗠𝗲𝗺𝗯𝗮𝘁𝗮𝗹𝗸𝗮𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @StrinG_Pantek_Bot

𝗚𝗿𝗼𝘂𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 : [Gabung](https://t.me/SharingUserbot)

𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [Pyrogram](docs.pyrogram.org)

𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [Python](www.python.org)

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: @Mafia_Tobatz
    """
