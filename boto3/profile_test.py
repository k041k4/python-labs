import boto3

aws_session = boto3.Session()
sts_client = aws_session.client('sts')
aws_response = sts_client.get_caller_identity()
print('\nDEFAULT\n-',aws_response,'\n')
del sts_client, aws_response

boto3.setup_default_session(profile_name='vbaranek')
aws_profile = 'vbaranek'
aws_session = boto3.Session(profile_name=aws_profile)
sts_client = aws_session.client('sts')
aws_response = sts_client.get_caller_identity()
print('SET DEFAULT = vbaranek\n-',aws_response,'\n')
del sts_client, aws_response

aws_session = boto3.Session()
sts_client = aws_session.client('sts')
aws_response = sts_client.get_caller_identity()
print('NO SETUP\n-',aws_response,'\n')
del sts_client, aws_response


