import asyncio
from websockets import serve
import os
async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "0.0.0.0", os.getenv('PORT')):
        await asyncio.Future()  # run forever

asyncio.run(main())