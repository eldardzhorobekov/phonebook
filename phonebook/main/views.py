from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator
from main.models import PhonebookItem


class HomeView(ListView):
    paginate_by = 10
    model = PhonebookItem
    
    def get_queryset(self):
        query = self.request.GET.get('q','')

        object_list = PhonebookItem.objects.filter(
            Q(name__icontains=query) | Q(phone_number__icontains=query)
        )

        return object_list