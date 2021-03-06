from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters


REPO = "**ποΈ Repo :** [VcBot Repo](https://github.com/shivam-op/VcBot)\n\nπ **Github :** [WINZO VC BOT](https://github.com/shivam-op) \n\n**π   [Group](https://t.me/winzogold_discuss)  &  [Channel](https://t.me/winzo_gold_answers)   π**"
HOME_TEXT = "π **Hi [{}](tg://user?id={})**,\n\nI'm **wΓ¬Γ±ΕΊo Music Bot** \nI Can Play Radio/Stream Music In Channels & Groups 24x7 Nonstop!\n\n**π Happy Streaming π**"
HELP = """**Join @winzo_gold_answers and @winzogold_discuss to get more help!!

π·οΈ **Users Commands**:
\u2022 `/play`  -  Reply to an audio to play or add to queue.
\u2022 `/help`  -  Shows help for commands.
\u2022 `/playlist`  -  Shows the playlist.
\u2022 `/current`  -  Shows playing time of current track.
\u2022 `/song song name`  -  Download the song.

π·οΈ **Admin Commands**:
\u2022 `/skip x`  -  Skip current or x song. [ x >= 2 ]
\u2022 `/join`  -  Join voice chat of current group.
\u2022 `/leave`  -  Leave current voice chat.
\u2022 `/vc`  -  Check which VC is joined.
\u2022 `/stop`  -  Stop playing music.
\u2022 `/radio`  -  Start radio stream.
\u2022 `/stopradio`  -  Stop radio stream.
\u2022 `/replay`  -  Play from the beginning.
\u2022 `/clean`  -  Remove unused RAW PCM files.
\u2022 `/pause`  -  Pause playing music.
\u2022 `/resume`  -  Resume playing music.
\u2022 `/mute`  -  Mute the VC Bot.
\u2022 `/unmute`  -  Unmute the VC Bot.
\u2022 `/restart`  -  Restart the bot.
"""


@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('πΊ CHANNEL', url='https://t.me/winzo-gold-answers'),
        InlineKeyboardButton('ποΈ Group', url='https://t.me/winzogold_discuss'),
    ],
    [
        InlineKeyboardButton('π GitHub', url='https://t.me/shivam9412'),
 
    ],
    [
        InlineKeyboardButton('βοΈ HELP βοΈ', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)


@Client.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(REPO, disable_web_page_preview=True)


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
