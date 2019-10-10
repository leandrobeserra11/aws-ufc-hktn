import boto3

s3 = boto3.resource('s3')
data = open('musga2.mp3', 'rb')
s3.Bucket('rumadecoisa').put_object(Key='musga2.mp3', Body=data)