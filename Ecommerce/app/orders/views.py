from django.shortcuts import render,redirect
from .models import order,order_items
from app.product.models import products_table
import re
# Create your views here.
def cart_items(request):
    user=request.user
    customer=user.customer_detail
    cart_obj,created=order.objects.get_or_create(
        owner=customer,
        order_status= order.CART_STAGE
    )
    context={"cart":cart_obj}
    return render(request,'cart.html',context)

def add_to_cart(request,pk):
    if request.POST:
        user=request.user
        customer=user.customer_detail
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status= order.CART_STAGE
        )
        

# Remove non-numeric characters from product_id
        product_id = re.sub('[^0-9]', '', product_id)
        products = products_table.objects.get(pk=product_id)
        
        ordered_item= order_items.objects.create(
            product=products,
            owner= cart_obj,
            quantity=quantity
        )
    return redirect('cart')    