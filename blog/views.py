from django.shortcuts import render
from django.views.generic import View

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        return render (request=  'blog_list.html', context)
