from django.shortcuts import render, HttpResponse
from index.__init__ import mapp
from index.models import Tokenlist
import time
import base64

# Create your views here.


def gettk(request):
    pass
    if request.method == 'GET':
        return HttpResponse('This is a POST page.')
    elif request.method == 'POST':
        uid = request.POST['uid']
        Tokenlist.objects.filter(id=uid).delete()
        tk = str(base64.b64encode(
            (str(time.time())+str(uid)+str(time.time())).encode('utf-8')))[:25]
        Tokenlist.objects.create(id=uid, token=tk)
        # print(tk)
        return HttpResponse(tk)

    else:
        pass


def getboard(request):
    ret = st = nd = rd = ""
    for y in range(0, 999):
        for x in range(0, 599):
            st, nd, rd = [str(hex(mapp[x][y][0]))[2:], str(
                hex(mapp[x][y][1]))[2:], str(hex(mapp[x][y][2]))[2:]]
            while (st.__len__() < 2):
                st = "0"+st
            while (nd.__len__() < 2):
                nd = "0"+nd
            while (rd.__len__() < 2):
                rd = "0"+rd
            ret += st + nd + rd
        ret += '\n'
    # print(ret)
    return HttpResponse(ret)


def checktoken(uid, token):
    dtlist = Tokenlist.objects.filter(id=uid)
    for data in dtlist:
        try:
            if (str(data.token) == token):
                return 1
        except Exception as ex:
            return 0
    return 0


def paintboard(request):
    if request.method == 'GET':
        return HttpResponse('This is a POST page.')
    elif request.method == 'POST':
        uid = request.POST['uid']
        token = request.POST['token']
        if (checktoken(uid, token)):
            mapp[int(request.POST['y'])][int(request.POST['x'])] = [int(request.POST['color'][0:2], 16), int(
                request.POST['color'][2:4], 16), int(request.POST['color'][4:6], 16)]
            with open('index/mapp.py', 'w',) as mapppy:
                mapppy.write("mapp = "+str(mapp))
            print(request.POST['uid'] + " paint " +
                  request.POST['color'] + " at " + request.POST['x'] + " " + request.POST['y'])
            return HttpResponse("{\"status\":200,\"data\":\"done\"}")
        return HttpResponse("{\"status\":400,\"data\":\"Token Error\"}")

        # return HttpResponse(request.POST['uid'] + " paint " + request.POST['color'] + " at " + request.POST['x'] + " " + request.POST['y'])
    else:
        pass


def index(request):
    return render(request, "index.html")
