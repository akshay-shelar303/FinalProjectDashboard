from django.shortcuts import render

def dashboardView(request):
    return render(request,"DashboardApp/base.html")