from django.shortcuts import render
from .models import Todo

# from django.views import View # this line was for using View class

# from django.views.generic.base import TemplateView

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

# from django.views.generic.edit import FormView
# from .forms import TodoCreateForm

from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages

from django.views.generic.edit import CreateView

from django.views.generic.edit import DeleteView

from django.views.generic.edit import UpdateView

# Create your views here.


# --------------------------- function based view -----------------------------
# def home(request):
#     return render(request, 'first/home.html')
# -----------------------------------------------------------------------------

# ------------------------ Class based view using View ------------------------
# class Home(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'first/home.html', {'name':'Mahdi'})
# -----------------------------------------------------------------------------

# ------------------- Class based view using TemplateView ---------------------
# class Home(TemplateView):
#     template_name = 'first/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['todos'] = Todo.objects.all()
#         return context
# -----------------------------------------------------------------------------

class Home(ListView):
    template_name = 'first/home.html'
    # queryset = Todo.objects.all() # object_list is default name for this query set in template
    # model = Todo
    context_object_name = 'todos'
    ordering = ['-created_at']

    def get_queryset(self):
        return Todo.objects.all()    


class DetailTodo(DetailView):
    # model = Todo

    # -----------

    slug_field = 'slug' # slug field name in model
    slug_url_kwarg = 'myslug' # slug arg in urls

    def get_queryset(self, **kwargs):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(slug=self.kwargs['myslug'])
        else:
            return Todo.objects.none()

            
# class TodoCreateView(FormView):
#     form_class = TodoCreateForm
#     template_name = 'first/todo_create.html'
#     success_url = reverse_lazy('first:home')

#     def form_valid(self, form):
#         self.create_todo(form.cleaned_data)
#         return super().form_valid(form)

#     def create_todo(self, data):
#         todo = Todo(title=data['title'], slug=slugify(data['title']))
#         todo.save()
#         messages.success(self.request, 'your todo added', 'success')


class TodoCreateView(CreateView):
    model = Todo
    fields = ('title',)
    template_name = 'first/todo_create.html'
    success_url = reverse_lazy('first:home')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.slug = slugify(form.cleaned_data['title'])
        todo.save()
        messages.success(self.request, 'your todo added', 'success')
        return super().form_valid(form)


class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'first/todo_delete.html'
    success_url = reverse_lazy('first:home')


class UpdateTodo(UpdateView):
    model = Todo
    fields = ['title']
    template_name = 'first/update_todo.html'
    success_url = reverse_lazy('first:home')