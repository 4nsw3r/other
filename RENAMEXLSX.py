import os 
import openpyxl

NAME = []
RNAME = []
directory = r'C:\xl\5'
files = os.listdir(directory)
csvfiles = filter(lambda x: x.endswith('xlsx'), files)
i = 1
for key in sorted(csvfiles):
	namefile = key
	wb = openpyxl.load_workbook(namefile)
	ws = wb.active
	rename = ws['D4']
	print(rename.value)
	os.rename(namefile, rename.value+str(i)+'.xlsx')
	i += 1