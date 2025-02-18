from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        event = {
            "rawPath": "/hello",
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }
        expected_response = {
            "statusCode": 200,
            "body": {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        }

        self.assertEqual(self.HANDLER.handle_request(event, dict()), expected_response)
