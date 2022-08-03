import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        print( self.scope["user"])
        self.user_room_name = "room_" + str(self.user['user_id'])
        print(self.user_room_name)
        await self.channel_layer.group_add(self.user_room_name, self.channel_name)
        print(f"Added chat {self.channel_name}")

    async def disconnect(self, event):
        self.user = self.scope["user"]
        self.user_room_name = "room_" + str(self.user['user_id'])
        print(self.user_room_name)
        await self.channel_layer.group_discard(self.user_room_name, self.channel_name)
        print(f"Removed chat {self.channel_name}")

    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        await self.send(text_data="User name connect send sms" + self.scope["user"]["username"])
        # Or, to send a binary frame:
        # Want to force-close the connection? Call:
        # await self.close()
        # Or add a custom WebSocket error code!
        # await self.close(code=4123)

    async def new_message(self, event):
        await self.send_json(event)
        print(f"Got messages chat {event} at {self.channel_name}")
