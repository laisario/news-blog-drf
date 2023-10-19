from django import forms
from news.models.category_model import Categories
from news.models.news_model import News


class CreateCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, new):
        return "%s" % new.name


class CreateNewModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da Imagem"
        self.fields["categories"] = CustomMMCF(
            queryset=Categories.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )
