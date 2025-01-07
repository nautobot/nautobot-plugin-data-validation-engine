"""Create fixtures for tests."""

from nautobot_data_validation_engine.models import ValidationRule


def create_validationrule():
    """Fixture to create necessary number of ValidationRule for tests."""
    ValidationRule.objects.create(name="Test One")
    ValidationRule.objects.create(name="Test Two")
    ValidationRule.objects.create(name="Test Three")
