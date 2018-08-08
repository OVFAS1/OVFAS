from django.shortcuts import render
from .models import Student
import re

# Create your views here.
def index(request):
    return render(request, 'ov/index.html')


def outingform(request):
    return render(request,'ov/outingform.html')


def registration(request):
    if(request.method=="POST"):
        registration_no=request.POST.get('registration_no')
        registration_no=registration_no.title()
        try:
            student=Student.objects.get(registration_no=registration_no)
            context={'student_name':student.name}
            return render(request,'ov/outingform.html',context)
        except:
            context={"error_message":"Invalid registration number"}
            return render(request,'ov/registration.html',context)
        

    return render(request,'ov/registration.html')


def studentimport(request):
    if request.method=="POST":
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            context={"error_message":["File is not csv type"]}
            return render(request, 'ov/studentimport.html', context)
        if csv_file.multiple_chunks():
            context={"error_message":["Uploaded file is too big."]}
            return render(request, 'ov/studentimport.html', context)
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")[1:]
        updated=[]
        for line in lines:
            inf=''
            fields = line.split(",")
            if('' in fields):
                fields.remove('')
            if(len(fields)==2):
                registration_no=fields[0].rstrip('\r').upper()
                name=fields[1].rstrip('\r').title()
                try:
                    student=Student.objects.get(registration_no=registration_no)
                    inf="Registration number already exists"
                    updated.append(inf)
                except:
                    validate=re.match(r'\d{2}[a-zA-Z]{3}\d{4}',registration_no)
                    if(validate):
                        student=Student(registration_no=registration_no,name=name)
                        student.save()
                        inf="Registration number:--"+registration_no
                    else:
                        inf="Invalid registration number:--"+registration_no+" at line number:-"+str(lines.index(line)+1)
                    updated.append(inf)
            else:
                updated.append("Got unexpected garbage value or unprocessed value at line number:->"+str(lines.index(line)+1))

        updated.append("-----------------Processing Completed-----------------")
        context={"error_message":updated
        }
        return render(request, "ov/studentimport.html", context)    

    return render(request,'ov/studentimport.html')