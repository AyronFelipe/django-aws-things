import os

from datetime import datetime

import boto3


def lambda_handler(event, context):
    """
    AWS Lambda function to calculate the birth year based on a given age or trigger a secondary action.

    This Lambda function serves as the entry point for processing AWS Lambda events.
    It can perform two different actions based on the type of event received.

    Parameters:
    event (dict): The event object passed to the Lambda function. It should contain either a JSON message with the 'age'
    field for age calculation or be in a specific format for a secondary action.
    context (LambdaContext): The Lambda function execution context (not used in this function).

    Returns:
    int or bool: If the event triggers age calculation, it returns the calculated birth year (int).
    If the event triggers a secondary action, it returns a boolean value (bool) indicating success.
    """
    result = None
    if "Records" in event:
        result = publish_to_sns()
    else:
        result = calculates_birthday_year(event)

    return result


def calculates_birthday_year(event):
    """
    Calculate the year of birth based on the provided age.

    This function extracts the age from an AWS Lambda event, calculates the year of birth by subtracting the age from
    the current year and returns the calculated year.

    Args:
    event (dict): An Lambda event containing information about the age. The age should be provided in the event body.

    Returns:
    int: The calculated year of birth.
    """
    age = event.get("age")
    current_year = datetime.now().year
    year_of_birthday = current_year - age
    return year_of_birthday


def publish_to_sns():
    """
    Publishes a message to an Amazon SNS topic.

    This function uses the AWS SDK (boto3) to publish a message to an Amazon Simple Notification Service (SNS) topic.

    Returns:
    bool: True if the message was published successfully, False otherwise.
    """
    client = boto3.client("sns")
    arn = os.environ["SNS_TOPIC_ARN"]
    message = "Message published with success"
    response = client.publish(TopicArn=arn, Message=message)
    return "MessageId" in response
