from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        """
        Validate the request and return an error response if invalid.
        """
        path = event.get("rawPath", "/")
        method = event.get("requestContext", {}).get("http", {}).get("method", "")

        if path != "/hello" or method != "GET":
            return {
                "statusCode": 400,
                "body": {
                    "statusCode": 400,
                    "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
                }
            }
        return None

    def handle_request(self, event, context):
        """
        Handle requests to /hello GET.
        """
        error_response = self.validate_request(event)
        if error_response:
            return error_response

        return {
            "statusCode": 200,
            "body": {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
