import json
from pytube import YouTube 
import os 
import logging
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implementd
    destination_bucket ="youtube-2-mp3-files"
    # url input from user 
    yt = YouTube( 
        str("https://youtu.be/Mt-JJBabxiA")) 
      
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
      
    # check for destination to save file 
    print("Enter the destination (leave blank for current directory)") 
    destination = "/tmp"
      
    # download the file 
    out_file = video.download(output_path=destination) 
      
    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    print(new_file)
    upload_file(new_file, destination_bucket)
      
    # result of success 
    print(yt.title + " has been successfully downloaded.")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
