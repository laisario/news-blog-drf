from django.shortcuts import redirect, render
from news.models.news_model import News
from django.shortcuts import get_object_or_404
from news.forms import CreateCategoryModelForm
from news.forms import CreateNewModelForm
from news.models.category_model import Categories


def index(request):
    context = {"news": News.objects.all()}

    return render(request, "home.html", context)


def news_details(request, id):
    new = get_object_or_404(News, pk=id)
    context = {"new": new, "categories": new.categories.all()}
    return render(request, "news_details.html", context)

def create_category(request):
    form = CreateCategoryModelForm()

    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)

def create_new(request):
    form = CreateNewModelForm()

    if request.method == "POST":
        form = CreateNewModelForm(request.POST)

        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "news_form.html", context)