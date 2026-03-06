from services.s3_service import get_image_info
from services.rekognition_service import detect_labels
from utils.logger import log
def lambda_handler(event, context):
    bucket, key = get_image_info(event)
    log(f"processing image {key} from {bucket}")
    labels = detect_labels(bucket, key)
    for label in labels:
        log(f"Detected: {label}")
        return {
                "ststusCode": 200,
                "body": "Image processed successfully"
                }
