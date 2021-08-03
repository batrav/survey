from django.urls import path, include
from django.views.generic.base import View
from rest_framework.views import APIView

from . import views
from .views import ApiDataView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("",views.LandingPage , name = "landing-page"),
    path("survey-list",views.SurveyListView.as_view(), name='survey-list'),
    path("new-survey/<int:field_id>", views.CreateSurveyView.as_view(), name = "new-survey"),
    path("thank-you", views.ThankYouView.as_view()),
    path("survey/<int:pk>",views.SurveyDetailView.as_view(), name='survey-detail-view'),
    path("survey-by-id",views.SurveybyIDDetailView.as_view(), name='survey-by-id'),
    path('edit-survey/<int:pk>', views.EditSurveyView.as_view() , name='survey_edit'),
    path('edit-success', views.EditSurveyView.as_view() , name='edit_survey_success'),
    path('api-view/', ApiDataView.as_view(), name = "api-view")
    # path('api-view/<int:pk>', ApiDataView.as_view(), name = "api-view-by-id")
]
