from django import template

register = template.Library()

@register.simple_tag(name='total_price')
def total_price(cart):
    total=0
    tax=0
    total_price=0
    for items in cart.added_items.all():
        total = items.quantity*items.product.price
        tax = total*0.2 
        total_price += total+tax
        
    return round(total_price, 2)
