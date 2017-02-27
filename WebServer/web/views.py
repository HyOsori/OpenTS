from django.shortcuts import render
from django.http import JsonResponse
'''
from web.singleton import code_dic
from web.models import Data
import win32com.client
import pythoncom
'''
# Create your views here.
from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')

def result(request):
    return render_to_response('result.html')

def getshcode(request):
    return JsonResponse({
        'status': 'Success',
        'shcode': '12345'
    })

    '''
    keyword = request.GET['keyword']

    if keyword in code_dic == True:
        return JsonResponse({
            'status' : 'Success',
            'shcode' : code_dic[keyword]
        })
    #If hname is in key
    else:
        return JsonResponse({
            'status': 'Failure',
            'shcode': -1
        })
    #If hname is not in key
    '''
def crawl(request):
    return JsonResponse({})

    '''
    shcode = request.GET['shcode']

    class XAQueryEventHandlerT1305:
        query_state = 0

        def OnReceiveData(self, code):
            XAQueryEventHandlerT1305.query_state = 1
    #기간별 주가 조회
    instXAQueryT1305 = win32com.client.DispatchWithEvents("XA_Dataset.XAQuery", XAQueryEventHandlerT1305)
    instXAQueryT1305.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1305.res"
    # Create instance : 기간별 주가 조회

    instXAQueryT1305.SetFieldData("t1305InBlock", "shcode", 0, shcode)
    instXAQueryT1305.SetFieldData("t1305InBlock", "dwmcode", 0, 1)
    instXAQueryT1305.SetFieldData("t1305InBlock", "cnt", 0, 100)
    # Default amount : 100

    instXAQueryT1305.Request(0)
    while XAQueryEventHandlerT1305.query_state == 0:
        pythoncom.PumpWaitingMessages()

    count = instXAQueryT1305.GetBlockCount("t1305OutBlock1")
    for i in range(count):
        stock_data = Data()
        stock_data.shcode = instXAQueryT1305.GetFieldData("t1305OutBlock1", "shcode", i)
        stock_data.date = instXAQueryT1305.GetFieldData("t1305OutBlock1", "date", i)
        stock_data.open = instXAQueryT1305.GetFieldData("t1305OutBlock1", "open", i)
        stock_data.high = instXAQueryT1305.GetFieldData("t1305OutBlock1", "high", i)
        stock_data.low = instXAQueryT1305.GetFieldData("t1305OutBlock1", "low", i)
        stock_data.close = instXAQueryT1305.GetFieldData("t1305OutBlock1", "close", i)
        stock_data.sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sign", i)
        stock_data.change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "change", i)
        stock_data.diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff", i)
        stock_data.volume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "volume", i)
        stock_data.diff_vol = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff_vol", i)
        stock_data.chdegree = instXAQueryT1305.GetFieldData("t1305OutBlock1", "chdegree", i)
        stock_data.sojinrate = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sojinrate", i)
        stock_data.changerate = instXAQueryT1305.GetFieldData("t1305OutBlock1", "changerate", i)
        stock_data.fpvolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "fpvolume", i)
        stock_data.covolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "covolume", i)
        stock_data.value = instXAQueryT1305.GetFieldData("t1305OutBlock1", "value", i)
        stock_data.ppvolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "ppvolume", i)
        stock_data.o_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_sign", i)
        stock_data.o_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_change", i)
        stock_data.o_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_diff", i)
        stock_data.h_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_sign", i)
        stock_data.h_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_change", i)
        stock_data.h_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_diff", i)
        stock_data.l_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_sign", i)
        stock_data.l_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_change", i)
        stock_data.l_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_diff", i)
        stock_data.marketcap = instXAQueryT1305.GetFieldData("t1305OutBlock1", "marketcap", i)
        # 각각 날짜, 시가, 고가, 저가, 종가, 전일대비구분, 전일대비, 등락율, 누적거래량, 거래증가율, 체결강도, 소진율, 회전율, 외인순매수, 기관순매수, 누적거래대금(단위:백만), 개인순매수, 시가대비구분, 시가대비, 시가기준등락율, 고가대비구분, 고가대비, 고가기준등락율, 저가대비구분, 저가대비, 저가기준등락율, 시가총액(단위:백만)
    XAQueryEventHandlerT1305.query_state = 0
    # Reset
    return JsonResponse({})
    '''