from datetime import datetime, timedelta
from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
from bot import user_time
from config import youtube_next_fetch
from helper.ytdlfunc import extractYt, create_buttons

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"


@Client.on_message(Filters.regex(ytregex))
async def ytdl(_, message):
    userLastDownloadTime = user_time.get(message.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            await message.reply_text(f"`Wait {wait_time} Minutes before next Request`")
            return
    except:
        pass

    url = message.text.strip()
    await message.reply_chat_action("typing")
    try:
        title, thumbnail_url, formats = extractYt(url)

        now = datetime.now()
        user_time[message.chat.id] = now + \
                                     timedelta(minutes=youtube_next_fetch)

    except Exception:
        await message.reply_text("`Fයූ ටියුබ් දත්ත ලබා ගැනීමට අපොහොසත් විය... 😓 \nPයූටියුබ් අවහිර කළ සේවාදායකය ip \n or ආරක්ෂිත වීඩියෝ බාගත කරන්න`")
        return
    buttons = InlineKeyboardMarkup(list(create_buttons(formats)))
    sentm = await message.reply_text("URL එක සකසමින් 😋😋😋")
    try:
        # Todo add webp image support in thumbnail by default not supported by pyrogram
        # https://youtu.be/_lGtWG8zTdU
        await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        await sentm.delete()
    except Exception as e:
        try:
            thumbnail_url = "https://telegra.ph/file/27b9b1d58c82a2343c3d8.jpg"
            await message.reply_photo(thumbnail_url, caption=title, reply_markup=buttons)
        except Exception as e:
            await sentm.edit(
            f"<code>{e}</code> #Error")

