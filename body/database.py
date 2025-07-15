import motor.motor_asyncio
from info import *

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
db = client.captions_with_chnl
chnl_ids = db.chnl_ids
users = db.users
delete_words = db.delete_words  # New collection for delete words

async def addCap(chnl_id, caption):
    dets = {"chnl_id": chnl_id, "caption": caption}
    await chnl_ids.insert_one(dets)

async def updateCap(chnl_id, caption):
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"caption": caption}})

async def insert(user_id):
    user_det = {"_id": user_id}
    try:
        await users.insert_one(user_det)
    except:
        pass
        
async def total_user():
    user = await users.count_documents({})
    return user

async def getid():
    all_users = users.find({})
    return all_users

async def delete(id):
    await users.delete_one(id)

# New functions for delete words
async def add_delete_words(chnl_id, words_list):
    """Add words to delete list for a channel"""
    dets = {"chnl_id": chnl_id, "delete_words": words_list}
    existing = await delete_words.find_one({"chnl_id": chnl_id})
    if existing:
        # Update existing words list
        current_words = existing.get("delete_words", [])
        updated_words = list(set(current_words + words_list))  # Remove duplicates
        await delete_words.update_one({"chnl_id": chnl_id}, {"$set": {"delete_words": updated_words}})
    else:
        # Create new entry
        await delete_words.insert_one(dets)

async def get_delete_words(chnl_id):
    """Get delete words list for a channel"""
    result = await delete_words.find_one({"chnl_id": chnl_id})
    return result.get("delete_words", []) if result else []

async def clear_delete_words(chnl_id):
    """Clear all delete words for a channel"""
    await delete_words.delete_one({"chnl_id": chnl_id})
