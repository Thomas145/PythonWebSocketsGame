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

url = 'ws://localhost:8765'


class TestClient:

    @staticmethod
    async def test_handshake(uri):

        async with websockets.connect(uri) as websocket:

            message = await websocket.recv()
            print("1#" + message)

            websocket.close()

    @staticmethod
    async def test_new_game(uri):

        async with websockets.connect(uri) as websocket:

            message = await websocket.recv()
            print("1#" + message)

            new_game_request = NewGameRequest()
            new_game_request.number_of_players = 2
            new_game_request.size_of_game = 3

            await websocket.send(json.dumps(new_game_request.__dict__))

            message = await websocket.recv()
            print("2#" + message)

            message = await websocket.recv()
            print("3#" + message)

            websocket.close()


functions_list = [o for o in getmembers(TestClient()) if isfunction(o[1])]

print('STARTED')
for f in functions_list:
    print('---------------------------')
    print(f[0])
    asyncio.get_event_loop().run_until_complete(f[1](url))

print('---------------------------')
print('ENDED')
