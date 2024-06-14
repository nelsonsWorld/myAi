from django.urls import path
from projects import views as vi

urlpatterns = [
    path("", vi.project_index, name="project_index"),
    path("<int:pk>/", vi.project_detail, name="project_detail"),
]
