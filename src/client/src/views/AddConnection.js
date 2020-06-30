import React, { Component } from "react"

class AddConnection extends Component {
	constructor(props){
        super(props)
        this.sendMessage = this.sendMessage.bind(this)
    }
    

    sendMessage = () => {
        this.props.websocket.send("ping")
    }

    render = () => {
        return(
            <button onClick={this.sendMessage}>Create new point</button>
        )
    }
}

export default AddConnection