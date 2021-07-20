from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["tute"]))
async def start(client, message):
    await message.reply_text("To make a YouTube downloader pess ⚜️ Go whatsapp bot make ⚜️ button to go youtube directly to make whatsapp bot. 🥳",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go whatsapp bot make⚜️", url="https://youtu.be/_lGtWG8zTdU")]
        ]))
    
