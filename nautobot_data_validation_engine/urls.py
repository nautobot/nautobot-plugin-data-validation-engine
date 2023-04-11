"""Django url patterns."""

from django.urls import path

from nautobot.core.views.routers import NautobotUIViewSetRouter
from nautobot.extras.views import ObjectChangeLogView, ObjectNotesView

from nautobot_data_validation_engine import views, models


router = NautobotUIViewSetRouter()
router.register("regex-rules", views.RegularExpressionValidationRuleUIViewSet)
router.register("min-max-rules", views.MinMaxValidationRuleUIViewSet)
router.register("required-rules", views.RequiredValidationRuleUIViewSet)
router.register("unique-rules", views.UniqueValidationRuleUIViewSet)
router.register("validation-result", views.ValidationResultListView)

urlpatterns = [
    path(
        "regex-rules/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="regularexpressionvalidationrule_changelog",
        kwargs={"model": models.RegularExpressionValidationRule},
    ),
    path(
        "regex-rules/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="regularexpressionvalidationrule_notes",
        kwargs={"model": models.RegularExpressionValidationRule},
    ),
    path(
        "min-max-rules/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="minmaxvalidationrule_changelog",
        kwargs={"model": models.MinMaxValidationRule},
    ),
    path(
        "min-max-rules/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="minmaxvalidationrule_notes",
        kwargs={"model": models.MinMaxValidationRule},
    ),
    path(
        "required-rules/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="requiredvalidationrule_changelog",
        kwargs={"model": models.RequiredValidationRule},
    ),
    path(
        "required-rules/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="requiredvalidationrule_notes",
        kwargs={"model": models.RequiredValidationRule},
    ),
    path(
        "unique-rules/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="uniquevalidationrule_changelog",
        kwargs={"model": models.UniqueValidationRule},
    ),
    path(
        "unique-rules/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="uniquevalidationrule_notes",
        kwargs={"model": models.UniqueValidationRule},
    ),
    path(
        "validation-results/<model>/<id>/",
        views.ValidationResultObjectView.as_view(),
        name="validationresults",
    ),
    path(
        "validation-result/<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="validationresult_changelog",
        kwargs={"model": models.ValidationResult},
    ),
    path(
        "validation-result/<uuid:pk>/notes/",
        ObjectNotesView.as_view(),
        name="validationresult_notes",
        kwargs={"model": models.ValidationResult},
    ),
] + router.urls
