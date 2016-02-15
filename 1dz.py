#coding: utf-8
print('Hello, github')
import os
path='test'
dirs=os.listdir(path)

count=0
countfiles=0
files=[]
localcounts=[]
record= ""



for file in dirs:
	f=open(file)
	
	words=f.read()
	words=words.split()
	
	localcount=0
	
	for word in words:
		word.lower
		if word=='python':
			count+=1
			localcount+=1
			files.append(file)
	if localcount !=0:
		localcounts.append(localcount)
		countfiles+=1


		
if count != 0:
	print('Слово "python" найдено в файлах:')		
	for file in files:
		print (file)
	print('Всего встретилось '+str(count) +' раз(а)')
	a=0
	while a != countfiles:	
		a+=1
		record=record+'В файле ' +str( files[a-1])+ ' ' + str(localcounts[a-1] )+ ' раз(а) встретилось слово "python"\n' 
	f=open('result.txt','w')
	f.write(record )
	f.close()
else:
	print('Слово " python " в файлах не найдено')
	
