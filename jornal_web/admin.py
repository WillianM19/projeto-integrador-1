from django.contrib import admin
from .models import Postador, Publicacao, Tags
from django.contrib.auth.admin import UserAdmin

@admin.register(Postador)
class PostadorAdmin(UserAdmin):
    list_display = ('nome', 'email', 'is_active_display', 'is_staff_display', 'is_superuser_display')
    search_fields = ('nome', 'email')
    ordering = ('nome',)

    def is_active_display(self, obj):
        return obj.is_active
    is_active_display.boolean = True
    is_active_display.short_description = 'Ativo'

    def is_staff_display(self, obj):
        return obj.is_staff
    is_staff_display.boolean = True
    is_staff_display.short_description = 'ADMIN'

    def is_superuser_display(self, obj):
        return obj.is_superuser
    is_superuser_display.boolean = True
    is_superuser_display.short_description = 'Superusuário'

    fieldsets = (
        (None, {'fields': ('nome', 'email', 'password', 'imagem_perfil')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'email',  'imagem_perfil', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

admin.site.register(Publicacao)
admin.site.register(Tags)