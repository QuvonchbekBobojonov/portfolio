from django.contrib import admin

from .models import (
    Resume,
    ResumeBody,
    Portfolio,
    PortfolioType,
    Servers
)


class PortfolioInline(admin.TabularInline):
    model = PortfolioType
    extra = 0


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioInline]


class ResumeInline(admin.TabularInline):
    model = ResumeBody
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = [ResumeInline]


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Servers)
admin.site.register(Portfolio, PortfolioAdmin)
