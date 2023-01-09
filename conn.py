from socketIO_client import SocketIO
import requests as r
print(r.get('ws://localhost:8000'))
socket = SocketIO('http://localhost:8000')
def on_connect():
  print('Connected to server')

def on_disconnect():
  print('Disconnected from server')

def on_response(data):
  print('Response received: ' + data)

socket.connect()
socket.emit('message', 'This is a message from the Python script')
