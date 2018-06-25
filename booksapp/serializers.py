from rest_framework.serializers import ModelSerializer
from booksapp.models import Books


class BooksViewSet(ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'
