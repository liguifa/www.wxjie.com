from django.db import models
import hashlib

class admin(models.Model):
	admin_id=models.AutoField(primary_key=True)
	admin_username=models.CharField(max_length=20)
	admin_password=models.CharField(max_length=200)
	class Meta(object):
		db_table="admins"
	def login(self,u_username,u_password):
		m=hashlib.md5()
		try:
			u=admin.objects.get(admin_username=u_username)
			m.update(u_username+u_password)
			return u.admin_password==m.hexdigest()
		except Exception as err:
			return False
	def add(self,u_username,u_password):
		try:
			u=admin.objects.get(user_username=u_username)
			return 3
		except Exception as err:
			try:
				u=admin()
				m=hashlib.md5()
				m.update(u_username+u_password)
				u.admin_username=u_username
				u.admin_password=m.hexdigest()
				u.save()
				return True
			except Exception as err:
				return 2
	def getUsername(self,u_username):
		u=admin.objects.get(user_username=u_username)
		return u.admin_id
	def getUserInfo(self,u_id):
		return admin.objects.get(user_id=u_id);