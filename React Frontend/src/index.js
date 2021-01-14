import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { BrowserRouter } from 'react-router-dom';
import Sider from './Components/common/menu/Sider';
import Login from './Components/Login/Login';
import Home from './Components/Home/Home';
// import App from './App';

// const hist = createBrowserHistory();

// function checkLogin() {
//     if (!sessionStorage.getItem("loging_status")) {
//         console.log("lkasd");
//       return (
//            <Route exact path="/" component={Sider}/>
        
//         //    <Route exact path='/home' component={Home} />
        
//       );
//     } else {
//       return (
//         <div>
//           <Redirect to="/login" />
//           <Route path="/login" component={Login} />
//         </div>
//       );
//     }
//   }

//   ReactDOM.render(
//     <BrowserRouter history={hist}>
//       {checkLogin()}
//     </BrowserRouter>,
//     document.getElementById("root")
//   );

ReactDOM.render(<BrowserRouter ><App /></BrowserRouter>, document.getElementById('root'));
serviceWorker.unregister();
