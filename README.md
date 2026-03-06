# AWS Serverless Image Processing Pipeline

This project demonstrates a **serverless image processing pipeline** using AWS services.  
When an image is uploaded to Amazon S3, AWS Lambda is triggered automatically and analyzes the image using Amazon Rekognition.

---

## Architecture

User Upload Image → S3 Bucket → Lambda Trigger → Rekognition Analysis → CloudWatch Logs

---

## AWS Services Used

- AWS Lambda
- Amazon S3
- Amazon Rekognition
- Amazon CloudWatch
- AWS CLI

---

## Project Structure

lambda-image-project
│
├── handler.py
├── services/
│ ├── s3_service.py
│ └── rekognition_service.py
├── utils/
│ └── logger.py
└── requirements.txt

Package Lambda Function
zip -r function.zip .

Create Lambda Function
aws lambda create-function \
--function-name image-processor \
--runtime python3.12 \
--role arn:aws:iam::ACCOUNT_ID:role/lambda-image-role \
--handler handler.lambda_handler \
--zip-file fileb://function.zip

Update Lambda Code
aws lambda update-function-code \
--function-name image-processor \
--zip-file fileb://function.zip


Check response:
cat response.json

Upload Image to S3
aws s3 cp photo.jpg s3://upload-bucket4734


Configure S3 Trigger for Lambda

Allow S3 to invoke Lambda:

aws lambda add-permission \
--function-name image-processor \
--statement-id s3-trigger \
--action lambda:InvokeFunction \
--principal s3.amazonaws.com \
--source-arn arn:aws:s3:::upload-bucket4734


Configure bucket notification:s s3api put-bucket-notification-configuration \
--bucket upload-bucket4734 \
--notification-configuration '{
"LambdaFunctionConfigurations": [
{
"LambdaFunctionArn": "arn:aws:lambda:us-east-1:ACCOUNT_ID:function:image-processor",
"Events": ["s3:ObjectCreated:*"]
}
]
}'



Workflow

Upload image to Amazon S3

S3 triggers AWS Lambda

Lambda extracts image metadata

Lambda calls Amazon Rekognition

Labels detected and logged in CloudWatch



Example Response
{
  "statusCode": 200,
  "body": "Image processed successfully"
}



Skills Demonstrated

Serverless Architecture

AWS Lambda Development

Event-driven Systems

AWS CLI Automation

Cloud Monitoring with CloudWatch

AI Image Analysis with Rekognition



