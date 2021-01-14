from flask import Flask
from flask import request
import boto3
import json

app = Flask(__name__)

OutInstances = {'instances': ''}
out = []




@app.route("/api/getallec2")
@app.route("/getall")
def getall():
    boto3.setup_default_session(profile_name='non_prod')
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:t_CreatedBy', 'Values': ['ProjectX']}])
    l_instance = []
    instance_keys = ""
    instance_keys2 = ""
    instance_keys3 = ""
    instance_keys4 = ""
    instance_id = ""
    instance_ip = ""
    ins = {}
    finstances = []

    for instance in instances:
        l_instance = []
        instance_keys = ""
        instance_keys2 = ""
        instance_keys3 = ""
        instance_keys4 = ""
        instance_id = ""
        instance_ip = ""
        ins = {}
        instance_id = instance.id
        instance_ip = instance.private_ip_address
        l_instance.append(instance_id)
        l_instance.append(instance_ip)
        for tag in instance.tags:
            if tag["Key"] == 't_name' or tag["Key"] == 'Name':
                instanceName = tag["Value"]
                instance_keys = instanceName
                l_instance.append(instance_keys)
            if tag["Key"] == 't_environment' or tag["Key"] == 't_Environment':
                environment = tag["Value"]
                instance_keys2 = environment
                l_instance.append(instance_keys2)
            if tag["Key"] == 't_Team' or tag["Key"] == 't_team':
                team = tag["Value"]
                instance_keys3 = team
                l_instance.append(instance_keys3)
            if tag["Key"] == 't_role' or tag["Key"] == 't_Role':
                role = tag["Value"]
                instance_keys4 = role
                l_instance.append(instance_keys4)
        ins['InstanceID'] = instance_id
        ins['instance_ip'] = instance_ip
        ins['instype'] = instance.instance_type
        ins['status'] = instance.state
        ins['avzone'] = instance.placement
        ins['t_name'] = instance_keys
        ins['t_environment'] = instance_keys2
        ins['t_Team'] = instance_keys3
        ins['t_role'] = instance_keys4
        ins['account'] = 'non_prod'
        finstances.append(ins)

    boto3.setup_default_session(profile_name='prod')
    ec2_2 = boto3.resource('ec2')
    instances_2 = ec2_2.instances.filter(
        Filters=[{'Name': 'tag:t_CreatedBy', 'Values': ['ProjectX']}])
    for instance in instances_2:
        l_instance = []
        instance_keys = ""
        instance_keys2 = ""
        instance_keys3 = ""
        instance_keys4 = ""
        instance_id = ""
        instance_ip = ""
        ins = {}
        instance_id = instance.id
        instance_ip = instance.private_ip_address
        l_instance.append(instance_id)
        l_instance.append(instance_ip)
        for tag in instance.tags:
            if tag["Key"] == 't_name' or tag["Key"] == 'Name':
                instanceName = tag["Value"]
                instance_keys = instanceName
                l_instance.append(instance_keys)
            if tag["Key"] == 't_environment' or tag["Key"] == 't_Environment':
                environment = tag["Value"]
                instance_keys2 = environment
                l_instance.append(instance_keys2)
            if tag["Key"] == 't_Team' or tag["Key"] == 't_team':
                team = tag["Value"]
                instance_keys3 = team
                l_instance.append(instance_keys3)
            if tag["Key"] == 't_role' or tag["Key"] == 't_Role':
                role = tag["Value"]
                instance_keys4 = role
                l_instance.append(instance_keys4)
        ins['InstanceID'] = instance_id
        ins['instance_ip'] = instance_ip
        ins['instype'] = instance.instance_type
        ins['status'] = instance.state
        ins['avzone'] = instance.placement
        ins['t_name'] = instance_keys
        ins['t_environment'] = instance_keys2
        ins['t_Team'] = instance_keys3
        ins['t_role'] = instance_keys4
        ins['account'] = 'prod'
        finstances.append(ins)

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response


