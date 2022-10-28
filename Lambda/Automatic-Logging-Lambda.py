import boto3, json

def lambda_handler(event, content):

    # 構築されたインスタンスID
    instanceId = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    # リソース作成者のユーザー情報
    userIdentity = event['detail']['userIdentity']
    userName = userIdentity['userName']
    
    # リソース作成日の情報
    creationDate = userIdentity['sessionContext']['attributes']['creationDate'][:10]
    
    
    # 構築されたインスタンスへのタグ付け
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
