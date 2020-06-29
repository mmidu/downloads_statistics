import React, { Component } from "react"
import CanvasJSReact from '../assets/canvasjs.react';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class Chart extends Component {	
    constructor(props){
        super(props)
    }
    render() {
      const options = {
        title: {
          text: this.props.title
        },
        data: [{				
                  type: "column",
                  dataPoints: this.props.dataPoints
         }]
     }
          
     return (
        <div className={this.props.className}>
          <CanvasJSChart options = {options} />
        </div>
      );
    }
  }

  export default Chart