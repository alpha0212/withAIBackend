from .views import DigitViewSet
from rest_framework.routers import DefaultRouter

# urls.py에 등록할 수 있는 뷰 세트
router = DefaultRouter()
router.register(r'digits', DigitViewSet)
urlpatterns = router.urls
