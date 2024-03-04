
# import schemas, models
from database import client, gemini_chat
from datetime import datetime
import asyncio



async def get_all_chats(username):
    result = gemini_chat.find({"username":  username}).sort("time", 1)
    # async for chat in result:
    #     print(chat)
    return result

async def store_chat(username, prompt, response):
    async with await client.start_session() as s:
        async with s.start_transaction():
            chat = {
                "username":  username,
                "prompt": prompt,
                "response": response,
                "time": datetime.now()
            }
            try:
                await gemini_chat.insert_one(chat, session=s)
            except Exception as e:
                print(e)

# asyncio.run(store_chat('khanhtt'))