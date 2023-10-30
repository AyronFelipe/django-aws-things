import json
import logging

from typing import Any

import boto3
import botocore

from challenge.apps.core.models import Message

logger = logging.getLogger(__name__)


def get_queue_if_exists_otherwise_creates(queue_name: str) -> Any:
    """
    Retrieve an existing Amazon SQS queue by name or create a new one if it doesn't exist.

    Args:
        queue_name (str): The name of the queue to retrieve or create.

    Returns:
        Any: An instance of the Amazon SQS queue.
    """
    sqs = boto3.resource("sqs")
    try:
        queue = sqs.get_queue_by_name(QueueName=queue_name)
    except botocore.errorfactory.QueueDoesNotExist:
        logger.warning(f"A queue with name {queue_name} does not exists, so we'll create one")
        queue = sqs.create_queue(QueueName=queue_name)
    return queue


def save_message(destination: str, body: str):
    return Message.objects.create(destination=destination, body=body)


def send(queue_name: str):
    """
    A decorator to send data from a model instance to an Amazon SQS queue.

    Args:
        queue_name (str): The name of the Amazon SQS queue to send messages to.
    """

    def save(self, *args, **kwargs):
        """
        Save the model instance and send its data to the specified SQS queue.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        This method extends the model's `save` method to send a JSON-serialized message to the specified SQS queue.
        """
        super(self.__class__, self).save(*args, **kwargs)
        queue = get_queue_if_exists_otherwise_creates(queue_name=queue_name)
        body = self.body_to_sent()
        message_body = json.dumps(body)
        save_message(destination=queue_name, body=message_body)
        queue.send_message(MessageBody=message_body)

    def decorator_send(cls):
        """
        Decorator function that adds the custom `save` method to the model class.

        Args:
            cls: The model class to decorate.

        Returns:
            cls: The decorated model class.
        """
        cls.save = save
        return cls

    return decorator_send
