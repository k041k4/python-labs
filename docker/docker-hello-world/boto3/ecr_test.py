import boto3
client = boto3.client('ecr')
response = client.describe_repositories(
    repositoryNames=[
        'spheres-test2',
    ]
)

print(response)
