import uuid
import datetime


class WebSocketClient:

    def __init__(self, connection):
        self.id = uuid.uuid4()
        self.player_name = None
        self.connection_time = datetime.datetime.now()
        self.connection = connection
        self.game = None

    def in_game(self):
        return self.game is not None

    def get_id_string(self):
        return str(self.id)

    def get_client_name(self):
        if self.player_name is None:
            return 'Anon'
        else:
            return self.player_name
