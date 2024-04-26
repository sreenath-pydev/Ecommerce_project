from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import order,order_items
from app.customer.models import customers
from app.product.models import products_table
from django.contrib import messages
import re
import razorpay
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed,JsonResponse
from app.customer.form import AddressForm



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
        ordered_item.save()

    return redirect('cart')

#update_product_quantity_in_cart
def update_product_quantity_in_cart(request):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_detail
        product_id = request.POST.get('product-id')  # Retrieve product ID from form data
        quantity = request.POST.get('quantity')

        if product_id is None:
            return HttpResponse("Product ID is missing.", status=400)

        try:
            # Convert product_id and quantity to integers
            product_id = int(product_id)
            quantity = int(quantity)

            # Retrieve the product from the database using the product_id
            product = products_table.objects.get(pk=product_id)

            # Get the cart object for the customer
            cart_obj, created = order.objects.get_or_create(owner=customer, order_status=order.CART_STAGE)

            # Update the quantity of the ordered item in the cart
            order_item, created = order_items.objects.get_or_create(product=product, owner=cart_obj)

            if quantity <= 0:
                order_item.delete()  # Remove the item from the cart if quantity is zero or less
            else:
                order_item.quantity = quantity
                order_item.save()

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


#update address

@login_required
def add_address(request):
    customer, created = customers.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=customer)
        if address_form.is_valid():
            address_form.save()
            return redirect('place_order')
    else:
        address_form = AddressForm(instance=customer)
        
    return render(request, 'address_page.html', {'address_form': address_form})


@login_required
def update_address_form(request):
    customer = get_object_or_404(customers, user=request.user)
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=customer)
        if address_form.is_valid():
            address_form.save()
            return redirect('place_order')
    else:
        address_form = AddressForm(instance=customer)
    
    return render(request, 'address_page.html', {'address_form': address_form})
#place order
def place_order(request):
    if request.method=="POST":
        user = request.user
        total = request.POST.get('total')
        customer = user.customer_detail
        context = {
            'name': user.username,
            'address': customer.address,
            'phone': customer.phone,
            'email': user.email,
            'city': customer.city,
            'locality': customer.locality,
            'pincode':customer.pincode,  
            'total':total,
        }
        
        return render(request, 'address_page.html', context)
    return render(request, 'address_page.html')


    
# order status
@login_required
def order_status(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_detail
            total_price=float(request.POST.get('tota'))
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



@login_required
def payment(request):
    if request.method == 'POST':
        try:
            user = request.user
            customer = user.customer_detail
            total_price = int(request.POST.get('total'))*100
            print(total_price)

            # Ensure that the total_price is at least ₹1 (100 paise)
            if total_price < 1:
                raise ValueError('Invalid amount. Minimum value is ₹1.')

            order_obj = order.objects.get(
                owner=customer,
                order_status=order.CART_STAGE
            )
            if order_obj:
                # Initialize Razorpay client
                client = razorpay.Client(auth=('rzp_test_QmPhbR0YVT5egw', 'T0hKmZXirqhcRFuGOgomT1Ez'))

                # Create a Razorpay order
                razorpay_order = client.order.create({
                    'amount': int(total_price *100),  # Amount in paise
                    'currency': 'INR',
                    'receipt': 'order_receipt',
                    # Add any other required parameters
                })

                # Store the Razorpay order ID in your order object
                order_obj.razorpay_order_id = razorpay_order['id']
                order_obj.save()

                # Redirect to the Razorpay payment gateway
                return redirect(razorpay_order['short_url'])
            else:
                error_message = 'Unable to process order. Please try again.'
                messages.error(request, error_message)
                return redirect('cart')
        except ValueError as ve:
            messages.error(request, str(ve))
            return redirect('cart')
        except Exception as e:
            error_message = 'Unable to process order. Please try again.'
            messages.error(request, error_message)
            return redirect('cart')
    else:
        # Handle GET request if needed
        return HttpResponseNotAllowed(['POST'])

# payment razorpay
def payments(request):
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')

        # Perform the multiplication operation here
        total_amount_paise = int(float(total_amount) * 100)

        # Initialize Razorpay client with your API key and secret
        client = razorpay.Client(auth=('rzp_test_QmPhbR0YVT5egw', 'T0hKmZXirqhcRFuGOgomT1Ez'))

        # Create a Razorpay order
        order_params = {
            'amount': total_amount*100 ,  # Amount in paise
            'currency': 'INR',
            'receipt': 'order_receipt',
            # Add any other required parameters
        }
        print(total_amount_paise)
        razorpay_order = client.order.create(order_params)

        # Return the Razorpay order ID and total_amount_paise to the client-side JavaScript
        return JsonResponse({'razorpay_order_id': razorpay_order['id'], 'total_amount_paise': total_amount_paise})

    return render(request, 'razorpay_payment.html', )