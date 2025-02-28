from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json
import logging
_LOG = get_logger(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        """
        Explain incoming event here
        """

        # TODO: implement business logic
        try:
            for record in event['Records']:
                message_body = record['body']
                logger.info(f"Received SNS message: {message_body}")

            return {
                "statusCode": 200,
                "body": json.dumps("Messages logged successfully!")
            }

        except Exception as e:
            logger.error(f"Error processing SNS message: {str(e)}")
            return {
                "statusCode": 500,
                "body": json.dumps("Error processing messages.")
            }

    

HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
