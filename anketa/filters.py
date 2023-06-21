from django_filters import rest_framework as filters
from .models import YourModel


class YourModelFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name='tags', method='filter_tags')

    def filter_tags(self, queryset, name, value):
        tags = value.split(',')  # Если хештеги разделены запятыми
        return queryset.filter(tags__name__in=tags)

    class Meta:
        model = YourModel
        fields = ('tags',)