#!/usr/bin/env python

# WS server example that synchronizes state across clients

import sys
import traceback
import asyncio
import logging
import websockets


from PythonWebSocketsGame.Application.Server.RequestManager import RequestManager

logging.basicConfig()

request_manager = RequestManager()
STATE = {'value': 0}


async def register(websocket):
    print("Server:  register")
    await request_manager.add_to_connection_pool(websocket)


async def unregister(websocket):
    print("Server: unregister")
    await request_manager.remove_from_connection_pool(websocket)


async def counter(websocket, path):
    print("Starting")

    # register(websocket) sends user_event() to websocket
    await register(websocket)

    print("Server: Connection received" + path)

    try:

        await request_manager.push_server_state_to_all_connections()

        async for message in websocket:
            await request_manager.on_message(message, websocket)

    except Exception:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(counter, 'localhost', 8765))
asyncio.get_event_loop().run_forever()