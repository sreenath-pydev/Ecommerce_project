from django.shortcuts import render,redirect
from .models import order,order_items
from app.product.models import products_table
import re
import razorpay


# load cart page
def cart_items(request):
    user=request.user
    customer=user.customer_detail
    cart_obj,created=order.objects.get_or_create(
        owner=customer,
        order_status= order.CART_STAGE
    )
    context={"cart":cart_obj}
    return render(request,'cart.html',context)

# add product to cart
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
        
        ordered_item,created= order_items.objects.get_or_create(
            product=products,
            owner= cart_obj,
        )
        if created: 
            ordered_item.quantity=quantity
            ordered_item.save()
        # if orederd items exist in cart, then only add quantity
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')    

#remove product in cart
def remove_items_from_cart(request,pk):
    items = order_items.objects.get(pk=pk)
    if items:
        items.delete()
    return redirect('cart')

# address page
def place_order(request):
    user = request.user
    customer = user.customer_detail
    context = {
        'name': user.username,
        'address': customer.address,
        'phone': customer.phone,
        'email': user.email
    }
    return render(request, 'address_page.html', context)

