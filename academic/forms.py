from django import forms
from .models import OrderJob

class NewOrderForm(forms.ModelForm):

	class Meta:
		model = OrderJob
		fields = ('order_pages', 'paper_subject', 'paper_topic', 'paper_style', 'sources_num', 'paper_deadline', 'paper_instruc', 'paper_files')
