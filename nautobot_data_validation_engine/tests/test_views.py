"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot_data_validation_engine import models
from nautobot_data_validation_engine.tests import fixtures


class ValidationRuleViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the ValidationRule views."""

    model = models.ValidationRule
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_validationrule()
