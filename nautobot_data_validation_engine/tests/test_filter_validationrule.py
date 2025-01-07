"""Test ValidationRule Filter."""

from django.test import TestCase

from nautobot_data_validation_engine import filters, models
from nautobot_data_validation_engine.tests import fixtures


class ValidationRuleFilterTestCase(TestCase):
    """ValidationRule Filter Test Case."""

    queryset = models.ValidationRule.objects.all()
    filterset = filters.ValidationRuleFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ValidationRule Model."""
        fixtures.create_validationrule()

    def test_q_search_name(self):
        """Test using Q search with name of ValidationRule."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for ValidationRule."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
