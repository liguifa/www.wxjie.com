from django.db import models
import hashlib

class user(models.Model):
	user_id=models.AutoField(primary_key=True)
	user_username=models.CharField(max_length=20)
	user_password=models.CharField(max_length=200)
	class Meta(object):
		db_table="users"
	def login(self,u_username,u_password):
		m=hashlib.md5()
		try:
			u=user.objects.get(user_username=u_username)
			m.update(u_username+u_password)
			return u.user_password==m.hexdigest()
		except Exception as err:
			return False
	def register(self,u_username,u_password):
		try:
			u=user.objects.get(user_username=u_username)
			return 3
		except Exception as err:
			try:
				u=user()
				m=hashlib.md5()
				m.update(u_username+u_password)
				u.user_username=u_username
				u.user_password=m.hexdigest()
				u.save()
				return True
			except Exception as err:
				return 2
	def getUsername(self,u_username):
		u=user.objects.get(user_username=u_username)
		return u.user_id
	def getUserInfo(self,u_id):
		return user.objects.get(user_id=u_id);