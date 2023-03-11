from django.shortcuts import get_object_or_404
from django.shortcuts import render

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj
        }
        return render(request, self.template, context)