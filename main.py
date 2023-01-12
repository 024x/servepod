from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    socketio.emit('response', message)

@socketio.on('response')
def handle_response(response):
    print('Received response: ' + response)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=os.getenv("PORT"))
