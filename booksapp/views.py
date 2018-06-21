# -*- coding: utf-8 -*-
from django.views import generic
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

    def get_queryset(self):
        return Books.objects.all()
