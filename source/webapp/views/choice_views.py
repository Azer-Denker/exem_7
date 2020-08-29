from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode

from webapp.forms import ChoiceForm, SimpleSearchForm
from webapp.models import Choice
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ChoiceView(ListView):
    template_name = 'choice/list.html'
    context_object_name = 'choices'
    model = Choice
    # ordering = ['-created_at']
    paginate_by = 4
    paginate_orphans = 1


class ChoiceDetailView(DetailView):
    template_name = 'choice/choice.html'
    context_object_name = 'choice'
    model = Choice


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('choice_view', kwargs={'pk': self.object.pk})


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('choice_view', kwargs={'pk': self.object.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    context_object_name = 'choice'
    success_url = reverse_lazy('poll_view')
