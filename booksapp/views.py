# -*- coding: utf-8 -*-
import random
from django.views import generic
from django.shortcuts import get_object_or_404
from models import Books


# with open('books.json') as json_data:
#     b = json.load(json_data)
#     json_data.close()
#
# booksSaver = BooksSerializer(data=b, many=True)
# if booksSaver.is_valid():
#     booksSaver.save()


class IndexView(generic.ListView):
    template_name = 'index.html'
    # context_object_name = 'random_no_list'
    # model = Books
    # r = random.sample(range(1,(len(Books.objects.all()))), 5)

    def get_context_data(self, **kwargs):
        r = random.sample(range(1, (len(Books.objects.all()))), 6)
        lb = len(Books.objects.all())
        cnt = [i for i in range(1,len(r)+1)]
        # lb = random.sample(range(1,5), 6)
        # l = []
        # for i in r:
        #     l.append(Books.objects.filter(pk__in=r))
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'random_books': zip(Books.objects.filter(pk__in=r), cnt),
            'english_books': Books.objects.filter(language='English')[:6],
            'latest_books':  Books.objects.order_by('year')[lb-5:lb],
        })
        return context

    def get_queryset(self):
        r = random.sample(range(1, (len(Books.objects.all()))), 5)
        return Books.objects.all()[0:5]


class BooksView(generic.ListView):
    template_name = 'all_books.html'

    def get_queryset(self):
        r = random.sample(range(1, (len(Books.objects.all()))), 5)
        return Books.objects.all()


class LanguageView(generic.ListView):
    template_name = 'language.html'

    def get_context_data(self, **kwargs):
        l = [definition.encode("utf8") for definition in Books.objects.values_list('language', flat=True).distinct().order_by('language')]
        tcnt=[]
        tcnt1=[]
        count=[i for i in range(len(l))]
        for i in range(len(l)):
            tcnt1.append(Books.objects.filter(language=l[i]))
            tcnt.append(Books.objects.filter(language=l[i]).count())
        context = super(LanguageView, self).get_context_data(**kwargs)
        context.update({
            'books_cnt': zip(l, tcnt),
            'tcnt_list': zip(tcnt1, count),
            'test_list': Books.objects.filter(language='English')
        })
        return context

    def get_queryset(self):
        return [definition.encode("utf8") for definition in Books.objects.values_list('language', flat=True).distinct().order_by('language')]
        # tarr=set(l)
        # return tarr


class AuthorView(generic.ListView):
    template_name = 'author.html'

    def get_context_data(self, **kwargs):
        a = [definition.encode("utf8") for definition in Books.objects.values_list('author', flat=True).distinct().order_by('author')]
        acnt=[]
        count=[i for i in range(len(a))]
        for i in range(len(a)):
            acnt.append(Books.objects.filter(author=a[i]).count())
        context = super(AuthorView, self).get_context_data(**kwargs)
        context.update({
            'author_cnt': zip(a, acnt),
        })
        return context

    def get_queryset(self):
        return [definition.encode("utf8") for definition in Books.objects.values_list('author', flat=True).distinct().order_by('author')]


class DetailView(generic.DetailView):
    model = Books
    template_name = 'details.html'


class LanguageDetailView(generic.DetailView):
    model = Books
    template_name = 'book_lang.html'

    def get_queryset(self):
        l = [definition.encode("utf8") for definition in
             Books.objects.values_list('language', flat=True).distinct().order_by('language')]
        tcnt = []
        for i in range(len(l)):
            tcnt.append([Books.objects.filter(language=l[i])])
        return tcnt