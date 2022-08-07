from django.contrib import admin

# Register your models here.
from .models import Blacklist
from .models import Whitelist
from .models import EventTags
from .models import Locations
from .models import SubscriptionTypes

admin.site.register(Blacklist)
admin.site.register(Whitelist)
admin.site.register(EventTags)
admin.site.register(Locations)
admin.site.register(SubscriptionTypes)