"""Test ValidationRule."""

from django.test import TestCase

from nautobot_data_validation_engine import models


class TestValidationRule(TestCase):
    """Test ValidationRule."""

    def test_create_validationrule_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        validationrule = models.ValidationRule.objects.create(name="Development")
        self.assertEqual(validationrule.name, "Development")
        self.assertEqual(validationrule.description, "")
        self.assertEqual(str(validationrule), "Development")

    def test_create_validationrule_all_fields_success(self):
        """Create ValidationRule with all fields."""
        validationrule = models.ValidationRule.objects.create(name="Development", description="Development Test")
        self.assertEqual(validationrule.name, "Development")
        self.assertEqual(validationrule.description, "Development Test")
