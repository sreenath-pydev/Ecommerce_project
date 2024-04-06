"""from django.conf import settings
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def generate_razorpay_payment(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        if amount is not None:
            try:
                amount = int(amount)
                # Proceed with the payment process using the 'amount'
                # variable here
                return JsonResponse({'success': True, 'message': 'Payment initiated successfully'})
            except ValueError:
                return JsonResponse({'success': False, 'message': 'Invalid amount format'})
        else:
            return JsonResponse({'success': False, 'message': 'Amount not provided'})
   
    
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    currency = 'INR'
    payment_data = {
        'amount': amount,
        'currency': currency,
        'receipt': 'order_receipt',
        'payment_capture': 1
    }
    razorpay_order = client.order.create(data=payment_data)
    return redirect(razorpay_order)


@csrf_exempt
def razorpay_payment_callback(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Process the payment response and update your database accordingly
        # Verify payment details, update database, handle errors
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

def order_details(request):
    # Fetch order details and delivery address details from the database
    # Replace this with your actual logic to fetch order details
    order_details = {
        'order_id': '12345',
        'total_amount': '500.00',
        # Add more order details here
    }
    context = {
        'order_details': order_details
    }
    return render(request, 'order_details.html', context)
"""