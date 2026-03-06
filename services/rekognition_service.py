import boto3

rekognition = boto3.client('rekognition')

def detect_labels(bucket, key):

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxLabels=5
    )

    labels = []

    for label in response['Labels']:
        labels.append(label['Name'])

    return labels
