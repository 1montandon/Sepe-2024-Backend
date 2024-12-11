"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name", "get_groups" ]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Campeonato)
admin.site.register(models.Rodada)
admin.site.register(models.Jogo)
from core.models import TimeJogador


class TimeJogadorInline(admin.TabularInline):
    model = TimeJogador
    extra = 1 # Quantidade de itens adicionais


@admin.register(models.Time)
class TimeAdmin(admin.ModelAdmin):
    inlines = [TimeJogadorInline]


@admin.register(models.Jogador)
class JogadorAdmin(admin.ModelAdmin):
    inlines = [TimeJogadorInline]