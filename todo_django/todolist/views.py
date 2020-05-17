import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from todolist.models import TodoList, NovaEntidade

#-----------------#
# CRUD "TodoList" #
#-----------------#
def save_or_update_list(lista, data):
    lista.name = data['name']
    lista.description = data['description']
    lista.save()
    return lista

def crud_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lista = save_or_update_list(TodoList(), data)

        return JsonResponse({'id': lista.id})
    elif request.method == 'GET':
        _id = request.GET.get('id', None)

        try:
            todolist = TodoList.objects.get(id=_id)

            return JsonResponse({
                'id': todolist.id,
                'name': todolist.name,
                'description': todolist.description
            })
        except TodoList.DoesNotExist:
            return JsonResponse({
                'erro': 'Lista Inexistente'
            })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        lista = save_or_update_list(TodoList.objects.get(id=request.GET.get('id', None)), data)

        return JsonResponse({'id': lista.id})
    elif request.method == 'DELETE':
        _id = request.GET.get('id', None)

        todolist = TodoList.objects.filter(id=_id)
        todolist.delete()
        return JsonResponse({
            'mensagem': 'Lista removida com sucesso!'
        })
    else:
        return HttpResponse('Tipo de requisição não implementada!')

#---------------------#
# CRUD "NovaEntidade" #
#---------------------#
def save_or_update_nova_entidade(entidade, data):
    entidade.name = data['name']
    entidade.sort = data['sort']
    entidade.save()
    return entidade

def crud_nova_entidade(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lista = save_or_update_nova_entidade(NovaEntidade(), data)

        return JsonResponse({'id': lista.id})
    elif request.method == 'GET':
        _id = request.GET.get('id', None)

        try:
            todolist = NovaEntidade.objects.get(id=_id)

            return JsonResponse({
                'id': todolist.id,
                'name': todolist.name,
                'sort': todolist.sort
            })
        except NovaEntidade.DoesNotExist:
            return JsonResponse({
                'erro': 'Lista Inexistente'
            })

    elif request.method == 'PUT':
        data = json.loads(request.body)
        lista = save_or_update_nova_entidade(NovaEntidade.objects.get(id=request.GET.get('id', None)), data)

        return JsonResponse({'id': lista.id})
    elif request.method == 'DELETE':
        _id = request.GET.get('id', None)

        todolist = NovaEntidade.objects.get(id=_id)
        todolist.delete()
        return JsonResponse({
            'mensagem': 'Lista removida com sucesso!'
        })
    else:
        return HttpResponse('Tipo de requisição não implementada!')

#-------------------------#
# Métodos de retorno HTML #
#-------------------------#
def home(request):
    return render(request, 'list.html')

def pegar_list(request):
    _id = request.GET.get('id', None)

    if _id:
        todolist = TodoList.objects.get(id=_id)

    todas_as_listas = TodoList.objects.all()

    return render(request, 'list.html', {
        'todas_as_listas': todas_as_listas,
        'todolist': todolist
    })

def criar_list(request):
    name = request.GET.get('name')
    description = request.GET.get('description')

    todolist = TodoList()

    todolist.name = name
    todolist.description = description

    todolist.save()

    return HttpResponse('Lista Criada!')