@app.route("/api/getallelb")
@app.route("/getallelb")
def getallelb():
    finstances = []
    ## Serch in non-prod
    boto3.setup_default_session(profile_name='non_prod')

    ## search in elbv2
    elbListv2 = boto3.client('elbv2')

    bals = elbListv2.describe_load_balancers()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['LoadBalancers']:
        ins = {}
        team = ''
        ins['LoadBalancerArn'] = elb['LoadBalancerArn']
        arn = ''
        arn = elb['LoadBalancerArn']
        ins['DNSName'] = elb['DNSName']
        ins['LoadBalancerName'] = elb['LoadBalancerName']
        ins['Type'] = elb['Type']
        ins['AvailabilityZones'] = elb['AvailabilityZones']
        ins['State'] = elb['State']
        ins['VpcId'] = elb['VpcId']
        # tag = elbListv2.describe_tags(ResourceArns=[arn])
        # for tt in tag['TagDescriptions']:
        #     for t_ in tt['Tags']:
        #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
        #             team = t_["Value"]
        # ins['t_team'] = team
        finstances.append(ins)

    while (NextMarker != ''):
        bals = elbListv2.describe_load_balancers(Marker=NextMarker)
        for elb in bals['LoadBalancers']:
            ins = {}
            ins['LoadBalancerArn'] = elb['LoadBalancerArn']
            arn = ''
            team = ''
            arn = elb['LoadBalancerArn']
            ins['DNSName'] = elb['DNSName']
            ins['LoadBalancerName'] = elb['LoadBalancerName']
            ins['Type'] = elb['Type']
            ins['AvailabilityZones'] = elb['AvailabilityZones']
            ins['State'] = elb['State']
            ins['VpcId'] = elb['VpcId']
            # tag = elbListv2.describe_tags(ResourceArns=[arn])
            # for tt in tag['TagDescriptions']:
            #     for t_ in tt['Tags']:
            #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
            #             team = t_["Value"]
            # ins['t_team'] = team
            finstances.append(ins)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

    ## search in elb

    elbList = boto3.client('elb')

    bals = elbList.describe_load_balancers()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['LoadBalancerDescriptions']:
        ins = {}
        team = ''
        ins['LoadBalancerArn'] = ''
        ins['DNSName'] = elb['DNSName']
        ins['LoadBalancerName'] = elb['LoadBalancerName']
        elbname = ''
        elbname = elb['LoadBalancerName']
        ins['Type'] = 'classic'
        ins['AvailabilityZones'] = elb['AvailabilityZones']
        ins['State'] = ''
        ins['VpcId'] = elb['VPCId']
        # tag = elbList.describe_tags(LoadBalancerNames=[elbname])
        # for tt in tag['TagDescriptions']:
        #     for t_ in tt['Tags']:
        #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
        #             team = t_["Value"]
        # ins['t_team'] = team
        finstances.append(ins)

    while (NextMarker != ''):
        bals = elbList.describe_load_balancers(Marker=NextMarker)
        for elb in bals['LoadBalancerDescriptions']:
            ins = {}
            team = ''
            ins['LoadBalancerArn'] = ''
            ins['DNSName'] = elb['DNSName']
            ins['LoadBalancerName'] = elb['LoadBalancerName']
            elbname = ''
            elbname = elb['LoadBalancerName']
            ins['Type'] = 'classic'
            ins['AvailabilityZones'] = elb['AvailabilityZones']
            ins['State'] = ''
            ins['VpcId'] = elb['VPCId']
            # tag = elbList.describe_tags(LoadBalancerNames=[elbname])
            # for tt in tag['TagDescriptions']:
            #     for t_ in tt['Tags']:
            #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
            #             team = t_["Value"]
            # ins['t_team'] = team
            finstances.append(ins)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

            ## Serch in prod
    boto3.setup_default_session(profile_name='prod')

    ## search in elbv2
    elbListv2 = boto3.client('elbv2')

    bals = elbListv2.describe_load_balancers()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['LoadBalancers']:
        ins = {}
        team = ''
        ins['LoadBalancerArn'] = elb['LoadBalancerArn']
        arn = ''
        arn = elb['LoadBalancerArn']
        ins['DNSName'] = elb['DNSName']
        ins['LoadBalancerName'] = elb['LoadBalancerName']
        ins['Type'] = elb['Type']
        ins['AvailabilityZones'] = elb['AvailabilityZones']
        ins['State'] = elb['State']
        ins['VpcId'] = elb['VpcId']
        # tag = elbListv2.describe_tags(ResourceArns=[arn])
        # for tt in tag['TagDescriptions']:
        #     for t_ in tt['Tags']:
        #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
        #             team = t_["Value"]
        # ins['t_team'] = team
        finstances.append(ins)

    while (NextMarker != ''):
        bals = elbListv2.describe_load_balancers(Marker=NextMarker)
        for elb in bals['LoadBalancers']:
            ins = {}
            ins['LoadBalancerArn'] = elb['LoadBalancerArn']
            arn = ''
            team = ''
            arn = elb['LoadBalancerArn']
            ins['DNSName'] = elb['DNSName']
            ins['LoadBalancerName'] = elb['LoadBalancerName']
            ins['Type'] = elb['Type']
            ins['AvailabilityZones'] = elb['AvailabilityZones']
            ins['State'] = elb['State']
            ins['VpcId'] = elb['VpcId']
            # tag = elbListv2.describe_tags(ResourceArns=[arn])
            # for tt in tag['TagDescriptions']:
            #     for t_ in tt['Tags']:
            #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
            #             team = t_["Value"]
            # ins['t_team'] = team
            finstances.append(ins)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

        ## search in elb

    elbList = boto3.client('elb')

    bals = elbList.describe_load_balancers()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['LoadBalancerDescriptions']:
        ins = {}
        team = ''
        ins['LoadBalancerArn'] = ''
        ins['DNSName'] = elb['DNSName']
        ins['LoadBalancerName'] = elb['LoadBalancerName']
        elbname = ''
        elbname = elb['LoadBalancerName']
        ins['Type'] = 'classic'
        ins['AvailabilityZones'] = elb['AvailabilityZones']
        ins['State'] = ''
        ins['VpcId'] = elb['VPCId']
        # tag = elbList.describe_tags(LoadBalancerNames=[elbname])
        # for tt in tag['TagDescriptions']:
        #     for t_ in tt['Tags']:
        #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
        #             team = t_["Value"]
        # ins['t_team'] = team
        finstances.append(ins)

    while (NextMarker != ''):
        bals = elbList.describe_load_balancers(Marker=NextMarker)
        for elb in bals['LoadBalancerDescriptions']:
            ins = {}
            team = ''
            ins['LoadBalancerArn'] = ''
            ins['DNSName'] = elb['DNSName']
            ins['LoadBalancerName'] = elb['LoadBalancerName']
            elbname = ''
            elbname = elb['LoadBalancerName']
            ins['Type'] = 'classic'
            ins['AvailabilityZones'] = elb['AvailabilityZones']
            ins['State'] = ''
            ins['VpcId'] = elb['VPCId']
            # tag = elbList.describe_tags(LoadBalancerNames=[elbname])
            # for tt in tag['TagDescriptions']:
            #     for t_ in tt['Tags']:
            #         if t_["Key"] == 't_Team' or t_["Key"] == 't_team':
            #             team = t_["Value"]
            # ins['t_team'] = team
            finstances.append(ins)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response


