# -*- coding: utf-8 -*-
# __author__ = 'kai.zhang'
# create date = 2018/04/18
# check file exsit  status.. retry of 10s 
def check(path):
	print 'check: path is {1}'.format(path)
	cmd = 'sh ./is_exsit.sh {0}'.format(path)
	try:
		res = os.popen(cmd).readlines()
		print int(res[0].strip())
		if int(res[0].strip()) == 0:
			return True
		else:
			print 'retry check(path):' + key
			time.sleep(10)
			check(path)
	except Exception,e:
        	print e.message
		print 'retry check(path):' + key
                time.sleep(10)
                check(path)
