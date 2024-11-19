from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Writing


class WritingListView(ListView):
    model = Writing
    template_name = "writings.html"
    context_object_name = "writings"


class WritingDetailView(DetailView):
    model = Writing
    template_name = "writing.html"
    context_object_name = "writing"
    success_url = reverse_lazy('writings')


class WritingUpdateView(UpdateView):
    model = Writing
    template_name = "writing_edit.html"
    fields = ['title', 'publication_year']
    success_url = reverse_lazy('writings')


class WritingCreateView(CreateView):
    model = Writing
    template_name = "writing_add.html"
    success_url = reverse_lazy('writings')
    fields = '__all__'
