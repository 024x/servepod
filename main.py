import asyncio
import websockets

async def echo_server(websocket, path):
  while True:
    message = await websocket.recv()
    await websocket.send(message)
    
    await websocket.send(message)
start_server = websockets.serve(echo_server, '0.0.0.0', 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
