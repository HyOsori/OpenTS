from django.shortcuts import render
from django.http import JsonResponse
import win32com.client
import pythoncom

# Create your views here.

from django.shortcuts import render_to_response

def search(request):
    return render_to_response('search.html')

def result(request):
    return render_to_response('result.html')

def getshcode(request):
    keyword = request.GET['keyword']

    if keyword == 'SAMSUNG':
        return render_to_response('result.html')
    else:
        return JsonResponse({
            'status': 'Failure',
            'shcode': -1
        })

def crawl(request):
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

    # 현재가 조회

    stocks = ["078020", "005930", "066570", "035420", "034220", "035720", "000720", "000660", "030200", "073240"]
    # 주삭별 종목 코드
    info = ["shcode", "date", "open", "high", "low", "close", "sign", "change", "diff", "volume", "diff_vol",
            "chdegree", "sojinrate", "changerate", "fpvolume", "covolume", "value", "ppvolume", "o_sign", "o_change",
            "o_diff", "h_sign", "h_change", "h_diff", "l_sign", "l_change", "l_diff", "marketcap"]
    # 각각 날짜, 시가, 고가, 저가, 종가, 전일대비구분, 전일대비, 등락율, 누적거래량, 거래증가율, 체결강도, 소진율, 회전율, 외인순매수, 기관순매수, 누적거래대금(단위:백만), 개인순매수, 시가대비구분, 시가대비, 시가기준등락율, 고가대비구분, 고가대비, 고가기준등락율, 저가대비구분, 저가대비, 저가기준등락율, 시가총액(단위:백만)

    # Excel file access
    excel = win32com.client.Dispatch("Excel.Application")
    # excel.Visible = True
    wb = excel.Workbooks.open("C:\\Users\\user\\Documents\\OpenTS\\crawler\\Data.xlsx")
    ws = wb.ActiveSheet

    instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
    # Create instance : Server Connection & Log-in Check

    id = ""
    password = ""
    cert_password = ""
    # Log-in information

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


    for code in stocks:
        instXAQueryT1305.SetFieldData("t1305InBlock", "shcode", 0, code)
        instXAQueryT1305.SetFieldData("t1305InBlock", "dwmcode", 0, 1)
        instXAQueryT1305.SetFieldData("t1305InBlock", "cnt", 0, 100)
        # Default amount : 100

        instXAQueryT1305.Request(0)
        while XAQueryEventHandlerT1305.query_state == 0:
            pythoncom.PumpWaitingMessages()

        count = instXAQueryT1305.GetBlockCount("t1305OutBlock1")
        for i in range(count):
            for data in info:
                stock_data = Data()
                ws.Cells(stocks.index(code) * count + i + 2,
                         info.index(data) + 1).Value = instXAQueryT1305.GetFieldData("t1305OutBlock1", data, i)

        XAQueryEventHandlerT1305.query_state = 0
        # Reset

    '''
    data = Data()
    data.date = oeifj
    data. oej = wefoiwejf
    data.save()

    '''
    wb.Save()

    # wb.SaveAs("C:\\Users\\user\\Documents\\OpenTS\\crawler\\Data.xlsx")
    # Save as another name

    # Write in Excel
    excel.Quit()
    return JsonResponse({})