import React from 'react';
// import { Menu, Icon, Button } from 'antd';
import { Link } from 'react-router-dom';
import { Layout, Menu, Icon, Breadcrumb, Affix } from 'antd';
import Instances from '../../Instances/Instances';
import Home from '../../Home/Home'
import { Route, Router, Switch } from 'react-router-dom';

import Header from '../Header/Header';

const SubMenu = Menu.SubMenu;

const { Sider, Content, Footer } = Layout;

class SiderBar extends React.Component {
  state = {
    collapsed: false,
  };

  toggleCollapsed = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  }

  render() {
    return (

      <Layout>

        <Sider style={{
          overflow: 'auto', height: '100vh', position: 'fixed', left: 0,
        }}
        >

          <Menu
            // defaultSelectedKeys={['1']}
            // defaultOpenKeys={['sub1']}
            mode="inline"
            theme="dark"
            inlineCollapsed={this.state.collapsed}

          >

            <Menu.Item key="1" style={{ alignItems: "left" }}>
              <Icon type="home" style={{align:"left"}}/>
              <span >Home</span>
              <Link to="/home" />
            </Menu.Item>

            <SubMenu key="sub1" title={<span><Icon type="database" /><span>Instance Management</span></span>}>
              <Menu.Item key="2"><Link to="/instances">Production</Link></Menu.Item>
            </SubMenu>

            <Menu.Item key="3">
              <Icon type="cluster" />
              <span>Load Balancers</span>
            </Menu.Item>

            <Menu.Item key="4">
            <Icon type="deployment-unit" />
              <span>Target Groups</span>
            </Menu.Item>

          </Menu>

        </Sider>

        <Layout style={{ marginLeft: 200 }}>
          
          <Content style={{ margin: '24px 16px 0', overflow: 'initial', minHeight: "90vh" }}>
            <div style={{ padding: 24, background: '#fff', textAlign: 'center', minHeight: "90vh" }}>

              <Switch>
                <Route exact path='/home' component={Home} />
                <Route exact path='/instances' component={Instances} />
              </Switch>

            </div>
          </Content>

          <Footer style={{ textAlign: 'center' }}>
            Pearson plc ©2019 Created by Chandira Jayasekara
        </Footer>

        </Layout>

      </Layout>
    );
  }
}
export default SiderBar;
