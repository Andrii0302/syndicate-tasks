from tests.test_sns_handler import SnsHandlerLambdaTestCase


class TestSuccess(SnsHandlerLambdaTestCase):

    def test_success(self):
        self.assertEqual(1,1)

