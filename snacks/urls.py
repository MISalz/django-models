from django.urls import path

from .views import SnackListPageView, SnackDetailPageView

urlpatterns = [
  
	path ('', SnackListPageView.as_view(), name='snack_list'),
	
	path ('<int:pk>/', SnackDetailPageView.as_view(), name='snack_detail')

]
