from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import ChoiceForm
from webapp.models import Choice


class ChoiceView(ListView):
    template_name = 'choice/list.html'
    context_object_name = 'choices'
    model = Choice
    paginate_by = 3
    paginate_orphans = 0


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
