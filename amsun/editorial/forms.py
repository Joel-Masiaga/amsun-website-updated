from django import forms
from tinymce.widgets import TinyMCE
from core.models import Blog, News, Events, Research
from users.models import User


# ---------------------------------------------------------------------------
# Shared widget CSS class names (defined in editorial/base.html)
# ---------------------------------------------------------------------------

TEXT_INPUT = 'edt-input'
SELECT     = 'edt-select'
FILE_INPUT = 'edt-file'
DATE_INPUT = 'edt-date'


# ---------------------------------------------------------------------------
# TinyMCE config override – dark skin inside the editorial portal
# ---------------------------------------------------------------------------

TINYMCE_ATTRS = {
    'mce_attrs': {
        'skin': 'oxide-dark',
        'content_css': 'dark',
        'height': 520,
        'plugins': (
            'advlist autolink autosave link image lists charmap preview '
            'anchor pagebreak searchreplace wordcount visualblocks '
            'visualchars code fullscreen insertdatetime media nonbreaking '
            'table emoticons codesample directionality'
        ),
        'toolbar': (
            'undo redo | blocks fontsize | bold italic underline strikethrough | '
            'forecolor backcolor | alignleft aligncenter alignright alignjustify | '
            'bullist numlist outdent indent | link image media table codesample | '
            'blockquote hr charmap emoticons | searchreplace fullscreen preview code'
        ),
        'toolbar_mode': 'wrap',
        'menubar': 'file edit view insert format tools table help',
        'branding': False,
        'promotion': False,
        'resize': True,
        'statusbar': True,
        'elementpath': False,
        'autosave_ask_before_unload': True,
        'autosave_interval': '30s',
        'image_advtab': True,
        'image_caption': True,
        'relative_urls': False,
        'remove_script_host': False,
        'convert_urls': True,
        'content_style': (
            'body { font-family: Inter, sans-serif; font-size: 15px; '
            'color: #f1f5f9; background: #1a2236; line-height: 1.75; '
            'max-width: 100%; margin: 0; padding: 16px; } '
            'h1,h2,h3,h4 { font-weight: 700; margin-top: 1.4em; color: #f8fafc; } '
            'p { margin-bottom: 1em; } '
            'a { color: #f59e0b; } '
            'blockquote { border-left: 4px solid #f59e0b; padding-left: 16px; '
            'color: #94a3b8; margin: 1em 0; font-style: italic; } '
            'code { background: #0f172a; color: #86efac; padding: 2px 6px; '
            'border-radius: 4px; font-size: 0.88em; } '
            'pre { background: #0f172a; color: #e2e8f0; padding: 16px; '
            'border-radius: 8px; overflow-x: auto; } '
            'img { max-width: 100%; height: auto; border-radius: 8px; } '
            'table { border-collapse: collapse; width: 100%; } '
            'table td, table th { border: 1px solid #1f2d45; padding: 8px 12px; } '
            'ul, ol { padding-left: 1.5em; margin-bottom: 1em; } '
            'hr { border: none; border-top: 1px solid #1f2d45; margin: 1.5em 0; }'
        ),
    }
}


# ---------------------------------------------------------------------------
# Blog Form
# ---------------------------------------------------------------------------

class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'required': False}, mce_attrs=TINYMCE_ATTRS['mce_attrs']))

    class Meta:
        model  = Blog
        fields = ['title', 'body', 'author', 'category', 'image']
        widgets = {
            'title':    forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Blog post title'}),
            'author':   forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Author name'}),
            'category': forms.Select(attrs={'class': SELECT}),
            'image':    forms.ClearableFileInput(attrs={'class': FILE_INPUT}),
        }


# ---------------------------------------------------------------------------
# News Form
# ---------------------------------------------------------------------------

class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'required': False}, mce_attrs=TINYMCE_ATTRS['mce_attrs']))

    class Meta:
        model  = News
        fields = ['headline', 'content', 'published_date', 'author', 'category', 'image']
        widgets = {
            'headline':       forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'News headline'}),
            'published_date': forms.DateInput(attrs={'class': DATE_INPUT, 'type': 'date'}),
            'author':         forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Reporter name'}),
            'category':       forms.Select(attrs={'class': SELECT}),
            'image':          forms.ClearableFileInput(attrs={'class': FILE_INPUT}),
        }


# ---------------------------------------------------------------------------
# Events Form
# ---------------------------------------------------------------------------

class EventForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'required': False}, mce_attrs=TINYMCE_ATTRS['mce_attrs']))

    class Meta:
        model  = Events
        fields = ['title', 'description', 'date', 'time', 'location', 'host', 'category', 'image']
        widgets = {
            'title':    forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Event title'}),
            'date':     forms.DateInput(attrs={'class': DATE_INPUT, 'type': 'date'}),
            'time':     forms.TimeInput(attrs={'class': DATE_INPUT, 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Venue / location'}),
            'host':     forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Organiser'}),
            'category': forms.Select(attrs={'class': SELECT}),
            'image':    forms.ClearableFileInput(attrs={'class': FILE_INPUT}),
        }


# ---------------------------------------------------------------------------
# Research Form
# ---------------------------------------------------------------------------

class ResearchForm(forms.ModelForm):
    abstract = forms.CharField(widget=TinyMCE(attrs={'required': False}, mce_attrs=TINYMCE_ATTRS['mce_attrs']))

    class Meta:
        model  = Research
        fields = ['title', 'authors', 'journal', 'abstract', 'link']
        widgets = {
            'title':   forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Research title'}),
            'authors': forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Author names (comma-separated)'}),
            'journal': forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Journal name'}),
            'link':    forms.URLInput(attrs={'class': TEXT_INPUT, 'placeholder': 'https://…'}),
        }


# ---------------------------------------------------------------------------
# User creation form (admin creates editor accounts)
# ---------------------------------------------------------------------------

class EditorCreateForm(forms.ModelForm):
    password  = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Password'}),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Confirm password'}),
        label='Confirm password'
    )

    class Meta:
        model  = User
        fields = ['email', 'first_name', 'last_name', 'role']
        widgets = {
            'email':      forms.EmailInput(attrs={'class': TEXT_INPUT, 'placeholder': 'editor@example.com'}),
            'first_name': forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'First name'}),
            'last_name':  forms.TextInput(attrs={'class': TEXT_INPUT, 'placeholder': 'Last name'}),
            'role':       forms.Select(attrs={'class': SELECT}),
        }

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# ---------------------------------------------------------------------------
# Login Form
# ---------------------------------------------------------------------------

class EditorialLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': TEXT_INPUT,
            'placeholder': 'your@email.com',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': TEXT_INPUT,
            'placeholder': '••••••••',
        })
    )
