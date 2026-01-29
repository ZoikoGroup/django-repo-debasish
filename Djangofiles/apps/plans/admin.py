from django.contrib import admin
from .models import PlanType, PlanCategory, Plan, PlanFeature


@admin.register(PlanType)
class PlanTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PlanCategory)
class PlanCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 1


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'plan_type',
        'category',
        'price',
        'is_active',
        'created_at',
    )

    list_filter = ('is_active', 'is_popular', 'plan_type', 'category')
    search_fields = ('name',)
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('name',)}

    inlines = [PlanFeatureInline]
