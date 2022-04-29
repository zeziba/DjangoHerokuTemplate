from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import UserCreationForm, UserChangeForm
from .models import Account

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Account
    list_display = ["email", "username",]

admin.site.register(Account, CustomUserAdmin)