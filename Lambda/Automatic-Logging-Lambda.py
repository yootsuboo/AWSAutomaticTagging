import boto3, json

def lambda_handler(event, content):

    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    userName = event['detail']['userIdentity']['userName']
    
    creationDate = event['detail']['userIdentity']['sessionContext']['attributes']['creationDate'][:10]
    
    
    ec2 = boto3.client('ec2')
    ec2.create_tags(
        Resources=[instanceId,],
        Tags=[
            {'Key': 'Owner', 'Value': userName},
            {'Key': 'CreationDate', 'Value': creationDate},
        ]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Excuted!')
    }
