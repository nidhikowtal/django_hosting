from django.urls import path
from . import views 

urlpatterns = [
    path('', views.getRoutes),
    path('farmers/',views.getFarmer),
    path('farmers/addFarmer/', views.addFarmer),
    path('farmers/<str:primary_key>/update/', views.updateFarmer),
    path('farmers/<str:primary_key>/delete/', views.deleteFarmer),
    path('farmers/<str:primary_key>/',views.getOneFarmer),

    path('test-view/<str:primary_key>/',views.render_pdf_view),
    path('report/<str:primary_key>/',views.all_details_report),
    #path('report/',views.farmer_list.as_view())
]