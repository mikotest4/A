from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

# Dictionary to store users waiting for word input
waiting_for_words = {}

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)

    # Get bot info to access username
    bot_info = await bot.get_me()
    bot_username = bot_info.username

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ᴍᴀᴋᴇ ᴍᴇ ʏᴏᴜʀ", url=f"https://t.me/Furina_Capbot?startchannel=true")
            ],
            [
                InlineKeyboardButton("ʏ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴀ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴇ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴍ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ɪ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴋ", url="https://t.me/Yae_X_Miko"),
                InlineKeyboardButton("ᴏ", url="https://t.me/Yae_X_Miko")
            ]
        ]
    )

    await message.reply_photo(
        photo=YAE_MIKO_PIC,
        caption=f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</b>",
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

# FIXED: set_cap command with better multiline handling
@Client.on_message(filters.command("set_cap") & (filters.private | filters.group | filters.channel))
async def setCap(bot, message):
    print(f"set_cap command received in chat: {message.chat.id}")
    
    try:
        # Handle private messages (DMs)
        if message.chat.type == "private":
            # In DMs, any user can use this command
            pass
        
        # Handle channel messages
        elif message.chat.type == "channel":
            # If it's a channel message, allow it (channel owner can use commands)
            if not message.from_user:
                # This is a channel posting - allow it
                pass
            else:
                # This is a user in channel - check if they're admin
                try:
                    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
                    if member.status not in ["administrator", "creator"]:
                        return await message.reply("❌ You must be an admin to use this command in channels!")
                except:
                    pass
        
        # Handle group messages
        elif message.chat.type in ["group", "supergroup"]:
            if not message.from_user:
                return await message.reply("❌ This command can only be used by users!")
        
        # Check if replying to a message with multiline caption
        if message.reply_to_message and message.reply_to_message.text:
            caption = message.reply_to_message.text
        else:
            # Check if caption is provided
            if len(message.command) < 2:
                return await message.reply(
                    "**Usage:** `/set_cap Your caption here`\n\n**Available Variables:**\n"
                    "`{file_name}` - Original File Name\n"
                    "`{file_size}` - File Size\n"
                    "`{language}` - Language of File\n"
                    "`{year}` - Year from File\n"
                    "`{default_caption}` - Original Caption\n\n"
                    "**📝 Multiple Line Support:**\n"
                    "• Type multiple lines directly\n"
                    "• Use `\\n` for line breaks\n"
                    "• Reply to a message with `/set_cap`\n\n"
                    "**Example:**\n"
                    "```\n/set_cap {file_name}\n\n⚙️ Size » {file_size}\n\nJoin Channel 1\nJoin Channel 2\n\n╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗\n💥 𝙅𝙊𝙄𝙉 :- @YourChannel\n╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝```"
                )
            
            # Extract caption from the FULL message text, not just after the command
            full_text = message.text
            if "\n" in full_text:
                # If there are actual line breaks, use them
                parts = full_text.split("\n", 1)
                if len(parts) > 1:
                    caption = parts[1]  # Everything after the first line
                else:
                    caption = full_text.split("/set_cap", 1)[1].strip()
            else:
                # Single line - extract after command
                caption = full_text.split("/set_cap", 1)[1].strip()
        
        if not caption:
            return await message.reply("❌ Please provide a caption!")
        
        # Convert \n to actual line breaks (for cases where user types \n literally)
        caption = caption.replace("\\n", "\n")
        
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

# UPDATED: del_cap command - Works in DMs, Groups, and Channels
@Client.on_message(filters.command("del_cap") & (filters.private | filters.group | filters.channel))
async def delCap(bot, message):
    print(f"del_cap command received in chat: {message.chat.id}")
    
    try:
        # Handle private messages (DMs)
        if message.chat.type == "private":
            # In DMs, any user can use this command
            pass
        
        # Handle channel messages
        elif message.chat.type == "channel":
            # If it's a channel message, allow it (channel owner can use commands)
            if not message.from_user:
                # This is a channel posting - allow it
                pass
            else:
                # This is a user in channel - check if they're admin
                try:
                    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
                    if member.status not in ["administrator", "creator"]:
                        return await message.reply("❌ You must be an admin to use this command in channels!")
                except:
                    pass
        
        # Handle group messages
        elif message.chat.type in ["group", "supergroup"]:
            if not message.from_user:
                return await message.reply("❌ This command can only be used by users!")
        
        chat_id = message.chat.id
        result = await chnl_ids.delete_one({"chnl_id": chat_id})
        
        if result.deleted_count > 0:
            await message.reply("✅ **Caption Deleted Successfully!**\n\nNow I will use my default caption.")
        else:
            await message.reply("❌ No custom caption found for this chat!")
            
    except Exception as e:
        print(f"Error in del_cap: {e}")
        await message.reply(f"❌ Error deleting caption: {str(e)}")

# UPDATED: remove_word command - Works in DMs, Groups, and Channels
@Client.on_message(filters.command("remove_word") & (filters.private | filters.group | filters.channel))
async def remove_word_command(bot, message):
    print(f"remove_word command received in chat: {message.chat.id}")
    
    try:
        # Handle private messages (DMs)
        if message.chat.type == "private":
            # In DMs, any user can use this command
            pass
        
        # Handle channel messages
        elif message.chat.type == "channel":
            # If it's a channel message, allow it (channel owner can use commands)
            if not message.from_user:
                # This is a channel posting - allow it
                pass
            else:
                # This is a user in channel - check if they're admin
                try:
                    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
                    if member.status not in ["administrator", "creator"]:
                        return await message.reply("❌ You must be an admin to use this command in channels!")
                except:
                    pass
        
        # Handle group messages
        elif message.chat.type in ["group", "supergroup"]:
            if not message.from_user:
                return await message.reply("❌ This command can only be used by users!")
        
        # Use chat_id as user identifier for channels, user_id for users
        user_identifier = message.from_user.id if message.from_user else message.chat.id
        
        # Set waiting status for this user and chat
        waiting_for_words[f"{user_identifier}_{message.chat.id}"] = message.chat.id
        
        await message.reply(
            "📝 **Send words separated by space to delete them from caption/filename...**\n\n"
            "*(Send /cancel to cancel this operation)*"
        )
        
    except Exception as e:
        print(f"Error in remove_word: {e}")
        await message.reply(f"❌ Error: {str(e)}")

# UPDATED: Handle word input for remove_word command - Works in DMs, Groups, and Channels
@Client.on_message(filters.text & (filters.private | filters.group | filters.channel))
async def handle_word_input(bot, message):
    # Use chat_id as user identifier for channels, user_id for users
    user_identifier = message.from_user.id if message.from_user else message.chat.id
    user_chat_key = f"{user_identifier}_{message.chat.id}"
    
    # Check if user is waiting for word input
    if user_chat_key in waiting_for_words:
        if message.text.lower() == "/cancel":
            del waiting_for_words[user_chat_key]
            await message.reply("❌ **Operation cancelled!**")
            return
        
        # Don't process commands while waiting for words
        if message.text.startswith("/"):
            return
        
        try:
            # Get words from user input
            words_to_delete = message.text.split()
            chat_id = waiting_for_words[user_chat_key]
            
            # Add words to delete list
            await add_delete_words(chat_id, words_to_delete)
            
            # Remove waiting status
            del waiting_for_words[user_chat_key]
            
            # Show success message
            words_text = ", ".join(words_to_delete)
            await message.reply(f"✅ **Words added to delete list:** {words_text}")
            
        except Exception as e:
            print(f"Error processing words: {e}")
            await message.reply(f"❌ Error processing words: {str(e)}")
            if user_chat_key in waiting_for_words:
                del waiting_for_words[user_chat_key]

# UPDATED: Show current delete words list - Works in DMs, Groups, and Channels
@Client.on_message(filters.command("show_delete_words") & (filters.private | filters.group | filters.channel))
async def show_delete_words(bot, message):
    try:
        # Handle private messages (DMs)
        if message.chat.type == "private":
            # In DMs, any user can use this command
            pass
        
        # Handle channel messages
        elif message.chat.type == "channel":
            # If it's a channel message, allow it (channel owner can use commands)
            if not message.from_user:
                # This is a channel posting - allow it
                pass
            else:
                # This is a user in channel - check if they're admin
                try:
                    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
                    if member.status not in ["administrator", "creator"]:
                        return await message.reply("❌ You must be an admin to use this command in channels!")
                except:
                    pass
        
        # Handle group messages
        elif message.chat.type in ["group", "supergroup"]:
            if not message.from_user:
                return await message.reply("❌ This command can only be used by users!")
        
        words_list = await get_delete_words(message.chat.id)
        
        if words_list:
            words_text = ", ".join(words_list)
            await message.reply(f"📝 **Current delete words list:**\n\n{words_text}")
        else:
            await message.reply("📝 **No words in delete list.**")
            
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

# UPDATED: Clear delete words list - Works in DMs, Groups, and Channels
@Client.on_message(filters.command("clear_delete_words") & (filters.private | filters.group | filters.channel))
async def clear_delete_words_command(bot, message):
    try:
        # Handle private messages (DMs)
        if message.chat.type == "private":
            # In DMs, any user can use this command
            pass
        
        # Handle channel messages
        elif message.chat.type == "channel":
            # If it's a channel message, allow it (channel owner can use commands)
            if not message.from_user:
                # This is a channel posting - allow it
                pass
            else:
                # This is a user in channel - check if they're admin
                try:
                    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
                    if member.status not in ["administrator", "creator"]:
                        return await message.reply("❌ You must be an admin to use this command in channels!")
                except:
                    pass
        
        # Handle group messages
        elif message.chat.type in ["group", "supergroup"]:
            if not message.from_user:
                return await message.reply("❌ This command can only be used by users!")
        
        await clear_delete_words(message.chat.id)
        await message.reply("✅ **Delete words list cleared successfully!**")
        
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

def remove_unwanted_words(text, words_to_remove):
    """Remove unwanted words from text"""
    if not text or not words_to_remove:
        return text
    
    # Create a pattern to match any of the words (case insensitive)
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    
    # Remove the words
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    # Clean up extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

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

# UPDATED: Auto-caption for media - Works in DMs, Groups, and Channels
@Client.on_message((filters.private | filters.group | filters.channel) & filters.media & ~filters.command(["set_cap", "del_cap", "remove_word", "show_delete_words", "clear_delete_words"]))
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
    
    # Get delete words list and remove unwanted words from filename and caption
    delete_words_list = await get_delete_words(chnl_id)
    if delete_words_list:
        file_name = remove_unwanted_words(file_name, delete_words_list)
        default_caption = remove_unwanted_words(default_caption, delete_words_list)
    
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
            
            # Remove unwanted words from final caption
            if delete_words_list:
                replaced_caption = remove_unwanted_words(replaced_caption, delete_words_list)
            
            # Only edit if caption is different
            if replaced_caption != message.caption:
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
    # Get bot info to access username
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    
    await query.message.edit_text(
        text=script.START_TXT.format(query.from_user.mention),  
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"https://t.me/{bot_username}?startchannel=true")
                ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
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
