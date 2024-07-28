from django.core.exceptions import ValidationError


def validar_nombre_plato(value):
    if len(value) <= 3:
        raise ValidationError(
            '%(value) no es un nombre válido de plato', params={'value': value},)


def validar_fechas_menu(date2,date1):
    if date2 < date1:
        raise ValidationError(
            'La fecha final no puede ser menor que la fecha inicial', params={'date1': date1, 'date2': date2}
        )
