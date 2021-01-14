import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Popup from "reactjs-popup";

import axios from 'axios';
import ReactTable from "react-table";
import columns from './columns';
import { Card, CardHeader, CardBody, Row, Col, InputGroup, InputGroupAddon, InputGroupText, Input, Spinner } from "reactstrap";
import { Spin, Icon } from 'antd';
// import { Form, FormGroup, Label, Input, Button} from "react-bootstrap";
// import { PulseLoader } from 'react-loaders-spinners';

import "react-table/react-table.css";
import './Table.css';
import './Model.css';

var instancePool = [];

const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;


class Instances extends Component {
    constructor(props) {
        super(props);
        this.state = {
            val: false,
            sname: null,
            sid: null,
            sip: null,
            ssize: null,
            sstatus: null,
            slctn: null,
            steam: null,
            senv: null
        }

        this.popUpModel = this.popUpModel.bind(this);
        this.getAllInstances = this.getAllInstances.bind(this);
        this.popDownModel = this.popDownModel.bind(this);
        // this.handleChange = this.handleChange.bind(this);
        // this.checkEnter = this.checkEnter.bind(this);
        // this.spinner = this.spinner.bind(this);
        this.loadTable = this.loadTable.bind(this);
        // this.test = this.test.bind(this);
        // this.openPopup = this.openPopup.bind(this);
        // this.closePopup = this.closePopup.bind(this);
        // this.toggle = this.toggle.bind(this);
    }
    componentWillMount() {
        this.getAllInstances();
    }

    getAllInstances() {
        axios.get('getall').then((data) => {
            console.log(data)
            instancePool = data.data;
            this.loadTable();
        }).catch((err) => {
            console.log(err)
        });
    }

    popUpModel(rowdata) {
        console.log(rowdata.status['Name'])
        this.setState({
            val: true,
            sname: rowdata.t_name,
            sid: rowdata.InstanceID,
            sip: rowdata.instance_ip,
            ssize: rowdata.instype,
            sstatus: rowdata.status['Name'],
            slctn: rowdata.avzone.AvailabilityZone,
            steam: rowdata.t_Team,
            senv: rowdata.t_environment
        });
    }

    popDownModel() {
        this.setState({
            val: false
        });
    }

    loadTable() {
        var array = [];

        array.push(<div style={{ height: "90vh" }}><ReactTable
            columns={columns}
            data={instancePool}
            filterable
            defaultPageSize={50}
            noDataText={"No Data Found."}

            getTdProps={(state, rowInfo, column, instance) => {
                return {
                    onClick: (e, handleOriginal) => {
                        console.log("It was in this row:", rowInfo.original);
                        this.popUpModel(rowInfo.original);
                        if (handleOriginal) {
                            handleOriginal();
                        }
                    }
                };
            }}



            style={{
                height: "90vh"
            }}
            className="-striped -highlight"
        >
            {}
            {(state, makeTable, instance) => {
                let recordsInfoText = "";

                const { filtered, pageRows, pageSize, sortedData, page } = state;

                if (sortedData && sortedData.length > 0) {
                    let isFiltered = filtered.length > 0;

                    let totalRecords = sortedData.length;

                    let recordsCountFrom = page * pageSize + 1;

                    let recordsCountTo = recordsCountFrom + pageRows.length - 1;

                    if (isFiltered)
                        recordsInfoText = `${recordsCountFrom}-${recordsCountTo} of ${totalRecords} filtered records`;
                    else
                        recordsInfoText = `${recordsCountFrom}-${recordsCountTo} of ${totalRecords} records`;
                } else recordsInfoText = "No records";

                return (
                    <div className="main-grid">
                        <div className="above-table text-right">
                            <div className="col-sm-12">
                                <span className="records-info">{recordsInfoText}</span>
                            </div>
                        </div>
                        {}

                        {makeTable()}
                    </div>
                );
            }}



        </ReactTable></div>)

        ReactDOM.render(array, document.getElementById('sp'));

    }

    render() {
        return (
            <div style={{ width: '100%', diplay: "flex", maxHeight: "90vh" }}>



                <Row>
                    <Col>
                        <Card>
                            <CardBody>
                                <div id="sp">
                              
                               <Spin indicator={antIcon} style={{paddingTop:"40vh"}}/>
                                    </div>
                                <Popup open={this.state.val == true} closeOnDocumentClick={false} >

                                    <div>
                                        <Card>
                                            <table >
                                                <tr>
                                                    <td ><strong>Name </strong></td><td>{this.state.sname}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>Instance ID</strong></td><td>{this.state.sid}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>IP Address</strong></td><td>{this.state.sip}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>Size</strong></td><td>{this.state.ssize}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>Location</strong></td><td>{this.state.slctn}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>Team</strong></td><td>{this.state.steam}</td>
                                                </tr>
                                                <tr>
                                                    <td><strong>Environment</strong></td><td>{this.state.senv}</td>
                                                </tr>
                                            </table>

                                        </Card>

                                        <button
                                            className="button"
                                            onClick={() => {
                                                this.popDownModel();

                                            }}
                                        >
                                            Close
                          </button>
                                    </div>



                                </Popup>
                            </CardBody>
                        </Card>
                    </Col>
                </Row>

            </div>
        );
    }
}
export default Instances;