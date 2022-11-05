from django.shortcuts import redirect, render
from .models import Concert,QticketsSalesInfo
from .forms import ConcertForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages

# Create your views here.

def home(request):
    context = {

    }
    
    template = "core/index.html"
    return render(request,template,context)

# def sell(request):
#     context = {
#         list_sell : QticketsSalesInfo.objects.all().order_by("id"),

#     }
    
#     template = "core/sell.html"
#     return render(request,template,context)

class SellListView(ListView):
    model = QticketsSalesInfo
    template_name = "core/sell.html"

def target(request):
    context = {

    }
    
    template = "core/target.html"
    return render(request,template,context)

class CustomSuccessMessage:
    @property
    def success_msg(self):
        return False
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

class ConcertCreateView(CustomSuccessMessage, CreateView):
    model = Concert
    template_name = 'core/concert.html'
    form_class = ConcertForm
    success_url = reverse_lazy('concert')
    success_msg = 'Запись создана'
    def get_context_data(self, **kwargs):
        kwargs['list_concert'] = Concert.objects.all().order_by("id")
        return super().get_context_data(**kwargs)


class ConcertUpdateView(CustomSuccessMessage, UpdateView):
    model = Concert
    template_name = 'core/concert.html'
    form_class = ConcertForm
    success_url = reverse_lazy('concert')
    success_msg = 'Объект обновлен'
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


def delete_page(request,pk):
    get_concert = Concert.objects.get(pk = pk)
    get_concert.delete()
    return redirect(reverse('concert'))

# class ConcertDeleteView(DeleteView):
#     model = Concert
#     template_name = 'core/concert.html'
#     success_url = reverse_lazy('concert')


# def update_page(request,pk):
#     success_update = False
#     get_concert = Concert.objects.get(pk = pk)
#     if request.method == 'POST':
#         form = ConcertForm(request.POST, instance = get_concert)
#         if form.is_valid():
#             form.save()
#             success_update = True

#     context = {
#         'get_concert' : get_concert,
#         'update': True,
#         'form':ConcertForm(instance = get_concert),
#         'success_update':success_update
#     }
    
#     template = "core/concert.html"
#     return render(request,template,context)




# def concert(request):
#     success = False 
#     if request.method == 'POST':
#         form = ConcertForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True

#     context = {
#         "list_concert" : Concert.objects.all().order_by("id"),
#         "form" : ConcertForm,
#         "success" : success
#     }
    
#     template = "core/concert.html"
#     return render(request,template,context)