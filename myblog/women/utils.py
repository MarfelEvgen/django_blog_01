from .models import *

class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['cats'] = cats
        return context