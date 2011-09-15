from django import forms
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from flatblocks.models import FlatBlock
 
class FlatBlockForm(forms.ModelForm):
    lang_code = forms.ChoiceField(label=_("Language"), choices=settings.LANGUAGES)

    class Meta:
        model = FlatBlock

class FlatBlockAdmin(admin.ModelAdmin):
    form = FlatBlockForm
    ordering = ['slug',]
    list_display = ('slug', 'header', 'lang_code', 'site')
    search_fields = ('slug', 'header', 'content')

admin.site.register(FlatBlock, FlatBlockAdmin)
