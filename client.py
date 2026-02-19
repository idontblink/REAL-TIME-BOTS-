import asyncio
import websockets


async def start_chat():

    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as ws:

        print(await ws.recv())

        while True:

            msg = input("You: ")

            await ws.send(msg)

            reply = await ws.recv()

            print("Bot:", reply)

            if msg == "exit":
                break


asyncio.run(start_chat())
