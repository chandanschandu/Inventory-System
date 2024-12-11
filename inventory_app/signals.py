# apps.py
from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

    def ready(self):
        import inventory.signals

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Item, Purchase

@receiver(post_delete, sender=Item)
@receiver(post_delete, sender=Item)
def delete_empty_purchase(sender, instance, **kwargs):
    purchase = instance.purchase
    print(f"Checking Purchase #{purchase.id} for empty items.")  # Debugging line
    if not purchase.items.exists():
        print(f"Deleting Purchase #{purchase.id} because it has no items.")  # Debugging line
        purchase.delete()

