country=input('你来自哪个国家：')
age= input('请问你的年龄：')
age= int(age)
if country=='台湾':
	if age>= 18:
	  print('您可以考取驾照')
	else:
	    print('您的年龄未达标')
if country== '美国':
	if age>= 16:
		print ('您可以考取驾照')
	else:
		print('您的年龄未达标')

