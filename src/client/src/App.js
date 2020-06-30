import React from 'react'
import Dashboard from './views/Dashboard'
import AddConnection from './views/AddConnection'

function App() {
  const ws = new WebSocket('ws://localhost:8081/ws')
  ws.onopen = () => {
    console.log('connected')
  }

  ws.onmessage = function(event) {
    console.log(event)
  };

  ws.onclose = () => {
    console.log('disconnected')
  }

  return (
    <div className="App">
        <Dashboard websocket={ws}/>
        <AddConnection websocket={ws}/>
    </div>
  );
}

export default App;
