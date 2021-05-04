from validate_docbr import CNPJ
from django.core.exceptions import ValidationError

def validate_cnpj(value):
    cnpj = CNPJ()
    if cnpj.validate(value) == False:
        raise ValidationError('CNPJ inválido', params={'value': value})


