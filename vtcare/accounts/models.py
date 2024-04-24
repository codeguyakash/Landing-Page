from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

class Myaccount(BaseUserManager):
    def create_user(self,first_name,last_name,user_name,email,password=None):
        if not email:
            raise ValueError('user must have an email address')
        
        if not user_name:
            raise ValueError('user must have username')
        user=self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, first_name, last_name, user_name, email, password):
        
        user = self.create_user(
        first_name=first_name,
        last_name=last_name,
        user_name=user_name,
        email=email,
        password=password,
    )
        
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

            



class Account(AbstractBaseUser):
    first_name      =models.CharField(max_length=100,null=True,default=None,blank=True)
    last_name       =models.CharField(max_length=100,null=True,default=None,blank=True)
    user_name       =models.CharField(max_length=100,null=True,default=None,blank=True)

    email           =models.EmailField(max_length=150,null=True,default=None,unique=True)
    phone_number    =PhoneNumberField(blank=True)
    address         =models.CharField(max_length=300,null=True,default=None,blank=True)
    query           =models.TextField()
    
    
    # required
    
    date_joined     =models.DateTimeField(auto_now_add=True)
    last_login      =models.DateTimeField(auto_now_add=True)
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=False)
    is_superadmin   =models.BooleanField(default=False)
    is_seller       =models.BooleanField(default=False)
    is_buyer        =models.BooleanField(default=False)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name','last_name']
    
    objects=Myaccount()
    
    def __str__(self):
        return self.email
    
    
    
    def has_module_perms(self, app_label):
       return True
   
   
   
    def has_perm(self, perm, obj=None):
       return self.is_admin
   
class ContactUs(Account):
    class Meta:
        proxy = True
        verbose_name = 'contactus'
        verbose_name_plural = 'contactus'   
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    

class Product(models.Model):
    category     =models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller       =models.ForeignKey(Account, related_name='products', on_delete=models.CASCADE)
    name         =models.CharField(max_length=200, db_index=True)
    description  =models.TextField(blank=True)
    image        =models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price        =models.DecimalField(max_digits=10, decimal_places=2)
    available    =models.BooleanField(default=True)
    stock        =models.PositiveIntegerField()
    created_at   =models.DateTimeField(auto_now_add=True)
    updated_at   =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'description'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.description])
    
    
    
class Review(models.Model):
    product       =models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author        =models.CharField(max_length=100)
    text          =models.TextField()
    created_at    =models.DateTimeField(auto_now_add=True)
    updated_at    =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.author} on {self.product.name}"
    
    
    
    
    
    
    
    
    
    # pass=care12345,user=vtcare@12gmail.com,user