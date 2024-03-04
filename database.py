import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import atexit

uri = "mongodb+srv://philtph19845:rgPiviNjuLxM61il@thephi.s7cokuk.mongodb.net/"

client = AsyncIOMotorClient(uri)
gemini_chat = client.assistants_chat.gemini_chat

async def test_query():
    try:

        # result = await client.admin.command('ping')
        customers_collection = client.sample_analytics.customers
        async for doc in customers_collection.find({'username': 'amandawilliams'}):   
        # print("Pinged your deployment. You successfully connection to MongoDB!")
            print(doc)
    except Exception as e:
        print(e)


# asyncio.run(test_query())








def  close_client(client):
    client.close()
atexit.register(close_client, client)