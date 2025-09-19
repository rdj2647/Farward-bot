from telethon import TelegramClient, events
import os, asyncio

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
source = os.environ.get("SOURCE")
target = os.environ.get("TARGET")

client = TelegramClient("forward_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source))
async def handler(event):
    try:
        await client.forward_messages(target, event.message)
        print(f"✅ Forwarded: {event.message.id}")
    except Exception as e:
        print("❌ Error:", e)

async def main():
    await client.start()
    print("Bot started on Railway ✅")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
