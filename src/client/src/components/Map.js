import React, { Component } from "react"
import mapboxgl from "mapbox-gl"
import { MAPBOX_ACCESS_TOKEN } from "../conf"
import 'mapbox-gl/dist/mapbox-gl.css'

mapboxgl.accessToken = MAPBOX_ACCESS_TOKEN

class Map extends Component {
	constructor(props) {
		super(props)

		this.state = {
			zoom: 1
		}
	}
	componentDidMount = async () => {

		var map = new mapboxgl.Map({
			container: this.mapContainer,
			style: 'mapbox://styles/mapbox/light-v10',
			center: [9.191383, 45.464211],
			zoom: this.state.zoom,
			attributionControl: false
		})

		// var marker = new mapboxgl.Marker()
		// 	.setLngLat([9.191383, 45.464211])
		// 	.addTo(map)

		try {
			const response = await fetch("http://localhost:8081/downloads")
			const data = await response.json()
			data.map((poi) => {
				new mapboxgl.Marker()
					.setLngLat(poi.coordinates)
					.addTo(map)
			})
		} catch(error){
			console.log(error)
		}
		
	}
	render(){
		return (
			<div>
				<div ref={el => this.mapContainer = el} className="mapContainer" />
			</div>
		)	
	}
}

export default Map