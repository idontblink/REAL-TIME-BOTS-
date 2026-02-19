import asyncio
import websockets
import datetime


async def handle_bot(websocket):

    await websocket.send("🤖 Bot is online. Type 'help'.")

    async for message in websocket:

        msg = message.lower().strip()

        if msg == "ping":
            reply = "🏓 Pong!"

        elif msg == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            reply = f"⏰ Time: {now}"

        elif msg == "help":
            reply = """
Commands:
ping  - test bot
time  - show time
help  - show commands
exit  - quit
"""

        elif msg == "exit":
            await websocket.send("Bye 👋")
            break

        else:
            reply = f"You said: {message}"

        await websocket.send(reply)


async def main():

    print("Bot running on ws://localhost:8765")

    async with websockets.serve(handle_bot, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
