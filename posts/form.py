from django import forms  
from .models import Post 
class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = ['fullName', 'date', 'fullUrl', 'comment'] 
        widgets = { 'fullName': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'date': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'fullUrl': forms.DateInput(attrs={ 'class': 'form-control' }),
            'comment': forms.TextInput(attrs={ 'class': 'form-control' }),

      }
