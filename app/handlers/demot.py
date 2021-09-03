import os

from telegram import dp, bot
from aiogram.types import ContentType, InputFile, Message

from utils.demot import create_demot, count_frames
from utils.paths import filename_append
from utils.text import emoji_progress_bar

@dp.message_handler(content_types=ContentType.TEXT)
async def handle_reply(message: Message) -> None:
    if message.reply_to_message and "|" in message.text:
        # not sure about this one, but they all have file_id attribute
        if message.reply_to_message.sticker:
            img = message.reply_to_message.sticker
            format = ".png"
        elif message.reply_to_message.photo:
            img = message.reply_to_message.photo[0]
            format = ".png"
        elif message.reply_to_message.animation:
            img = message.reply_to_message.animation
            format = ".mp4"
        else:
            return

        file_in = img.file_id + format
        file_out = filename_append(file_in, "_out")
        text = message.text.split("|", 1)

        await bot.download_file_by_id(img.file_id, file_in)

        if format == ".mp4":
            total_frames = count_frames(file_in)
            progress_bar = await bot.send_message(message.chat.id, "progress: 0%\n🌚🌚🌚🌚")

            for frames in create_demot(file_in, file_out, text[0], text[1]):
                percent = int(frames / total_frames * 100)
                new = "progress: " + str(percent) + "%\n" + emoji_progress_bar(percent)
                if progress_bar.text != new: # crashes if edited message is identical
                    await progress_bar.edit_text(new)

            await progress_bar.delete()
            await bot.send_animation(message.chat.id, InputFile(file_out))

        else:
            create_demot(file_in, file_out, text[0], text[1])
            
            await bot.send_photo(message.chat.id, InputFile(file_out))

        os.remove(file_in)
        os.remove(file_out)