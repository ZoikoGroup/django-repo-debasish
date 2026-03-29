from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            # Basic info
            'name',
            'slug',
            'plan_type',
            'category',

            # Pricing & duration
            'price',
            'sale_price',
            'duration_days',
            'sim_type',

            # Flags
            'is_popular',
            'is_active',

            # SEO
            'meta_title',
            'meta_description',
            'meta_keywords',
            'canonical_url',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

            'plan_type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'duration_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'sim_type': forms.Select(attrs={'class': 'form-control'}),

            'is_popular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control'}),
            'canonical_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
