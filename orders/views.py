from django.contrib.contenttypes.models import ContentType

from .models import Customer, Order, OrderItem, DrinkType, Milk, Flavor, Drink
from .forms import OrderForm
from django.shortcuts import render, redirect


# Create your views here.
def drink_menu(request):
    """
    Display a list of available drinks.
    """
    drinktypes = DrinkType.objects.all()
    milks = Milk.objects.all()
    flavors = Flavor.objects.all()
    context = {
        'drinktypes': drinktypes,
        'milks': milks,
        'flavors': flavors,
    }
    return render(request, 'orders/drink_menu.html', context)

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            drink = Drink.objects.create(
                drink_type=form.cleaned_data['drink_type'],
                flavor=form.cleaned_data['flavor'],
                milk=form.cleaned_data['milk'],
                size=form.cleaned_data['size'],
                extra_shots=form.cleaned_data['extra_shots'],
                weight=form.cleaned_data['weight'],
            )
            customer = Customer.objects.create(
                first_name="Temp",
                last_name="User",
            )
            order = Order.objects.create(
                customer=customer,
                is_complete=False,
            )
            drink_ct = ContentType.objects.get_for_model(Drink)
            OrderItem.objects.create(
                order=order,
                content_type=drink_ct,
                object_id=drink.id,
                quantity=1
            )
    else:
        form = OrderForm()
    return render(request, 'orders/order_drink.html', {'form': form})


def home(request):
    return render(request, 'orders/home.html')