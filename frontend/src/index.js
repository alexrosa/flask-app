import React from 'react';
import ReactDOM from 'react-dom';
import '../node_modules/materialize-css/dist/css/materialize.css'
import '../node_modules/materialize-css/dist/js/materialize.js'
import './index.css';
import App from './App';
import User from './User';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Switch, Route} from 'react-router-dom';

ReactDOM.render(
        <BrowserRouter>
            <div>
                <Switch>
                    <Route exact path="/:id" component={User}/>
                    <App />
                </Switch>
            </div>
        </BrowserRouter>
        ,document.getElementById('root')
);
registerServiceWorker();
