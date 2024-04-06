from django import template

register = template.Library()

@register.simple_tag(name='tax')
def tax(cart):
    total=0
    tax=0
    for items in cart.added_items.all():
        total = items.quantity*items.product.price
        tax += total*0.2 
        
    return round(tax,2)
