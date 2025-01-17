from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'index.html', context)
    
#aqui lo que hicimos fue crear una vista de clase donde el contexto fue el template con el archivo index.html