@app.route("/api/getalltg")
@app.route("/getalltg")
def getalltg():
    finstances = []
    count = 0
    # Search for non-prod
    boto3.setup_default_session(profile_name='non_prod')
    client = boto3.client('elbv2')

    bals = client.describe_target_groups()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['TargetGroups']:
        count = count + 1
        finstances.append(elb)

    while (NextMarker != ''):
        bals = client.describe_target_groups(Marker=NextMarker)
        for elb in bals['TargetGroups']:
            count = count + 1
            finstances.append(elb)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

    # Search for prod
    boto3.setup_default_session(profile_name='prod')
    client = boto3.client('elbv2')

    bals = client.describe_target_groups()
    try:
        bals['NextMarker']
        NextMarker = bals['NextMarker']
    except:
        NextMarker = ''
    for elb in bals['TargetGroups']:
        count = count + 1
        finstances.append(elb)

    while (NextMarker != ''):
        bals = client.describe_target_groups(Marker=NextMarker)
        for elb in bals['TargetGroups']:
            count = count + 1
            finstances.append(elb)
        try:
            bals['NextMarker']
            NextMarker = bals['NextMarker']
        except:
            NextMarker = ''

    print(count)

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response






@app.route("/getallnonprod")
def getallnonprod():
    boto3.setup_default_session(profile_name='non_prod')
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:t_CreatedBy', 'Values': ['ProjectX']}])
    l_instance = []
    instance_keys = ""
    instance_keys2 = ""
    instance_keys3 = ""
    instance_keys4 = ""
    instance_id = ""
    instance_ip = ""
    ins = {}
    finstances = []

    for instance in instances:
        l_instance = []
        instance_keys = ""
        instance_keys2 = ""
        instance_keys3 = ""
        instance_keys4 = ""
        instance_id = ""
        instance_ip = ""
        ins = {}
        instance_id = instance.id
        instance_ip = instance.private_ip_address
        l_instance.append(instance_id)
        l_instance.append(instance_ip)
        for tag in instance.tags:
            if tag["Key"] == 't_name' or tag["Key"] == 'Name':
                instanceName = tag["Value"]
                instance_keys = instanceName
                l_instance.append(instance_keys)
            if tag["Key"] == 't_environment' or tag["Key"] == 't_Environment':
                environment = tag["Value"]
                instance_keys2 = environment
                l_instance.append(instance_keys2)
            if tag["Key"] == 't_Team' or tag["Key"] == 't_team':
                team = tag["Value"]
                instance_keys3 = team
                l_instance.append(instance_keys3)
            if tag["Key"] == 't_role' or tag["Key"] == 't_Role':
                role = tag["Value"]
                instance_keys4 = role
                l_instance.append(instance_keys4)
        ins['InstanceID'] = instance_id
        ins['instance_ip'] = instance_ip
        ins['instype'] = instance.instance_type
        ins['status'] = instance.state
        ins['avzone'] = instance.placement
        ins['t_name'] = instance_keys
        ins['t_environment'] = instance_keys2
        ins['t_Team'] = instance_keys3
        ins['t_role'] = instance_keys4
        finstances.append(ins)

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response


