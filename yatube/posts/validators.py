from django import forms


def validate_not_empty(values):
    if values == '':
        raise forms.ValidationError(
            'А кто поле заполнять будет, Пушкин?'
        )
