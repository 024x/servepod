from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
@socketio.on('connect')
def on_connect():
  print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
  print('Client disconnected')

@socketio.on('message')
def on_message(message):
  print('Message received: ' + message)
  # Send a response back to the client
  socketio.emit('response', {'data': 'This is a response'})

if __name__ == '__main__':
  socketio.run(app, allow_unsafe_werkzeug=True)

