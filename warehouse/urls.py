from django .urls import path
from .views import CalculateMaterialsView
urlpatterns = [
    path('', CalculateMaterialsView.as_view())
]

