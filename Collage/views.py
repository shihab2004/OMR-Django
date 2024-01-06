from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from time import sleep
import cv2
import numpy as np
from django.views.generic import ListView
from Collage.models import *
from .ImageProcessor.crop_sheet import crop_sheet
import base64
from django.contrib import messages
from Collage.forms import *
from django.conf import settings
import os
import pandas as pd
import urllib.parse as url_parse
# Create your views here.


@login_required(login_url="/auth/login")
def home(request):
    
    return render(request,"index.html")





from Collage.ImageProcessor.calculator import calculate_imgage
class CreateTemplate(View):
    
    def get(self,request,*args, **kwargs):
        return render(request,"create-template.html")
    
    
    def calculator_result(self,exam_sheet,achieve_id):
        
        file = AnswerSheet.objects.get(pk=achieve_id).result_sheet
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8),-1)
        ans_sheet = crop_sheet(img)
        
        return calculate_imgage(ans_sheet,exam_sheet)
    
    
    def post(self,request,*args, **kwargs):
        if request.GET.get("img_lookUp"):
            context = {}
            
            file = request.FILES['file']
            
            img = cv2.imdecode(np.frombuffer(file.read(), np.uint8),-1)
            img = crop_sheet(img)
            
            
            if request.GET.get("result"):
                context = self.calculator_result(img, int(request.GET.get("achieve_id")) )
            
            retval, buffer = cv2.imencode('.png', img)
            base64_img = base64.b64encode(buffer).decode()
            context.update({"img_b64":base64_img})

            return JsonResponse(context)
        
        form = AnswerSheetForm(request.POST,files=request.FILES)
        if form.is_valid():
            messages.success(request, "New Template Created.")
            form.save()
            return redirect("/")
        else:
            messages.error(request, "Invalid Form.")
            
        self.get(request,*args, **kwargs)
        
    


def about(request):
    return render(request,"about.html")



class Achieve(ListView):
    queryset = AnswerSheet.objects.all().order_by("-pk")
    template_name = "achieve.html"
    


from django.http import HttpResponse
class StudentsList(ListView,View):
    queryset = StudentResultSheet.objects.all()
    template_name = "student-list.html"
    
    def get_queryset(self,*args, **kwargs):
        return AnswerSheet.objects.get(pk=self.kwargs['pk']).students.all()
    
    def get(self, request, *args, **kwargs):
        if request.GET.get("q"):

             data = {}
             for i in request.GET.get('q').split(','):
                 try:
                     data.update({i:None})
                 except:pass
             
             
             return self.download_csv(data.items())
             
        return super().get(request, *args, **kwargs)
    
    
    
    
    def post(self,request,*args, **kwargs):
        
        
        
        
        post_data = dict(request.POST.copy())
        del post_data['csrfmiddlewaretoken']
        url = "-".join([key for key, val in post_data.items()])
        # 
        # )
        # for  key , val in :
        #         q_data += (str(key) + ",")
        
        print(post_data.items())
        print(url)
        if request.GET.get("download"):
            
            
            link =  request.build_absolute_uri('/')[:-1] + "/download/"  + url +"/"
            print(link)
            
            return render(request,'share-download.html',{"link":link,"sms":"Student Results"})
        
        
        return redirect(f"/download/{url}/")
        
        
        
        



def studentDetails(request,pk):
    return render(request,"student.html",{
        "student":StudentResultSheet.objects.get(pk=pk),
        "prefix":"Details",
        "read_only":True
    })




class StudentAdd(View):
     
     
    def get(self,request,*args, **kwargs):
        return render(request,"student.html",{
            "prefix":"Add",
            "read_only":False,
            "pk":kwargs['pk']
        })
        
    
    def post(self,request,*args, **kwargs):
   
        print(request.POST)
        print(request.FILES)
        form = StudentResultSheetForm(request.POST,files=request.FILES)
        if form.is_valid():
            messages.success(request, "New Student Created.")
            student= form.save()
            
            ans_room = AnswerSheet.objects.get(pk=kwargs['pk'])
            ans_room.students.add(student)
            ans_room.save()
            
             
            return redirect(f"/achieve/{kwargs['pk']}/students/")
        else:
            messages.error(request, "Invalid Form.")
            
        self.get(request,*args, **kwargs)
     
     
        # form = StudentResultSheet(request.POST,request.FILES)
        # if form.is_valid():
        #         messages.success(request, "New Template Created.")
        #         form.save()
        #         return redirect("/")
            
        # else:
        #         messages.error(request, "Invalid Form.")
    
    







def downloadStudentResultSheet(request,slug):
        df = pd.DataFrame()
        
        for key in slug.split("-"):
            try:
                a = StudentResultSheet.objects.filter(pk=int(key)).values(
                    "name", "subject","dept","batch","section","examiner","code","stu_id","physics","chemistry","math","english","analytical","result"
                )[0]
      
                df = df._append(a, ignore_index=True)
            except Exception as e:
                pass
              
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="student_result.csv"'
        df.to_csv(path_or_buf=response, index=False)  
        return response





