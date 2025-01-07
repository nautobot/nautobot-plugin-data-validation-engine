"""API views for nautobot_data_validation_engine."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_data_validation_engine import filters, models
from nautobot_data_validation_engine.api import serializers


class ValidationRuleViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ValidationRule viewset."""

    queryset = models.ValidationRule.objects.all()
    serializer_class = serializers.ValidationRuleSerializer
    filterset_class = filters.ValidationRuleFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
