import asyncio
import websockets
import json


async def hello(uri):
    print("Client: making connection")
    async with websockets.connect(uri) as websocket:
        print("Client: Connection Made")
        greeting = await websocket.recv()
        print("Client: " + greeting)


        message = await websocket.recv()
        print("client: message " + message)

asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8765'))