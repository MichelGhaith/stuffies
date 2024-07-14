from rest_framework.routers import DefaultRouter
from . import views
urlpatterns = []
router = DefaultRouter(trailing_slash=False)
router.register('', views.ProductViewSet, basename='products')
urlpatterns += router.urls
