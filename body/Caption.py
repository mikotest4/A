from pyrogram import *
from info import *
import asyncio
import sys
import os
import time
from Script import script
from .database import *
import re
from pyrogram.errors import FloodWait
from pyrogram.types import *
from pyrogram import errors

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"https://t.me/{bot.username}?startchannel=true")
            ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
        ]]
    )
    await message.reply_photo(
        photo=SILICON_PIC,
        caption=f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ »<a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛᴢ</a></b>",
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["total_users"]))
async def all_db_users_here(client, message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    await silicon.edit(f"Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        silicon = await message.reply_text("Getting All ids from database..\n Please wait")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...")
        async for user in all_users:
            try:
                await asyncio.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated += 1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked += 1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(e.x)
        await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
    else:
        await message.reply_text("Reply to a message to broadcast it to all users.")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await silicon.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Fixed set_cap command - works in both groups and channels
@Client.on_message(filters.command("set_cap") & (filters.group | filters.channel))
async def setCap(bot, message):
    print(f"set_cap command received in chat: {message.chat.id}")
    
    try:
        # Check if user is admin (for groups/channels)
        if message.chat.type in ["group", "supergroup", "channel"]:
            user_id = message.from_user.id
            chat_id = message.chat.id
            
            try:
                member = await bot.get_chat_member(chat_id, user_id)
                if member.status not in ["administrator", "creator"]:
                    return await message.reply("❌ You must be an admin to use this command!")
            except Exception as e:
                print(f"Error checking admin status: {e}")
                return await message.reply("❌ Error checking admin status!")
        
        # Check if caption is provided
        if len(message.command) < 2:
            return await message.reply(
                "**Usage:** `/set_cap Your caption here`\n\n**Available Variables:**\n"
                "`{file_name}` - Original File Name\n"
                "`{file_size}` - File Size\n"
                "`{language}` - Language of File\n"
                "`{year}` - Year from File\n"
                "`{default_caption}` - Original Caption\n\n"
                "**Example:**\n"
                "```\n/set_cap {file_name}\n\n⚙️ Size » {file_size}\n\n╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗\n💥 𝙅𝙊𝙄𝙉 :- @YourChannel\n╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝```"
            )
        
        # Extract caption from message
        caption = message.text.split("/set_cap", 1)[1].strip()
        
        if not caption:
            return await message.reply("❌ Please provide a caption!")
        
        chat_id = message.chat.id
        
        # Check if caption already exists
        chkData = await chnl_ids.find_one({"chnl_id": chat_id})
        if chkData:
            await updateCap(chat_id, caption)
            await message.reply(f"✅ **Caption Updated Successfully!**\n\n**New Caption:**\n{caption}")
        else:
            await addCap(chat_id, caption)
            await message.reply(f"✅ **Caption Set Successfully!**\n\n**Your Caption:**\n{caption}")
            
    except Exception as e:
        print(f"Error in set_cap: {e}")
        await message.reply(f"❌ Error setting caption: {str(e)}")

# Fixed del_cap command - works in both groups and channels
@Client.on_message(filters.command("del_cap") & (filters.group | filters.channel))
async def delCap(bot, message):
    print(f"del_cap command received in chat: {message.chat.id}")
    
    try:
        # Check if user is admin (for groups/channels)
        if message.chat.type in ["group", "supergroup", "channel"]:
            user_id = message.from_user.id
            chat_id = message.chat.id
            
            try:
                member = await bot.get_chat_member(chat_id, user_id)
                if member.status not in ["administrator", "creator"]:
                    return await message.reply("❌ You must be an admin to use this command!")
            except Exception as e:
                print(f"Error checking admin status: {e}")
                return await message.reply("❌ Error checking admin status!")
        
        chat_id = message.chat.id
        result = await chnl_ids.delete_one({"chnl_id": chat_id})
        
        if result.deleted_count > 0:
            await message.reply("✅ **Caption Deleted Successfully!**\n\nNow I will use my default caption.")
        else:
            await message.reply("❌ No custom caption found for this chat!")
            
    except Exception as e:
        print(f"Error in del_cap: {e}")
        await message.reply(f"❌ Error deleting caption: {str(e)}")

def extract_language(default_caption):
    if not default_caption:
        return "Hindi-English"
    
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Kannada|Bengali|Marathi|Gujarati|Punjabi|Urdu|Hin|Eng|Tam|Tel|Mal|Kan|Ben|Mar|Guj|Pun|Urd)\b'
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    
    if not languages:
        return "Hindi-English"
    
    # Convert short forms to full names
    lang_map = {
        'Hin': 'Hindi', 'Eng': 'English', 'Tam': 'Tamil', 'Tel': 'Telugu',
        'Mal': 'Malayalam', 'Kan': 'Kannada', 'Ben': 'Bengali', 'Mar': 'Marathi',
        'Guj': 'Gujarati', 'Pun': 'Punjabi', 'Urd': 'Urdu'
    }
    
    full_languages = []
    for lang in languages:
        full_languages.append(lang_map.get(lang, lang))
    
    return ", ".join(sorted(set(full_languages), key=str.lower))

