from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Store
from django.views.generic import ListView, DetailView

# Create your views here.
def StoreView(request, StoreName):
	store = get_object_or_404(Store, store_name=StoreName)
	return render(request, 'stores.html', {'store': store})


# Create your views here.
class StoreListView(ListView):
	model = Store
	template_name = 'stores_topups.html'
	paginate_by = 4

	def get_queryset(self):
		if self.kwargs.get('tabulator'):
			#hay que cambiar el nombre del campo a 'tabulator' en tabulators
			queryset = self.model.objects.filter(tabulator__tab_zone__contains=self.kwargs['tabulator'])
		else:
			queryset = super(StoreListView, self).get_queryset()
		return queryset

class StoreDetailView(DetailView):
	model = Store
	template_name = "store_detail.html"
	slug_url_kwarg = "store_name"
	slug_field = "store_name"
