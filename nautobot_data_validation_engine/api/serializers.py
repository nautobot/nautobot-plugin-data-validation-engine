"""API serializers for nautobot_data_validation_engine."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_data_validation_engine import models


class ValidationRuleSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ValidationRule Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ValidationRule
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
