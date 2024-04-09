from django import template

register = template.Library()


@register.simple_tag(name='multiply')
def multiply(a, b):
    try:
        # Convert inputs to float and perform multiplication
        result = float(a) * float(b)
        return result
    except (TypeError, ValueError):
        # Handle cases where inputs are not valid numbers
        return 0  # Or any other appropriate default value
