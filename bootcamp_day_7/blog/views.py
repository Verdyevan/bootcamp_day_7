from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.serializers import MahasiswaSerializer, DaftarKuliahSerializer


@api_view(["GET"])
def Mahasiswa(request):
    queryset = Mahasiswa.objects.all()
    serialized = MahasiswaSerializer(queryset, many=True)
    return Response(serialized.data)

@api_view(["GET"])
def DaftarKuliah(request):
    queryset = DaftarKuliah.objects.all()
    serialized = DaftarKuliahSerializer(queryset, many=True)
    return Response(serialized.data)
