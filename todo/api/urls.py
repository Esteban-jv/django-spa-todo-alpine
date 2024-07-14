from rest_framework import routers

from .viewsets import TodoViewSet

route = routers.SimpleRouter()
route.register('todo',TodoViewSet)

urlpatterns = route.urls