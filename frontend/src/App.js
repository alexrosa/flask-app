import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import {Link} from 'react-router-dom';


//auxiliary functions
const serviceURL = 'http://localhost:5000/';
const snapshotToArray = snapshot => Object.entries(snapshot).map(
        e => Object.assign(e[1], { key: e[0] })
);


class App extends Component {
  constructor(props){
        super(props)
        this.state = {
            locations: []
        }
    }

    componentWillMount(){
        axios.get(serviceURL).then(response =>
            this.setState({
                locations: snapshotToArray(response.data),
            })
        ).catch(error => {

           console.log(error.message);
        });
    }

    render(){
        return(
            <div className="row">
                <div className="col s12">
                    <ul className="collection with-header">
                        <li className="collection-header"><h4><a href="">Locations</a></h4></li>
                    </ul>
                    <table className="highlight">
                        <thead>
                            <tr>
                                <td>Address</td>
                                <td>City</td>
                                <td>Country</td>
                                <td>...</td>
                            </tr>
                        </thead>
                        <tbody>
							{
							    this.state.locations.map(item =>(
							        <tr key={item.id}>
                                        <td>
                                            {item.address}
                                        </td>
                                        <td>{item.city}</td>
                                        <td>{item.country}</td>
                                        <td>
                                            <Link to={`/${item.id}`} className="waves-effect waves-light btn">Shifts</Link>
                                        </td>
                                    </tr>
							))
							}
						</tbody>
                    </table>
                </div>
            </div>
        );
    }
}

export default App;
