from django.urls import path
from .views import WordDelete, WordList,WordDetail,WordCreate,WordUpdate,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', WordList.as_view(), name='words'),
    path('word/<int:pk>/', WordDetail.as_view(), name='word'),
    path('word-create', WordCreate.as_view(), name='word-create'),
    path('word-update/<int:pk>', WordUpdate.as_view(), name='word-update'),
    path('word-delete/<int:pk>', WordDelete.as_view(), name='word-delete'),
]