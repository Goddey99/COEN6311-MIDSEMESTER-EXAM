from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PostBookForm, SearchBookForm
from .models import Textbook

def landing_page(request):
    post_form = PostBookForm()
    search_form = SearchBookForm()

    if request.method == 'POST':
        if 'post_book' in request.POST:
            post_form = PostBookForm(request.POST)
            if post_form.is_valid():
                post_form.save()
                return redirect('/')
        elif 'search_book' in request.POST:
            search_form = SearchBookForm(request.POST)
            if search_form.is_valid():
                course_code = search_form.cleaned_data['course_code']
                return redirect(reverse('search_results', args=[course_code]))

    return render(request, 'books/landing.html', {
        'post_form': post_form,
        'search_form': search_form
    })

def search_results(request, course_code):
    results = Textbook.objects.filter(course_code__iexact=course_code)
    return render(request, 'books/search_results.html', {
        'course_code': course_code,
        'results': results
    })
