from typing import Any
from django.http.response import HttpResponse as HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.base import TemplateView
from main_page.models import BookModel

from main_page.forms import BookForm

from django.http import HttpRequest, HttpResponseRedirect

from django.urls import reverse_lazy

# Create your views here.



class IndexView(ListView):
    template_name = 'main_page/index.html'
    model = BookModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Books'
        context['book_list'] = BookModel.objects.all()
        return context


class BookDetailView(View):
    def get(self, request, book_id=None):
        if book_id:
            book_get = BookModel.objects.get(id=book_id)

            context = {
                'book_name': book_get.book_name,
                'book_author': book_get.book_author,    
                'book_image': book_get.book_img.url,
                'form': BookForm(initial={'book_name': book_get.book_name, 'book_author': book_get.book_author, 'book_image': book_get.book_img}),
                'book_id': book_id,
                'title': book_get.book_name
            }

        return render(request, 'main_page/book_go.html', context)

    def post(self, request, book_id=None):
        if book_id:
            book = BookModel.objects.get(id=book_id)
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                return redirect(request.META.get('HTTP_REFERER'))

class AddBookView(TemplateView):
    template_name = 'main_page/add_book.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['form'] = BookForm
        context['title'] = 'Add book'
        return context
    
    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            print(form.errors)


def del_book(request, book_id):
    try:
        book = BookModel.objects.get(id=book_id)
        book.delete()
        return HttpResponseRedirect(reverse_lazy('index'))
    except:
        return HttpResponseNotFound("<h2>Person not found</h2>")