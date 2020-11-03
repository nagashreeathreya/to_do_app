from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class AddTaskForm(forms.Form):
    status_choices = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    )
    title = forms.CharField(max_length=50)
    due_date = forms.DateField()
    category = forms.CharField(max_length=50)
    status = forms.ChoiceField(choices=status_choices)