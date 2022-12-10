# from django.shortcuts import render

# # Create your views here.

# from django.http import JsonResponse

#crud operations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import farmerSerializer
from .models import farmer

from django.shortcuts import render

#pdf generation
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from django.views.generic import ListView


@api_view(['GET'])
def getRoutes(request):
    routes = [
    {
        'Endpoint':'./jai_kisaan/',
        'method':'GET',
        'body': None,
        'description': 'Return an array'

    },
    {
        'Endpoint':'./jai_kisaan/create/',
        'method':'POST',
        'body': {'body':""},
        'description': 'Create new data'
        
    },
    ]
    return Response(routes)

@api_view(['GET'])
def getFarmer(request):
    farmers = farmer.objects.all()
    serializer = farmerSerializer(farmers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOneFarmer(request,primary_key):
    one_farmer = farmer.objects.get(id=primary_key)
    serializer = farmerSerializer(one_farmer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addFarmer(request):
    data=request.data

    addfarmer=farmer.objects.create(
        body=data['body']
    )

    serializer = farmerSerializer(addfarmer,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateFarmer(request, primary_key):
    data=request.data

    updatefarmer=farmer.objects.get(id=primary_key)
    serializer = farmerSerializer(updatefarmer,data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteFarmer(request, primary_key):
    deletefarmer=farmer.objects.get(id=primary_key)
    deletefarmer.delete()

    return Response("farmer was deleted")

@api_view(['GET'])
def render_pdf_view(request,primary_key):
    template_path = 'pdf1.html'
    # context = {'myvar': 'this is your template context',
    # }
    obj=farmer.objects.get(id=primary_key)
    context={
        'name': obj.name
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if we have to download the pdf, use the below line
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #view the report
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def farmer_render_pdf(request, *args, **kwargs):
    pass


class farmer_list(ListView):
    model=farmer
    template_name='main.html'

@api_view(['GET'])
def all_details_report(request, primary_key):
    farmers=farmer.objects.get(id=primary_key)
    print(farmers)

    context={'details' : farmers}

    return render(request, 'main.html', context)









