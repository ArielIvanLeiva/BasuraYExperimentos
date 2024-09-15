from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        # Stores active connections sockets on ram, indexable by player id.
        self.active_connections: dict[int, WebSocket] = {}
        
    async def connect(self, player_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[player_id] = websocket
        
    def disconnect(self, user_id: int):
        self.active_connections.pop(user_id)    
    
    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)
            
            
ws_manager = ConnectionManager()