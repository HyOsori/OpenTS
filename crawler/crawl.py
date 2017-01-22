import win32com.client
import pythoncom

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("Login Success!")
            XASessionEventHandler.login_state = 1
        else:
            print("Login Fail! Error code : " + code)
#Log-in Check

class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1
#현재가 조회

stocks = ["078020", "005930", "066570", "035420", "034220", "035720", "000720", "000660", "030200", "073240"]
#주삭별 종목 코드
info = ["hname", "price", "sign", "change", "diff", "volume", "recprice", "avg", "uplmtprice", "dnlmtprice", "jnilvolume", "volumediff", "open", "opentime", "high", "hightime", "low", "lowtime"]
#각각 한글명, 현재가, 전일대비구분, 전일대비, 등락율, 누적거래량, 기준가, 가중평균, 상한가, 하한가, 전일거래량, 거래량차, 시가, 시가시간, 고가, 고가시간, 저가, 저가시간

#Excel file access
excel = win32com.client.Dispatch("Excel.Application")
#excel.Visible = True
wb = excel.Workbooks.open("C:\\Users\\user\\Documents\\OpenTS\\crawler\\Data.xlsx")
ws = wb.ActiveSheet

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
#Create instance : Server Connection & Log-in Check

id = "아이디"
password = "비밀번호"
cert_password = "공인인증서번호"
#Log-in information

if instXASession.ConnectServer("hts.ebestsec.co.kr", 20001) == False:
    print("Server Connect Fail!")
else:
    print("Server Connect success!")
#Server Connection

instXASession.Login(id,password,cert_password,1,False)

while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()
#Log-in process

instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_Dataset.XAQuery", XAQueryEventHandlerT1102)
instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"
#Create instance : 현재가 조회

for code in stocks:
    instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, code)
    instXAQueryT1102.Request(0)
    while XAQueryEventHandlerT1102.query_state == 0:
        pythoncom.PumpWaitingMessages()

    for data in info:
        ws.Cells(stocks.index(code)+2, info.index(data)+1).Value = instXAQueryT1102.GetFieldData("t1102OutBlock", data, 0)

    XAQueryEventHandlerT1102.query_state = 0
    #Reset

wb.SaveAs("C:\\Users\\user\\Documents\\OpenTS\\crawler\\Data.xlsx")
#Write in Excel
excel.Quit()