from django.conf.urls import url
from . import views

'''
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
# Log-in Check

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
'''

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^result/', views.result, name = 'result'),
    url(r'^crawl/', views.Crawling.as_view, name='crawl'),
    url(r'^getshcode/', views.getshcode, name='getshcode')
]