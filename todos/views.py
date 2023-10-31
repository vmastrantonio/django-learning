from django.shortcuts import render

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all
    return render(request, "todos/todo_list.html", {'todos': todos})

def teste(request):
    nome = "Cleyson"
    alunos = ["aluno1", "aluno2", "aluno3"]
    return render(request, "todos/todo_list.html", {"nome": nome, "alunos": alunos})
