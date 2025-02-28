from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json
_LOG = get_logger(__name__)


class SqsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        for record in event['Records']:
            print("Received SQS message:", json.dumps(record, indent=2))
        return {"statusCode": 200, "body": "Message processed"}
    

HANDLER = SqsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
