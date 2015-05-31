from django.db import models

class book(models.Model):
	class Meta(object):
		db_table="books"
	book_id=models.AutoField(primary_key=True)
	book_title=models.CharField(max_length=50)
	book_image=models.CharField(max_length=100)
	book_author=models.CharField(max_length=20)
	book_introduction=models.CharField(max_length=800)
	book_recommend=models.TextField()
	book_username=models.IntegerField()
	book_time=models.DateTimeField()
	book_line=models.CharField(max_length=100)
	def select(self,pageIndex,pageSize):
   		books=book.objects.order_by('book_time')[(pageIndex-1)*pageSize:pageIndex*pageSize]
   		return books
   	def find(self,b_id):
   		try:
   			return book.objects.get(book_id=b_id)
   		except Exception as err:
   			return book()
   	def findNext(self,b_id):
   		try:
   			return book.objects.extra(where=['book_id >'+b_id])[0:1]
   		except Exception as err:
   			return False
   	def findPrevious(self,b_id):
   		try:
   			return book.objects.extra(where=['book_id <'+b_id])[0:1]
   		except Exception as err:
   			return False
   	def add(self,title,image,author,introduction,recommend,line,time,username):
   		b=book()
   		b.book_title=title
   		b.book_image=image
   		b.book_author=author
   		b.book_introduction=introduction
   		b.book_recommend=recommend
   		b.book_time=time
   		b.book_line=line
   		b.book_username=username
   		try:
   			b.save()
   			return True
   		except Exception as err:
   			return False
