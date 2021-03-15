import React, { Component, Fragment } from 'react'
import ReactDOM from 'react-dom'

import Header from './layout/Header'
import Dashboard from './heroes/Dashboard'
class App extends Component {
    render() {
        return(
            <Fragment>
                <div>
                    <Header/>
                    <div className="container">
                    <Dashboard/>
                    </div>
                </div>
            </Fragment>
        )
        
    }
}
ReactDOM.render( <App/> , document.getElementById('app'))