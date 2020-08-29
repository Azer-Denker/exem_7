# from django.db.models import Q
# from django.shortcuts import redirect
#
# from django.urls import reverse, reverse_lazy
# from django.utils.http import urlencode
# from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, FormView, View
#
# from webapp.forms import ArticleForm, ArticleCommentForm, SimpleSearchForm, FullSearchForm
from webapp.models import Answer, Poll, Choice


class AnswerView(View):
    template_name = 'answer/list.html'
    context_object_name = 'answers'
    model = Answer

    def get(self, request, *args, **kwargs):
        context = {}
        context['poll'] = Poll.objects.get(pk=kwargs['pk'])
        print(context)
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=kwargs['pk'])
        choice = Choice.objects.get(pk=request.POST.get('choice'))


        Answer.objects.create(poll=poll, choice=choice)
        return redirect('index')






