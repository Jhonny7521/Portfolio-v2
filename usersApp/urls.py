from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, LoginUserView, VisitsView

from .views import LogoutUserView

urlpatterns = [
    path('accounts/login/', LoginUserView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('see_visits/', VisitsView.as_view(), name = 'see_visits'),
    # path('test/', test_celery, name='test_celery')
]


