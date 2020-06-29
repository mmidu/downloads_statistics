import React, { Component } from "react"
import Map from "../components/Map"
import Chart from "../components/Charts"

class Dashboard extends Component {
	constructor(props){
		super(props)
		this.state = {
			country: [],
			timeOfDay: [],
			appId: []
		}
	}
	setDataPoints = (family, dataPoints) => {
		this.setState({
			[family]: dataPoints
		})
	}
	render(){
		return(
			<div>
				<Map setDataPoints={this.setDataPoints}/>
				<div>
					<Chart className="chart3" title="Downloads by country" dataPoints={this.state.country}/>
					<Chart className="chart3" title="Dowloads by time of day" dataPoints={this.state.timeOfDay}/>
					<Chart className="chart3" title="Downloads by app id" dataPoints={this.state.appId}/>
				</div>
			</div>
		)
	}
}

export default Dashboard;