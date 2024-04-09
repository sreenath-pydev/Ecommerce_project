from django.shortcuts import render,redirect,HttpResponse
from .models import order,order_items
from app.product.models import products_table
from django.contrib import messages
import re
import razorpay
from django.core.exceptions import ObjectDoesNotExist

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

def add_to_cart(request, pk):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_detail
        product_id = request.POST.get('product_id')

        # Retrieve the product from the database
        product = products_table.objects.get(pk=product_id)

        # Get or create the cart object for the customer
        cart_obj, created = order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )

        # Add the product to the cart
        ordered_item, created = order_items.objects.get_or_create(
            product=product,
            owner=cart_obj,
        )

    return redirect('cart')

#update_product_quantity_in_cart



def update_product_quantity_in_cart(request):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_detail
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if product_id is None:
            return HttpResponse("Product ID is missing.", status=400)

        try:
            # Convert product_id and quantity to integers
            product_id = int(product_id)
            quantity = int(quantity)

            # Retrieve the product from the database
            product = products_table.objects.get(pk=product_id)

            # Get the cart object for the customer
            cart_obj = order.objects.get(owner=customer, order_status=order.CART_STAGE)

            # Update the quantity of the ordered item in the cart
            ordered_item, created = order_items.objects.get_or_create(
                product=product,
                owner=cart_obj,
            )
            ordered_item.quantity = quantity
            ordered_item.save()

            return redirect('cart')

        except ObjectDoesNotExist:
            return HttpResponse("The requested product does not exist.", status=404)

        except ValueError:
            return HttpResponse("Invalid product ID or quantity.", status=400)

    return HttpResponse("Method not allowed.", status=405)
    

  

#remove product from cart
def remove_items_from_cart(request,pk):
    items = order_items.objects.get(pk=pk)
    if items:
        items.delete()
    return redirect('cart')

# customer address page
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

# order status
def order_status(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_detail
            total_price=float(request.POST.get('total'))
            order_obj=order.objects.get(
                owner=customer,
                order_status=order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=order.ORDER_CONFIRMED
                order_obj.save()
                success_message='Order Confirmed'
                messages.success(request,success_message)
            else:
                error_message='Unable to proccess order Please try again'
                messages.error(request,error_message)
        except:
            except_message='Unable to proccess order Please try again'
            messages.error(request,except_message)
        return redirect('cart')


