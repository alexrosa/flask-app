import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

//auxiliary functions
const serviceURL = 'http://localhost:5000/';
const snapshotToArray = snapshot => Object.entries(snapshot).map(
        e => Object.assign(e[1], { key: e[0] })
);

class User extends Component {
    constructor(props){
        super(props);
        this.state = {
            location_name: '',
            user_data_list: [],
        };

        this.getUserData = this.getUserData.bind(this);
    }

    getUserData(){
        let url = serviceURL + `users/${this.props.match.params.id}`;
        console.log("url "+url);

        axios.get(url).then(response=>
            this.setState({
                user_data_list: snapshotToArray(response.data),
            })
        ).catch(error => {
            console.log(error.message);
        })
    }
    componentWillMount(){
        this.getUserData();
    }

    render() {
        return (
            <div className="row">
                <div className="row">
		  	        <div className="col s12">
                        <div className="divider"></div>
                        <div className="section-heading">
                            <h4>Employee List</h4>
                        </div>
			        </div>
                </div>
                <div className="row">
                    <table className="highlight">
                        <thead>
                            <tr>
                                <td>First Name</td>
                                <td>Last Name</td>
                                <td>Worked hours</td>
                                <td>Over time hours</td>
                                <td>picture</td>
                            </tr>
                        </thead>
                        <tbody>
                        {
                            this.state.user_data_list.map(item =>(
                                <tr key={item.id}>
                                    <td>{item.firstName}</td>
                                    <td>{item.lastName}</td>
                                    <td>{item.worked_hours}</td>
                                    <td>{item.over_time}</td>
                                    <td><img src={item.photo} alt="Employee Image" className="circle"/></td>
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

export default User;
