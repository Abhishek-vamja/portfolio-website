from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class PortfolioWebSite():
    
    def home_view(request):
        return render(request, 'index.html')

    def about_view(request):
        return render(request, 'about.html')
    
    def contact_view(request):
        return render(request, 'contact.html')
    
    def service_view(request):
        return render(request, 'services.html')