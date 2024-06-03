# YouTube to MP3 Downloader with AWS Lambda
This Python code implements a serverless function using AWS Lambda that allows users to download audio from YouTube videos and convert them to MP3 format. 
The downloaded MP3 files are then uploaded to a designated S3 bucket for storage.

## Important Note: 
Downloading and converting copyrighted content without permission is illegal. Use this project responsibly and only with videos that you have the rights to convert.

## Requirements:

- AWS Account with Lambda and S3 Services enabled
- Python 3.6 or later
- boto3 library (`pip install boto3`)
- pytube library (`pip install pytube`)

## Deployment:

- Create a new Lambda function in your AWS account and name it appropriately (e.g., youtube-to-mp3-converter).
- Choose Python 3.6 or later as the runtime environment.
- Copy and paste the provided Python code into the function's code editor.
- Configure the Lambda function with an environment variable named destination_bucket containing the name of your S3 bucket for storing the converted MP3 files.
- Grant the Lambda function appropriate permissions to access S3 using an IAM role.

## Limitations:

- This function uses `pytube` which may have limitations on downloadable video formats and resolutions.
- Converting and uploading large video files might exceed Lambda execution time limits.

## Security Considerations:

Downloading copyrighted content without permission is illegal. Use this project responsibly with videos you have the rights to convert.
Implement proper IAM roles and permissions for the Lambda function to access S3 securely.


## Disclaimer:

**This code is provided for educational purposes only. The author is not responsible for any misuse of this project.**
