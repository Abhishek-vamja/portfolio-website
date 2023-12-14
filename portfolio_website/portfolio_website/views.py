from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class PortfolioWebSite():
    
    def home_view(request):
        project_obj = Project.objects.all()
        context = {
            'project': project_obj,
        } 

        return render(request, 'index.html', context)

    def about_view(request):
        return render(request, 'about.html')
    
    def contact_view(request):
        return render(request, 'contact.html')
    
    def service_view(request):
        return render(request, 'services.html')