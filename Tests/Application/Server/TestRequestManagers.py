import asyncio
import websockets
import json

from inspect import getmembers, isfunction
from PythonWebSocketsGame.Tests.Application.TheTest import TheTest


from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest
from PythonWebSocketsGame.Application.Requests.Models.JoinGameRequest import JoinGameRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitLobbyRequest import ExitLobbyRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitGameRequest import ExitGameRequest
from PythonWebSocketsGame.Application.Requests.Models.SelectAreaRequest import SelectAreaRequest

import time

url = 'ws://localhost:8765'


async def get_message(websocket):

    try:
        while True:
            message = await asyncio.wait_for(websocket.recv(), timeout=1)
            print(message)
    except Exception:
        print("No more messages")


class TestClient:

    async def test_join_game(self, uri):

        async with websockets.connect(uri) as websocket:

            await get_message(websocket)

            join_game_request = JoinGameRequest()
            await websocket.send(json.dumps(join_game_request.__dict__))

            await get_message(websocket)

            websocket.close()

    @staticmethod
    async def test_handshake(uri):

        async with websockets.connect(uri) as websocket:

            await get_message(websocket)

            websocket.close()

    @staticmethod
    async def test_new_game(uri):

        async with websockets.connect(uri) as websocket:

            await get_message(websocket)

            new_game_request = NewGameRequest()
            new_game_request.number_of_players = 2
            new_game_request.size_of_game = 3

            await websocket.send(json.dumps(new_game_request.__dict__))

            await get_message(websocket)

            await TestClient().test_join_game(uri)

            await get_message(websocket)

            websocket.close()


functions_list = [o for o in getmembers(TestClient()) if isfunction(o[1])]

print('STARTED')

for f in functions_list:
    print('---------------------------')
    print(f[0])
    asyncio.get_event_loop().run_until_complete(f[1](url))

print('---------------------------')
print('ENDED')
