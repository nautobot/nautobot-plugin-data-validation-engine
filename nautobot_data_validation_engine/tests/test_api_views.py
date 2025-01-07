"""Unit tests for nautobot_data_validation_engine."""

from nautobot.apps.testing import APIViewTestCases

from nautobot_data_validation_engine import models
from nautobot_data_validation_engine.tests import fixtures


class ValidationRuleAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for ValidationRule."""

    model = models.ValidationRule
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_validationrule()
