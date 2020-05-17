from rest_framework import serializers
from todolist.models import TodoList, TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):
    atrasado = serializers.BooleanField(required=False)

    def validate_description(self, data):
        if len(data) < 50:
            raise serializers.ValidationError({'error': '(description) precisa ter no mínimo 50 caracteres'})
        return data

    def create(self, validated_data):
        validated_data['info'] = 'Acabou de ser criado'

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.modified_info:
            modified_info = instance.modified_info
        else:
            modified_info = ''

        modified_info += '\nModificou de Novo'

        validated_data['modified_info'] = modified_info

        return super().update(instance, validated_data)

    class Meta:
        model = TodoTask
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):
    #tasks = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    tasks = TodoTaskSerializer(read_only=True, many=True)

    class Meta:
        model = TodoList
        fields = '__all__'
