from django.shortcuts import render, HttpResponse, redirect
from todolist1.models import List
from index_var_read import read_file
from index_var_write import write_file
from django.contrib import messages

# Create your views here.
def index_page(request):
    b = 0
    entry_check = 0 != List.objects.all().values().count()
    values1 = List.objects.all().values()
    values2 = 0 != List.objects.filter(check_task = True).count()
    value3 = [False,False]
    field_no_fetch = -1

    try:
        field_no_ls = list(map(int,read_file("field_no.txt").split(" ")))
    except:
        field_no_ls = []


    if request.method == "POST":
        value3 = [False,False]
        if request.POST['form_id'] == 'add_list':
            t = request.POST.get('task')
            d = request.POST.get('desc')
            l1 = List(field_no = int(read_file("index_v.txt")),task = t,desc = d,check_task=False)
            l1.save()
            field_no_ls.append(int(read_file("index_v.txt")))
            new_text = ""
            for i in field_no_ls:
                new_text += str(i)+" "
            new_text = new_text.strip()
            write_file("field_no.txt", new_text)
            messages.success(request, 'Task Added')
            write_file("index_v.txt",int(read_file("index_v.txt"))+1)
        
        elif request.POST['form_id'] == 'list':
            b = []
            for i in field_no_ls:
                b.append(request.POST.get(str(i)))
            for i in range(len(b)):
                if(b[i] == None):
                    update = List.objects.get(field_no = field_no_ls[i])
                    update.check_task = False
                    update.save()
                else:
                    update = List.objects.get(field_no = field_no_ls[i])
                    update.check_task = True
                    update.save()
            values2 = 0 != List.objects.filter(check_task = True).count()

        elif request.POST['form_id'] == 'delete_list':
            try:
                field_no_ls = list(map(int,read_file("field_no.txt").split(" ")))
            except:
                field_no_ls = []
            if(List.objects.all().values()):
                b = []
                for i in field_no_ls:
                    b.append(request.POST.get(("dc"+str(i))))
                for i in range(len(field_no_ls)):
                    if(b[i] == None):
                        pass
                    else:
                        update = List.objects.get(field_no = b[i])
                        update.delete()
                        field_no_ls = []
                        for i in List.objects.all().values():
                            field_no_ls.append(i.get('field_no'))
                        new_text = ""
                        for i in field_no_ls:
                            new_text += str(i)+" "
                        new_text = new_text.strip()
                        write_file("field_no.txt", new_text)
                        write_file("field_no.txt", new_text)
            # return HttpResponse(b)
            temp_list = b[0]
            if(b[0]!=None):
                messages.warning(request, 'Task Deleted')
            else:
                messages.warning(request, 'Select a Task in Delete Item Menu and then Click Delete')

        elif request.POST['form_id'] == 'select_delete_list':     
            b = []
            update = List.objects.filter(check_task = True).values_list('field_no',flat=True)
            for i in update:
                obj = List.objects.get(field_no = i)
                obj.delete()
            field_no_ls = []
            for i in List.objects.all().values():
                field_no_ls.append(i.get('field_no'))
            new_text = ""
            for i in field_no_ls:
                new_text += str(i)+" "
            new_text = new_text.strip()
            write_file("field_no.txt", new_text)
            messages.info(request, 'Completed Task Removed')

        elif request.POST['form_id'] == 'edit_list':
            fl_id = request.POST['form_id_data']
            update = List.objects.get(field_no = fl_id)
            update.task = request.POST['task']
            update.desc = request.POST['desc']
            update.save()
            pass
    
    lst = []
    if(not entry_check):
        lst = [entry_check]
    else:
        lst = []
    context = {
    "val":values1,
    "val2":values2,
    "fln":field_no_fetch,
    "ec":entry_check,
    "en":List.objects.all().values().count(),
    "list_n":lst,
    }        

    return render(request,'index.html',context)

# def set_increment_0(request):
#     write_file("index_v.txt",0)
#     return HttpResponse("Increment set to Zero")
# Set ID no to 0 using the above function
# Uncomment in urls to use the avove function
