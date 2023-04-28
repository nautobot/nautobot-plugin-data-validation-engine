"""Jobs for nautobot_data_validation_engine."""

from django.apps import apps as global_apps

from nautobot.extras.models import GitRepository
from nautobot.extras.jobs import Job, MultiChoiceVar, BooleanVar

from .custom_validators import get_classes_from_git_repo, get_data_compliance_rules


def get_choices():
    """Get choices from registry."""
    choices = []
    for ruleset_class in get_data_compliance_rules():
        choices.append((ruleset_class.__name__, ruleset_class.__name__))
    for repo in GitRepository.objects.all():
        if "nautobot_data_validation_engine.data_compliance_rules" in repo.provided_contents:
            for compliance_class in get_classes_from_git_repo(repo):
                choices.append((compliance_class.__name__, compliance_class.__name__))

    choices.sort()
    return choices


class RunRegisteredDataComplianceRules(Job):
    """Run the validate function on all registered DataComplianceRule classes."""

    selected_classes = MultiChoiceVar(
        choices=get_choices,
        label="Select Data Compliance Classes",
        required=False,
        description="Not selecting any classes will run all classes listed.",
    )
    override_enforce = BooleanVar(
        default=True,
        label="Override Ruleset Enforce",
        description="Override any enforce values set on the DataComplianceRule classes. Not overriding this value will cause any enforced ComplianceErrors to fail the job.",
    )

    def run(self, data, commit):
        """Run the validate function on all given DataComplianceRule classes."""
        selected_classes = data.get("selected_classes")
        override_enforce = data.get("override_enforce")

        compliance_classes = []
        compliance_classes.extend(get_data_compliance_rules())

        for repo in GitRepository.objects.all():
            if "nautobot_data_validation_engine.data_compliance_rules" in repo.provided_contents:
                compliance_classes.extend(get_classes_from_git_repo(repo))

        for compliance_class in compliance_classes:
            if selected_classes and compliance_class.__name__ not in selected_classes:
                continue
            self.log_info(f"Running {compliance_class.__name__}")
            app_label, model = compliance_class.model.split(".")
            for obj in global_apps.get_model(app_label, model).objects.all():
                ins = compliance_class(obj)
                if override_enforce:
                    ins.enforce = False
                ins.clean()


jobs = [RunRegisteredDataComplianceRules]