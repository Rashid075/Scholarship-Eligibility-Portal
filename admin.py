from django.contrib import admin
from Application.models import Login
from Application.models import ContactModel
from Application.models import MeritModel
from Application.models import AthleticModel
from Application.models import EconomicalModel
from Application.models import Merit_Services
from Application.models import Sport_Services
from Application.models import Economical_Services

# Register your models here.
admin.site.register(Login)
admin.site.register(ContactModel)
admin.site.register(MeritModel)
admin.site.register(AthleticModel)
admin.site.register(EconomicalModel)
admin.site.register(Merit_Services)
admin.site.register(Sport_Services)
admin.site.register(Economical_Services)