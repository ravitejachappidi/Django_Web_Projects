from django.shortcuts import render, redirect
from .models import Order


def order_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        category = request.POST['category']
        colour = request.POST['colour']
        size = request.POST['size']
        quantity = request.POST['quantity']
        hear_about = request.POST['hear-about']
        visit_store = request.POST['visit-store'] == 'yes' 

        order = Order(
            name=name,
            location=location,
            category=category,
            colour=colour,
            size=size,
            quantity=quantity,
            hear_about=hear_about,
            visit_store=visit_store
        )
        order.save()

        return redirect('order_success')

    return render(request, 'order_form.html')

def order_success(request):
    return render(request, 'order_success.html')


def order_dashboard(request):
    orders = Order.objects.all()

    categories = [order.category for order in orders]
    locations = [order.location for order in orders]
    colours = [order.colour for order in orders]
    sizes = [order.size for order in orders]

    context = {
        'categories': categories,
        'locations': locations,
        'colours': colours,
        'sizes': sizes,
    }

    return render(request, 'dashboard.html', context)