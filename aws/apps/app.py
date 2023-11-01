import json
import os

from datetime import datetime

import boto3


def lambda_handler(event, context):
    """
    Lambda function to calculate the birth year based on a given age.

    Parameters:
        event (dict): The event object passed to the Lambda function. It should contain a JSON message with the 'age'
        field.
        context (LambdaContext): The Lambda function execution context (not used in this function).

    Returns:
        int: The calculated birth year based on the provided age.
    """
    body = json.loads(event.get("Records")[0].get("body"))
    age = body.get("age")
    current_year = datetime.now().year
    year_of_birthday = current_year - age

    client = boto3.client("sns")
    arn = os.environ["SNS_TOPIC_ARN"]
    message = "Message published with success"
    client.publish(TopicArn=arn, message=message)

    return year_of_birthday
