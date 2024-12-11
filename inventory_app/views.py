from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, UserRegistrationForm
from .models import Item, Purchase
from django.contrib.auth import login, authenticate,logout

from .forms import UserRegistrationForm

from django.contrib.auth.forms import AuthenticationForm


# Custom login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Custom logout view
@login_required
def logout_view(request):
    if request.method == "POST" or request.method == "GET":
        logout(request)
        return redirect('login') 

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    # Get the logged-in user's purchases
    
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'purchases': purchases})

from django.shortcuts import get_object_or_404

def add_item(request, purchase_id=None):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if purchase_id:
                item.purchase = get_object_or_404(Purchase, id=purchase_id)  # This will return 404 if the purchase does not exist
            else:
                purchase = Purchase.objects.create(user=request.user)
                item.purchase = purchase
            item.save()
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


@login_required
def view_purchases(request):
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'view_purchases.html', {'purchases': purchases})

@login_required
def view_items(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id, user=request.user)
    items = purchase.items.all()
    return render(request, 'view_items.html', {'items': items, 'purchase': purchase})

@login_required
def update_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_items', purchase_id=item.purchase.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    purchase_id = item.purchase.id
    item.delete()
    return redirect('view_items', purchase_id=purchase_id)

from django.shortcuts import render, redirect
from .models import Purchase
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now  # For adding the current date

@login_required
def add_purchase(request):
    if request.method == 'POST':
        # Create a new purchase for the logged-in user
        Purchase.objects.create(user=request.user, purchase_date=now())
        return redirect('dashboard')  # Redirect back to the dashboard
    return render(request, 'add_purchase.html')  # Render a basic form if needed

from django.shortcuts import get_object_or_404
@login_required
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    
    # Check if the purchase has no items before deleting
    if not purchase.items.exists():
        purchase.delete()
    return redirect('dashboard')  # Redirect to the dashboard after deletion



from django.shortcuts import render
from .models import Item

def item_list_by_type(request):
    # Grouping items by their type and including related user information
    electronics = Item.objects.filter(item_type='electronics')
    furniture = Item.objects.filter(item_type='furniture')
    clothing = Item.objects.filter(item_type='clothing')
    
    return render(request, 'item_list_by_type.html', {
        'electronics': electronics,
        'furniture': furniture,
        'clothing': clothing
    })
