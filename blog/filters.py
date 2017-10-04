from .models import Document
import django_filters

class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = {'title':['icontains'], 'genre':['icontains'], 'author':['icontains'], }
