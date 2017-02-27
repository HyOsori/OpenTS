from django.conf.urls import url
import win32com.client
import pythoncom
from . import views

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("Login Success!")
            XASessionEventHandler.login_state = 1
        else:
            print("Login Fail! Error code : " + code)
# Log-in Check

id = "epikjjh"
password = "han4101!"
cert_password = "dhgud4101!"
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
urlpatterns = [
    url(r'^crawl/', views.crawl, name = 'crawl'),
    url(r'^getshcode/', views.getshcode, name='getshcode')
]