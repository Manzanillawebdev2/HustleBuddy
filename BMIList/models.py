from django.db import models

class LogIn(models.Model):
	pass
#	lsignup=models.ForeignKey (SignUp, default=None, on_delete=models.CASCADE)
#	psw=models.ForeignKey (SignUp, default=None, on_delete=models.CASCADE)
	
#	class meta:
#		db_table= "LogIn"
		
#class Index(models.Model):
#	pass
class SignUp(models.Model):
#	sex = [
#				('Male', 'Male'),
#				('Female', 'Female'),
#				]
	meyl = models.EmailField(default="", max_length =50)
	psw=models.CharField(default="", max_length =50)
	fname=models.CharField(default="", max_length =50)
	lname=models.CharField(default="", max_length =50)
	age=models.PositiveIntegerField(default="")
	sex=models.TextField(max_length =20, default="---")
	
	class meta:
		db_table= "SignUp"		
		
		
class InputData(models.Model):
	SignUp=models.ForeignKey(SignUp,default=None, on_delete=models.CASCADE)
	Date=models.DateTimeField(auto_now_add=True, null=True)
	Height=models.FloatField(default="")
	Weight=models.FloatField(default="")
	BMITotal=models.FloatField(default="")
	BMIResult=models.TextField(default="")
	class meta:
		db_table="InputData"	

class Rate(models.Model):
	SignUp=models.ForeignKey(SignUp,default=None, on_delete=models.CASCADE)
	Rating=models.TextField(default="")
	Message=models.TextField(default="")
#	pass

# Create your models here.
#class Item(models.Model):
#	KeyId=models.(unit,default=None, on_delete=models.CASCADE)
#	text=models.TextField(default="")
#	pass

# Create your models here.
