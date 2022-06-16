from . import models
from . import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('title', 'product_text', 'price', 'author',
                  'create_date', 'published_date', )
        labels = {'title': '商品名', 'product_text': '説明文', 'price': '値段',
                  'author': 'ユーザー', 'create_date': '作成日', 'published_date': '公開日', }
