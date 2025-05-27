import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid
import requests

API_ID = 27246910
API_HASH = "2220cdeac98f15c69fabe30b364de4e2" 
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("my_cinema_pro", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

ALLOWED_GROUPS = ["new_release_movies_202", "amovies2024"]
CHANNELS = ["mycinema225", "goldminesmovies23"]
SHORTNER_API = "69888fba01d81429d92880e72753b1a67e4c0274"

WELCOME_MESSAGE = welcome_text = "Welcome to MY CINEMA PRO bot where you can search movies and get direct links privately."

note_text = "Please don't forget to start me first!"
welcome_text = "Welcome to MY CINEMA PRO bot where you can search movies and get direct links privately."
Your personal movie assistant is here!  
 welcome_text = "Search your favorite movies in the group, and I'll instantly deliver them to your private chat - safely and directly!"
note_text = "Please don't forget to start me first!"

For any help, contact admin: @Dm_Anonymous  
Enjoy your show!


def shorten_link(original_url):
    try:
        r = requests.get(f"https://krownlinks.com/api?api={SHORTNER_API}&url={original_url}")
        return r.json().get("shortenedUrl") or original_url
    except:
        return original_url

@app.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    await message.reply(WELCOME_MESSAGE)

@app.on_message(filters.text & filters.group)
async def search_movie(_, message: Message):
    if str(message.chat.username) not in ALLOWED_GROUPS:
        return

    query = message.text.lower()
    found = False
    for channel in CHANNELS:
        try:
            async for msg in app.search_messages(channel, query, limit=1):
                if msg and msg.media:
                    original_link = f"https://t.me/{channel}/{msg.id}"
                    short_link = shorten_link(original_link)
                    try:
                        await message.from_user.send(f"**Movie Found:**" {query.title()}

await message.from_user.send(
    f"**Movie Found:** {query.title()}\n\n🔗 [Click Here]({short_link}) to download/view.",
    disable_web_page_preview=True
)
                        found = True
                    except PeerIdInvalid:
                        await message.reply("Please start the bot first by clicking the link below.")
                        await message.reply(f"[Start Bot](https://t.me/{(await app.get_me()).username})", disable_web_page_preview=True)
                    break
        except Exception as e:
            print(e)
    if not found:
        await message.reply("Sorry, movie not found in our database.")

app.run()
