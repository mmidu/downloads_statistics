import React, { Component } from "react"
import mapboxgl from "mapbox-gl"
import { MAPBOX_ACCESS_TOKEN } from "../conf"
import 'mapbox-gl/dist/mapbox-gl.css'

mapboxgl.accessToken = MAPBOX_ACCESS_TOKEN

class Map extends Component {
	constructor(props) {
		super(props)
		this.state = {
			map: null,
			zoom: 1
		}
		const self = this
		props.websocket.onmessage = async (evt) => {
			const data = JSON.parse(evt.data).msg
			const poi = data.download
			new mapboxgl.Marker()
					.setLngLat(poi.coordinates)
					.setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    				.setHTML('<h3>' + poi.country + '</h3><p>' + new Date(poi.downloaded_at) + '<br>' + poi.app_id + '</p>'))
					.addTo(this.state.map)
			
			self.props.setDataPoints('country', data.country)
			self.props.setDataPoints('appId', data.appId)
			self.props.setDataPoints('timeOfDay', data.timeOfDay)
		}
	}

	componentDidMount = async () => {
		this.setState({
			map: new mapboxgl.Map({
				container: this.mapContainer,
				style: 'mapbox://styles/mapbox/light-v10',
				center: [9.191383, 45.464211],
				zoom: this.state.zoom,
				attributionControl: false
			})
		})

		try {
			const response = await fetch("http://localhost:8081/downloads")
			const data = await response.json()

			this.props.setDataPoints('country', data.countries)
			this.props.setDataPoints('appId', data.appIds)
			this.props.setDataPoints('timeOfDay', data.timesOfDay)

			const self = this

			await data.downloads.map( async (poi) => {
				new mapboxgl.Marker()
					.setLngLat(poi.coordinates)
					.setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    				.setHTML('<h3>' + poi.country + '</h3><p>' + new Date(poi.downloaded_at) + '<br>' + poi.app_id + '</p>'))
					.addTo(self.state.map)
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