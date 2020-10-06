import os
import shutil

FilesOut = r'gip\УВЕДОМЛЕНИЯ ЮСБ ЧАСТЬ'
FilesIn = r'gip\01.12.2019'

files = []
paths = []
surnames = []

path1 = os.walk(FilesOut)
for i, _, k in path1:
	for file in k:
		#print(i+'\\'+file)
		files.append(i+'\\'+file)

path2 = os.walk(FilesIn)
for path, folders, files in path2:
	paths.append(path)

dir_list = os.listdir(FilesOut)
for surname in dir_list:
	if surname.split()[0].isdigit():
		sname = (surname.split()[1])
	else:
		sname = (surname.split()[0])
	#print(a1)
	surnames.append(sname+' ')

for file in files:
	for path in paths:
		for word in surnames:
			#word.lower() in path.lower():
			if word.lower() in file.lower() and word.lower() in path.lower():
				#print(file)
				if file in path:
					continue
				else:
					try:
						shutil.copy2(file, path)
					except:
						continue
print('ok')