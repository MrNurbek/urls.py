import django_filters
from page.models import *


class TableFilter(django_filters.FilterSet):
    group_name = django_filters.ModelChoiceFilter(queryset=GroupName.objects.all())

    # group_name = django_filters.BooleanFilter(field_name='group_name')
    class Meta:
        model = Table
        fields = ["group_name", "week"]
