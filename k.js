const WebSocket = require('ws');

const socket = new WebSocket('ws://localhost:5000');
socket.addEventListener('open', (event) => {
  socket.send('Hello Server!');
});

socket.addEventListener('message', (event) => {
  console.log('Message from server: ', event.data);
});
