import win32com.client
import pythoncom

excel = win32com.client.Dispatch("Excel.Application")
# Excel file access
wb = excel.Workbooks.open("C:\\Users\\user\\Documents\\OpenTS\\WebServer\\web\\shcode.xlsx")
ws = wb.ActiveSheet
# Write in Excel
code_dic = {}
for i in range(2503):
    code_dic[ws.Cells(i+1,2).Value] = ws.Cells(i+1,1).Value
excel.Quit()