import React, { Component } from 'react';
// import Drawer from 'react-drag-drawer';

class Assigment extends Component {
    constructor(props){
        super(props);
        this.state = {

        }
        this.toggle = this.toggle.bind(this);
    }

    toggle = () => {
        let { toggle } = this.state
      
        this.setState({ toggle: !toggle })
      }


    render() {
        const { open } = this.state
        return (
            <div style={{ backgroundColor: 'white', width: '100%' }}>
                <h1>This is Assigment</h1>
                {/* <Drawer
      open={open}
      onRequestClose={this.toggle}
    >
      <div>Hey Im inside a drawer!</div>
    </Drawer> */}

            </div>
        );
    }
}
export default Assigment;