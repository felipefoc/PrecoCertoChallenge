from django import template
register = template.Library()


@register.filter
def add_class(modelform_input, css_class):
    return modelform_input.as_widget(attrs={'class': css_class})

@register.filter(name='add_attr')
def add_attr(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)