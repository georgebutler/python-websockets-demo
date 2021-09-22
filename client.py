import websockets
import asyncio
import json

CLIENTS = {}


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        result = await websocket.recv()
        print(result)


asyncio.run(hello())
