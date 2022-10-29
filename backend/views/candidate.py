from django.shortcuts import render
from backend.serializers.candidates import CandidatesSerializer,CandidatesfoSerializer
# Create your views here.
from rest_framework import viewsets,permissions,filters
from backend.models.candidates import Candidates
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
from rest_framework.response import Response
import codecs

fs=FileSystemStorage(location='tmp/')

class CandidateModelViewSet(viewsets.ModelViewSet):
    queryset=Candidates.objects.all()
    serializer_class=CandidatesSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','EnrollmentNo']
    search_fields=['name','EnrollmentNo']
    odering_fields=['name','EnrollmentNo']
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    @action(detail=False,methods=['POST'])
    def upload_data_to_model(self,request):
        file=request.FILES.get("file")
        SId=request.POST.get("SId")
        RId=request.POST.get("RId")
        # content=file.read()
        # file_content=ContentFile(content)
        # file_name=fs.save("_tmp.csv",file_content)
        # tmp_file=fs.path(file_name)
        # csv_file=open(tmp_file,errors="ignore")
        # reader=csv.reader(csv_file)
        # next(reader)
        reader=csv.DictReader(
            codecs.iterdecode(file,"utf-8"),delimiter=","
        )
        data=list(reader)
        serializer=self.serializer_class(data=data,many=True)
        serializer.is_valid(raise_exception=True)
        candidate_list=[]
        for row in serializer.data:
            candidate_list.append(
                Candidates(
                    name=row['name'],
                    EnrollmentNo=row['EnrollmentNo'],
                    branch=row['branch'],
                    EmailId=row['EmailId'],
                    phone=row['phone'],
                    role=row['role'],
                    year=row['year'],
                    RId=RId,#['RId'],
                    SId=SId,#['SId'],
                    cg=row['cg'],
                    StudentId=row['StudentId'],

                )
            )
            
            
        Candidates.objects.bulk_create(candidate_list)
        return Response("registration successful")
        