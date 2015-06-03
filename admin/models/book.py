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
   def select(self,pageIndex,pageSize):
      try:
         books=book.objects.order_by('book_time').reverse()[(int(pageIndex)-1)*pageSize:int(pageIndex)*pageSize]
         return books
      except Exception as err:
         return book.objects.all()[0:0]
   def find(self,b_id):
      try:
         return book.objects.get(book_id=b_id)
      except Exception as err:
         return book()
   def getPageCount(self,pageSize):
      count=book.objects.count()
      return count/pageSize if count%pageSize==0 else count/pageSize+1
