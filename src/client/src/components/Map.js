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

		var countries = {

		}
		
		this.props.setDataPoints('timeOfDay', [
			{ label: "Morning",  y: 10  },
			{ label: "Afternoon", y: 15  },
			{ label: "Night", y: 25  },
		])
		this.props.setDataPoints('type', [
			{ label: "Apple",  y: 10  },
			{ label: "Orange", y: 15  },	
		])
		try {
			const response = await fetch("http://localhost:8081/downloads")
			const data = await response.json()

			this.props.setDataPoints('country', data.countries)
			this.props.setDataPoints('appId', data.appIds)
			this.props.setDataPoints('timeOfDay', data.timesOfDay)

			await data.downloads.map( async (poi) => {
				new mapboxgl.Marker()
					.setLngLat(poi.coordinates)
					.setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    				.setHTML('<h3>' + poi.country + '</h3><p>' + new Date(poi.downloaded_at) + '<br>' + poi.app_id + '</p>'))
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