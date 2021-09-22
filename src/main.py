import websockets
import asyncio
import json

CLIENTS = {}


def users_event():
    return json.dumps(CLIENTS)


async def client_handler(websocket, path):
    try:
        CLIENTS[str(websocket.id)] = {"x": 0, "y": 0}
        await websocket.send(users_event())
    finally:
        del CLIENTS[str(websocket.id)]
        websockets.broadcast(CLIENTS.items(), users_event())


async def main():
    async with websockets.serve(client_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