@app.route("/api/getec2")
def getallprod():
    env = request.args.get('env')
    boto3.setup_default_session(profile_name=env)
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:t_CreatedBy', 'Values': ['ProjectX']}])
    l_instance = []
    instance_keys = ""
    instance_keys2 = ""
    instance_keys3 = ""
    instance_keys4 = ""
    instance_id = ""
    instance_ip = ""
    ins = {}
    finstances = []

    for instance in instances:
        l_instance = []
        instance_keys = ""
        instance_keys2 = ""
        instance_keys3 = ""
        instance_keys4 = ""
        instance_id = ""
        instance_ip = ""
        ins = {}
        instance_id = instance.id
        instance_ip = instance.private_ip_address
        l_instance.append(instance_id)
        l_instance.append(instance_ip)
        for tag in instance.tags:
            if tag["Key"] == 't_name' or tag["Key"] == 'Name':
                instanceName = tag["Value"]
                instance_keys = instanceName
                l_instance.append(instance_keys)
            if tag["Key"] == 't_environment' or tag["Key"] == 't_Environment':
                environment = tag["Value"]
                instance_keys2 = environment
                l_instance.append(instance_keys2)
            if tag["Key"] == 't_Team' or tag["Key"] == 't_team':
                team = tag["Value"]
                instance_keys3 = team
                l_instance.append(instance_keys3)
            if tag["Key"] == 't_role' or tag["Key"] == 't_Role':
                role = tag["Value"]
                instance_keys4 = role
                l_instance.append(instance_keys4)
        ins['InstanceID'] = instance_id
        ins['instance_ip'] = instance_ip
        ins['instype'] = instance.instance_type
        ins['status'] = instance.state
        ins['avzone'] = instance.placement
        ins['t_name'] = instance_keys
        ins['t_environment'] = instance_keys2
        ins['t_Team'] = instance_keys3
        ins['t_role'] = instance_keys4
        finstances.append(ins)

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response


@app.route("/api/getec2byteam")
def getbyteam():
    env = request.args.get('env')
    boto3.setup_default_session(profile_name=env)
    ec2 = boto3.resource('ec2')
    team = request.args.get('team')
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:t_Team', 'Values': [team]}, {'Name': 'tag:t_CreatedBy', 'Values': ['ProjectX']}])
    l_instance = []
    instance_keys = ""
    instance_keys2 = ""
    instance_keys3 = ""
    instance_keys4 = ""
    instance_id = ""
    instance_ip = ""
    ins = {}
    finstances = []

    for instance in instances:
        l_instance = []
        instance_keys = ""
        instance_keys2 = ""
        instance_keys3 = ""
        instance_keys4 = ""
        instance_id = ""
        instance_ip = ""
        ins = {}
        instance_id = instance.id
        instance_ip = instance.private_ip_address
        # l_instance.append(instance_id)
        # l_instance.append(instance_ip)
        for tag in instance.tags:
            if tag["Key"] == 't_name' or tag["Key"] == 'Name':
                instanceName = tag["Value"]
                instance_keys = instanceName
                l_instance.append(instance_keys)
            if tag["Key"] == 't_environment' or tag["Key"] == 't_Environment':
                environment = tag["Value"]
                instance_keys2 = environment
                l_instance.append(instance_keys2)
            if tag["Key"] == 't_Team' or tag["Key"] == 't_team':
                team = tag["Value"]
                instance_keys3 = team
                l_instance.append(instance_keys3)
            if tag["Key"] == 't_role' or tag["Key"] == 't_Role':
                role = tag["Value"]
                instance_keys4 = role
                l_instance.append(instance_keys4)
        ins['InstanceID'] = instance_id
        ins['instance_ip'] = instance_ip
        ins['instype'] = instance.instance_type
        ins['status'] = instance.state
        ins['avzone'] = instance.placement
        ins['t_name'] = instance_keys
        ins['t_environment'] = instance_keys2
        ins['t_Team'] = instance_keys3
        ins['t_role'] = instance_keys4
        finstances.append(ins)

    response = app.response_class(
        response=json.dumps(finstances, indent=2),
        mimetype='application/json'
    )
    return response


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=8082)
