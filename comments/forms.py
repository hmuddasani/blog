from django import forms
from .models import Comment

#class CommentForm(forms.ModelForm):
#	class Meta:
#			model = Comment
#			fields = ('user','text','path')
			
class CommentForm(forms.Form):
	Comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Your Comment/Reply"})
	)