import asyncio
import websockets
import json

from PythonWebSocketsGame.Application.Requests.Models.NewGameRequest import NewGameRequest
from PythonWebSocketsGame.Application.Requests.Models.JoinGameRequest import JoinGameRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitLobbyRequest import ExitLobbyRequest
from PythonWebSocketsGame.Application.Requests.Models.ExitGameRequest import ExitGameRequest
from PythonWebSocketsGame.Application.Requests.Models.SelectAreaRequest import SelectAreaRequest


async def connection(uri):

    async with websockets.connect(uri) as websocket:

        message = await websocket.recv()
        print("1#" + message)

        join_game_request = JoinGameRequest()
        await websocket.send(json.dumps(join_game_request.__dict__))

        message = await websocket.recv()
        print("2#" + message)

        message = await websocket.recv()
        print("3#" + message)


asyncio.get_event_loop().run_until_complete(connection('ws://localhost:8765'))
