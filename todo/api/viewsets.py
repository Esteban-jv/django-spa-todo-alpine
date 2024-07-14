from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializer import TodoSerializer
from app.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('order') # Esta línea no es negociable
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    # Lógica antes de obtener resultados de la bd (queryset)
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user.id).all().order_by('order')

    # Lógica antes de crear un objeto (Añadir columnas automáticas)
    def perform_create(self, serializer):
        serializer.save(
            user=User.objects.get(pk=self.request.user.id),
            order=Todo.objects.filter(user=self.request.user.id).count()
        )

    @action(detail=False, methods=['POST'])
    def sort(self, request):
        ids = request.POST.get('ids').split(',')
        # ids = [1,20,2,6,3]
        print(ids)

        for i,t in enumerate(ids):
            print("{} - {}".format(i,t))
            Todo.objects.filter(pk=t).update(order=i)

        return Response('ok')

    @action(detail=False, methods=['DELETE']) #url_path='borrar' #En caso que quieras cambiar el endpoint
    def delete(self, request):
        Todo.objects.filter(user=request.user.id).delete()

        return Response('ok')