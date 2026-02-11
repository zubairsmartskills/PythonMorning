import openpyxl

def readData(file,sheetName,rowno,columnno):
    wb = openpyxl.load_workbook(file)
    ws = wb[sheetName]
    return ws.cell(row=rowno, column=columnno).value