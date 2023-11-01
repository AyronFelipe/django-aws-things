import json
import logging

from typing import Any
from typing import Dict

import boto3

logger = logging.getLogger(__name__)


def call_lambda(function_name: str, body: Dict) -> Any:
    """
    Invoke an AWS Lambda function and return the result.

    This function allows you to invoke another AWS Lambda function synchronously and retrieve its result.

    Parameters:
    function_name (str): The name or ARN of the Lambda function to invoke.
    body (dict): The input payload to pass to the Lambda function.

    Returns:
    dict: The result returned by the invoked Lambda function, represented as a dictionary.
    """
    lambda_client = boto3.client("lambda")

    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType="RequestResponse",
        Payload=json.dumps(body),
    )

    if response["StatusCode"] != 200:
        logging.warning("The call of lambda returned an error!")
        return

    result = json.loads(response["Payload"].read())
    return result
