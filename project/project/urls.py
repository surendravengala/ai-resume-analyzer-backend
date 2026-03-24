from django.contrib import admin
from django.urls import path
from app.views import AnalyzeResumeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/analyze/', AnalyzeResumeView.as_view()),
]