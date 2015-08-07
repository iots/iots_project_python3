from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from iots_app.models import Title,Person,PushModel,ShowEndAlive,ShowPushMessage
from iots_app.forms import PushForm,PushFormAlias
from django.template import Context, loader
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
import json


# Create your views here.
def online(request):
    page = int(request.GET.get('page',1))
    pe = 4
    pf = 5
    pview = pe+pf+1
    onlinelist = ShowEndAlive.objects.all()
    try:
        p = Paginator(onlinelist,10)
        if page <= 0:
            page = 1
        if page > p.num_pages:
            page = p.num_pages
        pagelist=[]
        pagelist = p.page(page).object_list
    except:
        print("p",p)
        print("pagelist",pagelist)
    if page > pf:
        page_range=p.page_range[page-pf-1:page+pe]
    else:
        page_range=p.page_range[0:pview]

    latest_poll_list = Title.objects.all()#('-pub_date')[:5]
    template = loader.get_template('frame/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return render(request,"page/onlinelist.html",locals())

def testdb(request):
    push_history = ShowPushMessage.objects.all()[0:5]
    for l in push_history:
        print (l.sent_message,l.sent_url)

def history(request):
    page = int(request.GET.get('page',1))
    pe = 4
    pf = 5
    pview = pe+pf+1

    historylist = ShowPushMessage.objects.all()
    try:
        p = Paginator(historylist,10)
        if page < 0:
            page = 1
        if page > p.num_pages:
            page = p.num_pages
        prepage = page-1
        nextpage = page+1
        pagelist=[]
        pagelist = p.page(page).object_list
    except:
        print("except")
    if page > pf:
        page_range=p.page_range[page-pf-1:page+pe]
    else:
        page_range=p.page_range[0:pview]
    latest_poll_list = Title.objects.all()#('-pub_date')[:5]
    template = loader.get_template('frame/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return render(request,"page/historylist.html",locals())


def index(request):
    latest_poll_list = Title.objects.all()#('-pub_date')[:5]
    template = loader.get_template('frame/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })

    return HttpResponse(template.render(context))

def detail(request):
    latest_poll_list = Title.objects.all()
    template = loader.get_template('detail.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))

def home(request):
    q = Person.objects.filter(name='online')

    if len(q)!=0:  #query success.
      context = {'number':q[0].number}
    else:  #result queried is null.
      context = {'number':'result queried is null, maybe table no item.',}
    latest_poll_list = Title.objects.all()
    template = loader.get_template('detail.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return render(request, 'home/home.html', context)

def query(request):
    q_online = Person.objects.filter(name='online')
    print (q_online,len(q_online))
    if len(q_online)!=0:  #query success.
      data_online = q_online[0].number
    else:  #result queried is null.
      data_online = 'result queried is null, maybe table no item.'

    q_sent = Person.objects.filter(name='sent')
    if len(q_sent)!=0:  #query success.
      data_sent = q_sent[0].number
    else:  #result queried is null.
      data_sent = 'result queried is null, maybe table no item.'

    q_read = Person.objects.filter(name='read')
    if len(q_read)!=0:  #query success.
      data_read = q_read[0].number
    else:  #result queried is null.
      data_read = 'result queried is null, maybe table no item.'
    '''
    result_queried = str(data_online)+':' +str(data_sent)+ ':' +str(data_read)
    return HttpResponse(result_queried)
    '''
    result_queried = {'online':data_online,'sent':data_sent,'read':data_read}
    encodedjson = json.dumps(result_queried, sort_keys=True, indent=4) #transform string into object:encodedjson.

    return HttpResponse(encodedjson)

@csrf_protect
def PushView(request):
    if request.method == 'POST':
        form = PushForm(request.POST)
        if form.is_valid():

            #use request.POST.get method
            msg = request.POST.get('push_message','')
            url = request.POST.get('push_url','')
            #print("[DEBUG] Request.POST.get->msg:%s,url:%s" % (msg,url))
            #print("[DEBUG] PUSH_MESSAGE : %s" % form['push_message'].value())

            #obj = PushModel.objects.get_or_create(push_message=msg,push_url=url)
            try:
                PushModel.objects.get(push_message=msg,push_url=url)
                print("[DEBUG] already in.")
            except PushModel.DoesNotExist:
                obj = PushModel(push_message=msg,push_url=url)
                obj.save()
            finally:
                return HttpResponseRedirect("/work/PushList/")
        else:
            print("Forms Arguments Error!!!")
    else:
        form = PushForm(initial={'push_message':'Hi,Everyone','push_url':'http://www.nfschina.com'})
    latest_poll_list = Title.objects.all()#('-pub_date')[:5]
    template = loader.get_template('frame/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    context_instance=RequestContext(request)
   # return render_to_response("forms/push.html",{'form':form},context_instance=RequestContext(request))
    return render(request,"forms/push.html",locals())

def PushList(request):
    #ret = PushModel.objects.filter(push_message__icontains='Hi')
    ret = PushModel.objects.all()
    #print(ret)
    return render_to_response("forms/PushList.html",{'ret':ret})

