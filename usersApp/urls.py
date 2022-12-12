from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, LoginUserView

from .views import LogoutUserView

urlpatterns = [
    path('accounts/login/', LoginUserView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    # path('test/', test_celery, name='test_celery')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
