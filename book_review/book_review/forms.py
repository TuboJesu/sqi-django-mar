from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer_name", "rating", "comment"]


class ManualReviewForm(forms.Form):
    reviewer_name = forms.CharField(max_length=255, widget=forms.TextInput())
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={"min":1, "max":5}))
    comment = forms.CharField(widget=forms.Textarea())


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]


class UpdateManualForm(forms.Form):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={"min":1, "max":5}))
    comment = forms.CharField(widget=forms.Textarea())