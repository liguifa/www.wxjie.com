from django.http import HttpRequest

class parameter(object):
	@staticmethod
	def getParameter(request,field):
		url=request.get_full_path()
		url=url.split(".html")[0]
		p_arr=url.split('_')
		i=-1
		for p in p_arr:
			if p == field:
				return p_arr[i+2]
				break
			else:
				i=i+1
		return 0