from django.shortcuts import render
from testapp.models import Employee
def index_info(request):
    return render(request,'testapp/index.html')

def history_info(request):
    return render(request,'testapp/base.html')

def timing_info(request):
    my_dict = {'head_msg': 'VALUABLE INFORMATION ABOUT DARGA',
               'sub_msg1': 'Darga Timings Morning:5.30 to 10.30AM',
               'sub_msg2': 'Evening timings are 5.30 PM to 10.PM',
               'sub_msg3': 'FRIDAY Timing:1.PM to 2.30PM',
               'photo':'static/HAZRAT.jpg'}

    return render(request,'testapp/history.html',context=my_dict)


def manage_info(request):
    my_dict = {'head_msg': 'ResponsiBilities Of Darga ManagingDepartment',
               'sub_msg1': '',
               'sub_msg2': 'Evening timings are 5.30 PM to 10.PM',
               'sub_msg3': 'FRIDAY Timing:1.PM to 2.30PM',
               'photo': 'static/HAZRAT.jpg'}
    return render(request,'testapp/manage.html')

def model_view(request):
    emp=Employee.objects.all()
    return render(request,'testapp/model.html',{'emp':emp})