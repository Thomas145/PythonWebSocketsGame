#!/usr/bin/env python

# WS server example that synchronizes state across clients

import sys
import traceback
import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {'value': 0}

USERS = set()


def state_event():
    _json = json.dumps({'type': 'state', **STATE})
    return _json


def users_event():
    print("Server: users_event")
    return json.dumps({'type': 'users', 'count': len(USERS)})


async def notify_state():
    print("Server: notify_state")
    if USERS:       # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    print("Server: notify_users")
    if USERS:       # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    print("Server:  register")
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    print("Server: unregister")
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    print("Starting")

    # register(websocket) sends user_event() to websocket
    await register(websocket)

    print("Server: Connection received" + path)

    try:

        msg_to_send = state_event()
        print("Sending: state event" + msg_to_send)
        await websocket.send(msg_to_send)
        print("Sent: state event")

        async for message in websocket:

            print("Server: message " + message)

            data = json.loads(message)

            if data['action'] == 'minus':

                STATE['value'] -= 1
                await notify_state()

            elif data['action'] == 'plus':

                STATE['value'] += 1
                await notify_state()

            else:

                logging.error("unsupported event: {}", data)

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