from django import forms
from django.contrib.auth.models import User
#from .models import Post
from .models import Post, Comment
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','item_cost', 'product_description','image','seller_name') 
	#fields=('title','text')
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
#class DocumentForm(forms.Form):
    #docfile = forms.FileField(
    #    label='Select a file',
   # )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    re_enter_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 're_enter_password']

