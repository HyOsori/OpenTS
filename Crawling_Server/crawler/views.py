from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
from .singleton import code_dic
import win32com.client
import pythoncom
import sys
import requests
# Create your views here.
from django.shortcuts import render_to_response

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("Login Success!")
            XASessionEventHandler.login_state = 1
        else:
            print("Login Fail! Error code : " + code)
# Log-in Check

class XAQueryEventHandlerT1305:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1305.query_state = 1
# 기간별 주가 조회


def getshcode(request):
    keyword = request.GET['keyword']

    if keyword in code_dic.keys():
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

def crawl(request):
    pythoncom.CoInitialize()
    if(XASessionEventHandler.login_state==0):
        id = ""
        password = ""
        cert_password = ""
        # Log-in information

        instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
        # Create instance : Server Connection & Log-in Check

        if instXASession.ConnectServer("hts.ebestsec.co.kr", 20001) == False:
            print("Server Connect Fail!")
        else:
            print("Server Connect success!")
        # Server Connection

        instXASession.Login(id, password, cert_password, 1, False)

        while XASessionEventHandler.login_state == 0:
          pythoncom.PumpWaitingMessages()
        # Log-in process

    instXAQueryT1305 = win32com.client.DispatchWithEvents("XA_Dataset.XAQuery", XAQueryEventHandlerT1305)
    instXAQueryT1305.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1305.res"
    # Create instance : 기간별 주가 조회

    URL = "127.0.0.1:8000/web/crawl"
    data = {"shcode":"code","date":"today","open":0,"high":0,"low":0,"close":0,"sign":0,"change":0,"diff":0,"volume":0,"diff_vol":0,"chdegree":0,
    "sojinrate":0,"changerate":0,"fpvolume":0,"covolume":0,"value":0,"ppvolume":0,"o_sign":0,"o_change":0,"o_diff":0,"h_sign":0,"h_change":0,
    "h_diff":0,"l_sign":0,"l_change":0,"l_diff":0,"marketcap":0}
    #local host

    shcode = request.GET['shcode']
    instXAQueryT1305.SetFieldData("t1305InBlock", "shcode", 0, shcode)
    instXAQueryT1305.SetFieldData("t1305InBlock", "dwmcode", 0, 1)
    instXAQueryT1305.SetFieldData("t1305InBlock", "cnt", 0, 100)
    # Default amount : 100

    instXAQueryT1305.Request(0)
    print("hey!")
    while XAQueryEventHandlerT1305.query_state == 0:
        pythoncom.PumpWaitingMessages()
    print("hey")
    count = instXAQueryT1305.GetBlockCount("t1305OutBlock1")

    for i in range(count):
        stock_data = Data()
        stock_data.shcode = instXAQueryT1305.GetFieldData("t1305OutBlock1", "shcode", i)
        data["shcode"]=instXAQueryT1305.GetFieldData("t1305OutBlock1", "shcode", i)

        stock_data.date = instXAQueryT1305.GetFieldData("t1305OutBlock1", "date", i)
        data["date"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "date", i)

        stock_data.open = instXAQueryT1305.GetFieldData("t1305OutBlock1", "open", i)
        data["open"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "open", i)

        stock_data.high = instXAQueryT1305.GetFieldData("t1305OutBlock1", "high", i)
        data["high"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "high", i)

        stock_data.low = instXAQueryT1305.GetFieldData("t1305OutBlock1", "low", i)
        data["low"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "low", i)

        stock_data.close = instXAQueryT1305.GetFieldData("t1305OutBlock1", "close", i)
        data["close"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "close", i)

        stock_data.sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sign", i)
        data["sign"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sign", i)

        stock_data.change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "change", i)
        data["change"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "change", i)

        stock_data.diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff", i)
        data["diff"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff", i)

        stock_data.volume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "volume", i)
        data["volume"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "volume", i)

        stock_data.diff_vol = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff_vol", i)
        data["diff_vol"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "diff_vol", i)

        stock_data.chdegree = instXAQueryT1305.GetFieldData("t1305OutBlock1", "chdegree", i)
        data["chdegree"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "chdegree", i)

        stock_data.sojinrate = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sojinrate", i)
        data["sojinrate"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "sojinrate", i)

        stock_data.changerate = instXAQueryT1305.GetFieldData("t1305OutBlock1", "changerate", i)
        data["changerate"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "changerate", i)

        stock_data.fpvolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "fpvolume", i)
        data["fpvolume"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "fpvolume", i)

        stock_data.covolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "covolume", i)
        data["covolume"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "covolume", i)

        stock_data.value = instXAQueryT1305.GetFieldData("t1305OutBlock1", "value", i)
        data["value"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "value", i)

        stock_data.ppvolume = instXAQueryT1305.GetFieldData("t1305OutBlock1", "ppvolume", i)
        data["ppvolume"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "ppvolume", i)

        stock_data.o_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_sign", i)
        data["o_sign"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_sign", i)

        stock_data.o_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_change", i)
        data["o_change"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_change", i)

        stock_data.o_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_diff", i)
        data["o_diff"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "o_diff", i)

        stock_data.h_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_sign", i)
        data["h_sign"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_sign", i)

        stock_data.h_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_change", i)
        data["h_change"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_change", i)

        stock_data.h_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_diff", i)
        data["h_diff"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "h_diff", i)

        stock_data.l_sign = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_sign", i)
        data["l_sign"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_sign", i)

        stock_data.l_change = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_change", i)
        data["l_change"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_change", i)

        stock_data.l_diff = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_diff", i)
        data["l_diff"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "l_diff", i)

        stock_data.marketcap = instXAQueryT1305.GetFieldData("t1305OutBlock1", "marketcap", i)
        data["marketcap"] = instXAQueryT1305.GetFieldData("t1305OutBlock1", "marketcap", i)

        #res = requests.request("POST",URL,data=data)
        stock_data.save()
        # 각각 날짜, 시가, 고가, 저가, 종가, 전일대비구분, 전일대비, 등락율, 누적거래량, 거래증가율, 체결강도, 소진율, 회전율, 외인순매수, 기관순매수, 누적거래대금(단위:백만), 개인순매수, 시가대비구분, 시가대비, 시가기준등락율, 고가대비구분, 고가대비, 고가기준등락율, 저가대비구분, 저가대비, 저가기준등락율, 시가총액(단위:백만)
    XAQueryEventHandlerT1305.query_state = 0

    # Reset
    return JsonResponse({
            'status': data
    })