def extract_year(default_caption):
    if not default_caption:
        return "2024"
    
    # Look for 4-digit years between 1900-2030
    match = re.search(r'\b(19[0-9]{2}|20[0-2][0-9]|2030)\b', default_caption)
    return match.group(1) if match else "2024"

@Client.on_message((filters.group | filters.channel) & filters.media & ~filters.command(["set_cap", "del_cap"]))
async def reCap(bot, message):
    if not message.media:
        return
    
    chnl_id = message.chat.id
    default_caption = message.caption or ""
    
    # Process different media types
    file_name = None
    file_size = None
    
    if message.document:
        file_name = message.document.file_name
        file_size = message.document.file_size
    elif message.video:
        file_name = getattr(message.video, 'file_name', None) or f"video_{message.video.file_unique_id}.mp4"
        file_size = message.video.file_size
    elif message.audio:
        file_name = getattr(message.audio, 'file_name', None) or f"audio_{message.audio.file_unique_id}.mp3"
        file_size = message.audio.file_size
    elif message.voice:
        file_name = f"voice_{message.voice.file_unique_id}.ogg"
        file_size = message.voice.file_size
    elif message.photo:
        file_name = f"photo_{message.photo.file_unique_id}.jpg"
        file_size = message.photo.file_size
    
    if not file_name or not file_size:
        return
    
    # Clean file name
    file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")
    
    # Extract language and year
    language = extract_language(default_caption)
    year = extract_year(default_caption)
    
    try:
        # Get custom caption or use default
        cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
        
        if cap_dets and cap_dets.get("caption"):
            caption_template = cap_dets["caption"]
        else:
            caption_template = DEF_CAP if DEF_CAP else default_caption
        
        # Replace variables in caption
        if caption_template:
            replaced_caption = caption_template.format(
                file_name=file_name,
                file_size=get_size(file_size),
                default_caption=default_caption,
                language=language,
                year=year
            )
            
            # Only edit if caption is different
            if replaced_caption != default_caption:
                await message.edit_caption(replaced_caption)
        
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        print(f"Error in reCap: {e}")

# Size conversion function
def get_size(size):
    if not size:
        return "Unknown"
    
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:
        i += 1
        size /= 1024.0
    return f"{size:.2f} {units[i]}"

@Client.on_callback_query(filters.regex(r'^start'))
async def start_callback(bot, query):
    await query.message.edit_text(
        text=script.START_TXT.format(query.from_user.mention),  
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"https://t.me/{bot.username}?startchannel=true")
                ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^help'))
async def help_callback(bot, query):
    await query.message.edit_text(
        text=script.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('About', callback_data='about')
            ],[
                InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True    
    )

@Client.on_callback_query(filters.regex(r'^about'))
async def about_callback(bot, query):
    await query.message.edit_text(
        text=script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='help')
            ],[
                InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True 
    )
