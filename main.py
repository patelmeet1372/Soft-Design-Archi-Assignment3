import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myApp.settings')
django.setup()

from example.models import ProdInvt

new_item = ProdInvt(item_bc='54321', item_details='iWatch-$550')
new_item.save()

