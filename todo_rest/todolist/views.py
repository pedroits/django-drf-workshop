from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from todolist.models import TodoList, TodoTask
from todolist.serializers import TodoListSerializer, TodoTaskSerializer

class TodoListView(APIView):
    obj = None
    serializer = None

    def get_object(self, id):
        try:
            return TodoList.objects.get(id=id)
        except TodoList.DoesNotExist:
            raise serializers.ValidationError({'error': 'List não existe'})

    def save_serializer(self, serialized):
        if serialized.is_valid():
            serialized.save()
            return serialized

        raise serializers.ValidationError(serialized.errors)

    def get(self, request, id=None):
        serialized_todolist = TodoListSerializer(instance=self.get_object(id))
        return Response(serialized_todolist.data, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serialized_todolist = self.save_serializer(TodoListSerializer(data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_201_CREATED)

    def put(self, request, id=None):
        serialized_todolist = self.save_serializer(TodoListSerializer(instance=self.get_object(id), data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id=None):
        self.get_object(id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TodoTaskView(APIView):
    obj = None
    serializer = None

    def get_object(self, id):
        try:
            return TodoTask.objects.get(id=id)
        except TodoTask.DoesNotExist:
            raise serializers.ValidationError({'error': 'List não existe'})

    def save_serializer(self, serialized):
        if serialized.is_valid():
            serialized.save()
            return serialized

        raise serializers.ValidationError(serialized.errors)

    def get(self, request, id=None):
        serialized_todolist = TodoTaskSerializer(instance=self.get_object(id))
        return Response(serialized_todolist.data, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serialized_todolist = self.save_serializer(TodoTaskSerializer(data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_201_CREATED)

    def put(self, request, id=None):
        serialized_todolist = self.save_serializer(TodoTaskSerializer(instance=self.get_object(id), data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id=None):
        self.get_object(id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)

"""
O exemplo abaixo foi dado rapidamente no final do workshop.
Ele é a base do principio de "Mixins" do DjangoRestFramework, onde o pressuposto
inicial é que a views tem sempre o mesmo comportamento. O GET é receber um ID e retornar
a entidade, o POST é receber dados para criar uma entidade nova, o PUT é receber um ID e
dados para alterar essa entidade, e o DELETE é receber um ID para remover essa entidade.

Nessa linha, o que mudaria entre as N views que podem ser criadas são os models que ela
trabalha e os serializers que são usados. Portanto cria-se uma GenericView que atende os
comportamentos padrões, e as classes de model e serializer que essa view usa são setados
dentro da classe que extende ela.
"""
class GenericView(APIView):
    entity_model = None
    entity_serializer = None

    def get_object(self, id):
        try:
            return self.entity_model.objects.get(id=id)
        except self.entity_model.DoesNotExist:
            raise serializers.ValidationError({'error': 'List não existe'})

    def save_serializer(self, serialized):
        if serialized.is_valid():
            serialized.save()
            return serialized

        raise serializers.ValidationError(serialized.errors)

    def get(self, request, id=None):
        serialized_todolist = self.entity_serializer(instance=self.get_object(id))
        return Response(serialized_todolist.data, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serialized_todolist = self.save_serializer(self.entity_serializer(data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_201_CREATED)

    def put(self, request, id=None):
        serialized_todolist = self.save_serializer(self.entity_serializer(instance=self.get_object(id), data=request.data))
        return Response(serialized_todolist.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id=None):
        self.get_object(id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class TodoListGenericView(GenericView):
    entity_model = TodoList
    entity_serializer = TodoListSerializer

class TodoTaskGenericView(GenericView):
    entity_model = TodoTask
    entity_serializer = TodoTaskSerializer
