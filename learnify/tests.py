import os
import json
import random
from unittest import mock, TestCase
from django.conf import settings
from learnify.utils import contingency

class UtilsTestCase(TestCase):
    @mock.patch('learnify.utils.os.listdir')
    @mock.patch('learnify.utils.open', new_callable=mock.mock_open, read_data='{"key": "value"}')
    def test_contingency(self, mock_open, mock_listdir):
        # Arrange
        mock_listdir.return_value = ['quiz_15-53.json', 'quiz_18-49.json']
        random.seed(0)  # Ensure random.choice is predictable

        # Act
        result = contingency()

        # Assert
        mock_listdir.assert_called_once_with(os.path.join(settings.MEDIA_ROOT, "quiz"))
        mock_open.assert_called_once_with(os.path.join(settings.MEDIA_ROOT, "quiz", 'quiz_18-49.json'), "r", newline="")
        self.assertEqual(result, {"key": "value"})