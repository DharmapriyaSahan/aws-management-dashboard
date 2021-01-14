var columns = [
    {
      Header: "Name",
      accessor: "t_name",
      width: 300,
      maxWidth: 400,
      minWidth: 300,
      headerClassName: 'my-favorites-column-header-group'
    },
    {
      Header: "ID",
      accessor: "InstanceID",
      width: 150,
      maxWidth: 150,
      minWidth: 110
    },
    {
      Header: "IP",
      accessor: "instance_ip"
    },
    {
      Header: "Size",
      accessor: "instype"
    },
    {
      Header: "Status",
      accessor: "status.Name"
    },
    {
      Header: "Location",
      accessor: "avzone.AvailabilityZone"
    },
    {
      Header: "Team",
      accessor: "t_Team",
      style: {
        textAlign: "left"
      }
    },
    {
      Header: "Environment",
      accessor: "t_environment"
    }
    // ,
    // {
    //   Header: "Actions",
    //   filterable: false,
    //   sortable: false,
    //   Cell: props =>{
    //     return(
    //       <Button  size="sm" variant="outline-primary">Stop</Button>
    //     )
  
    //   }
    // }
  ]

  export default columns;