import React from 'react';
import { Layout, Menu, Breadcrumb, Avatar } from 'antd';
import { Link } from 'react-router-dom';
import logo from '../../../Resources/Img/output-onlinepngtools.png';
import style from './style';

import './avatar.css';

const { Header } = Layout;


class HeaderMain extends React.Component {

    render() {

        return (
            <Header>
               {/* <div className="logo" src={logo} style={style.logoImg}/> */}
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={['2']}
                    style={{ lineHeight: '64px' }}
                    selectable={false}
                >
            
                    <Menu.Item style={{float:"left"}} >
                    <img src={logo} style={style.logoImg} /></Menu.Item>
                    {/* <Menu.Item key="1"><Link to='/home' >Home</Link></Menu.Item> */}
                    {/* <Menu.Item key="2"><Link to='/instances' >Instances</Link></Menu.Item> */}
                     <Menu.Item  style={{float:"right"}}><Avatar style={{ backgroundColor: '#87d068' }} icon="user" /></Menu.Item>
                    {/* <Menu.Item key="3"><Link to='/Assigment' >Assigment</Link></Menu.Item> */}
                    {/* <Menu.Item key="4"><Link to='/Allcourses' >Allcourses</Link></Menu.Item> */}
                    {/* <Menu.Item key="5"><Link to='/Blog' >Blog</Link></Menu.Item> */}
                    
                </Menu> 
            </Header>
        );
    }
}
export default HeaderMain