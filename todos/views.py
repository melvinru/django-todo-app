from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoItem

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    ordering = ['is_resolved', 'due_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_todos'] = TodoItem.objects.filter(is_resolved=False).order_by('due_date')
        context['resolved_todos'] = TodoItem.objects.filter(is_resolved=True).order_by('-due_date')
        return context

class TodoCreateView(CreateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date', 'is_resolved']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

def toggle_status(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    return redirect('todo_list')
