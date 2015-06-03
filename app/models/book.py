from django.db import models
import math

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
   book_clickNum=models.IntegerField()
   def select(self,pageIndex,pageSize,sequence):
      try:
         books=book.objects.order_by('book_id').reverse()[(int(pageIndex)-1)*pageSize:int(pageIndex)*pageSize] if int(sequence)==1 else book.objects.order_by('book_clickNum').reverse()[(int(pageIndex)-1)*pageSize:int(pageIndex)*pageSize]
         return books
      except Exception as err:
         return book.objects.all()[0:0]
   def find(self,b_id):
      try:
         return book.objects.get(book_id=b_id)
      except Exception as err:
         return book()
   def findNext(self,b_id):
   	try:
         b=book.objects.reverse().filter(book_id__lt=b_id)
         return b[b.count()-1]
   	except Exception as err:
   		return False
   def findPrevious(self,b_id):
   	try:
         b=book.objects.reverse().filter(book_id__gt=b_id)
         return b[0]
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
   def getPageCount(self,pageSize):
      count=book.objects.count()
      return count/pageSize if count%pageSize==0 else count/pageSize+1
   def search(self,key,category):
      try:
         return book.objects.filter(book_title__icontains=key) if int(category)==1 else book.objects.filter(book_author__icontains=key)
      except Exception as err:
         return book.objects.all()[0:0]