import React, { Component } from 'react';
import Header from './Components/common/Header/Header';
import Sider from './Components/common/menu/Sider';
import Home from './Components/Home/Home';
import { Affix } from 'antd';
// import Mycours from './Components/Mycours/Mycours';
// import Assigment from './Components/Assigment/Assigment';
// import Allcourses from './Components/All courses/Allcourses';
// import Blog from './Components/blog/Blog';
import Instances from './Components/Instances/Instances';
import { Route, Router, Switch } from 'react-router-dom';
import { Card, CardHeader, CardBody, Row, Col, InputGroup, InputGroupAddon, InputGroupText, Input, Spinner } from "reactstrap";

import './App.css';
import 'antd/dist/antd.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        {/* <Header style={{position:"fixed"}}/> */}
        <Affix><Header style={{ position: 'fixed', zIndex: 1, width: '100%' }} /></Affix>
        <div style={{ display: 'flex' }}>
          <Sider />
          {/* <Switch>
            <Route exact path='/home' component={Home} />
            <Route exact path='/mycours' component={Mycours} />
            <Route exact path='/Assigment' component={Assigment} />
            <Route exact path='/Allcourses' component={Allcourses} />
            <Route exact path='/Blog' component={Blog} />
              <Route exact path='/instances' component={Instances} />
          </Switch> */}
        </div>


      </div>
    );
  }
}

export default App;
