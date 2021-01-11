import os
import json
import urllib.parse
import boto3
import datetime

print('Loading function')

s3 = boto3.resource('s3')

def copy_Object_to_folder(bucket, to_folder, from_key, to_key):
    copy_to_path = os.path.join(to_folder, to_key) 
    copy_source =  {
    'Bucket': bucket,
    'Key': from_key
    }

    response = s3.meta.client.copy(copy_source, bucket, copy_to_path)
    return response

def lambda_handler(event, context):
   
    # Get the object from the event and show its content type
    #bucket：S3のバケット名
    #key：バックアップを取得するファイル名
    #backup_folder：バックアップ先のフォルダ名
    #prod
    #bucket = event['bucket']
    #key = urllib.parse.unquote_plus(event['key'], encoding='utf-8')
    #backup_folder = event['backup_folder']
    #local
    bucket = 's3bucketname'
    key = 'key'
    backup_folder = 'backupfoldername'
    backup_key = key + '_' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        response = copy_Object_to_folder(bucket, backup_folder, key, backup_key)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

