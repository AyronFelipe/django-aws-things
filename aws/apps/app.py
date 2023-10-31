import json

from datetime import datetime


def lambda_handler(event, context):
    body = json.loads(event.get("Records")[0].get("body"))
    age = body.get("age")
    current_year = datetime.now().year
    year_of_birthday = current_year - age
    return year_of_birthday
