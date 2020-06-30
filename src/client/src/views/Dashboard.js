import React, { Component } from "react"
import Map from "../components/Map"
import Chart from "../components/Charts"

class Dashboard extends Component {
	constructor(props){
		super(props)
		this.state = {
			country: {},
			timeOfDay: {},
			appId: {},
			upload: 0
		}
	}
	setDataPoints = (family, dataPoints) => {
		if(typeof dataPoints === 'string' || dataPoints instanceof String){
			if(dataPoints in this.state[family]){
				this.state[family][dataPoints] += 1
			} else {
				this.state[family][dataPoints] = 1
			}
		} else {
			this.state[family] = dataPoints
		}
		this.setState({
			upload: this.state.upload ++
		})
	}

	formatDataPoints = (collection) => {
		let list = []
		for(let elem in collection){
			list.push({"label": elem, "y": collection[elem]})
		}
		return list
	}
	
	render(){
		return(
			<div>
				<Map setDataPoints={this.setDataPoints} websocket={this.props.websocket}/>
				<div>
					<Chart className="chart3" title="Downloads by country" dataPoints={this.formatDataPoints(this.state.country)}/>
					<Chart className="chart3" title="Downloads by time of day" dataPoints={this.formatDataPoints(this.state.timeOfDay)}/>
					<Chart className="chart3" title="Downloads by app id" dataPoints={this.formatDataPoints(this.state.appId)}/>
				</div>
			</div>
		)
	}
}

export default Dashboard;