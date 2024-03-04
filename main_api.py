from fastapi import FastAPI, Query, Body, Depends, Response
from typing import Annotated
from datetime import datetime
from pydantic import Field
from dotenv import load_dotenv
import httpx
from schemas import Prompt
import asyncio
from sqlalchemy.orm import Session
import crud, models, schemas
from bson import ObjectId

app = FastAPI()

username = 'khanhtt'
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent" 
GEMINI_KEY = 'AIzaSyBbpOmWGc2xEsxlksKz9nK17RdS8dumFZY'


async def complete_gemini(conversation, key):
    data = {
        "contents": conversation,
        "generationConfig": {
            "stopSequences": ["Title"],
            "temperature": 1.0,
            "maxOutputTokens": 5000,
            "topP": 0.8,
            "topK": 10,
            # "target_language": "vi"
        }
    }
    params = {'key': key}
    headers = {"Content-Type": "application/json"}

    try:
        async with httpx.AsyncClient(timeout=100) as client:
            result = await client.post(GEMINI_URL, params=params, json=data, headers=headers)
            result.raise_for_status()  # Raise an exception for bad responses (4xx, 5xx)
            # print('--------------------------------------------------------------------')
            # print("result = {}".format(result.json()["candidates"][0]))
            return result.json()["candidates"][0]["content"]["parts"][0]["text"]
    except httpx.HTTPError as e:
        print(f"Error making Gemini API request: {e}")
        raise


@app.get('/')
async def get_all_chats():
    chats = await crud.get_all_chats(username=username)
    chats = await chats.to_list(length=None)
    for chat in chats:
        chat['_id'] = str(chat['_id'])
        print(chat)
    # if chats:
    #     raise HTTPException(status_code=400, detail="Couldn't find any chats")
    return chats


@app.post("/")
async def send_prompt(prompt: schemas.Prompt):
    older_chats = await crud.get_all_chats(username=username)
    conversation = []
    async for older_chat in older_chats:
        conversation.extend([{"role":"user",
         "parts":[{
           "text": older_chat['prompt']}]},
        {"role": "model",
         "parts":[{
           "text": older_chat['response']}]}])
    
    conversation.append({"role":"user",
         "parts":[{
           "text": prompt.prompt}]})
    response = await complete_gemini(conversation=conversation, key=GEMINI_KEY)

    await crud.store_chat(username=username, prompt=prompt.prompt, response=response)
    return Response(status_code=200)
    












# older code
# @app.get("/")
# async def root():
#     await asyncio.sleep(1)
#     return conversation_histories

# @app.post("/send-prompt/")
# async def send_prompt(prompt: Prompt = Body(embed=True), q: Annotated[str | None, Query(alias="item-query", title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3, max_length=100, regex="^Hung$", deprecated=True, include_in_schema=True)] = None):
#     print(q)
#     print(prompt)
#     if prompt is None:
#         return conversation_histories
    
#     answer = await complete_gemini(prompt=prompt.prompt, key=GEMINI_KEY)

#     conversation_histories.append({
#         "user": prompt.prompt,
#         "assistant": answer
#     })

#     return conversation_histories
