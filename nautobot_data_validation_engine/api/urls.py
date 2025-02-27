"""Django API urlpatterns declaration for nautobot_data_validation_engine app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_data_validation_engine.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("validationrule", views.ValidationRuleViewSet)

app_name = "nautobot_data_validation_engine-api"
urlpatterns = router.urls
