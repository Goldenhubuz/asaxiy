from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from details.models import CategoryModel, ImageModel, DiscountModel, ReviewModel, CharacteristicsModel

# Register your models here.
admin.site.register(
    CategoryModel,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(ImageModel)
admin.site.register(DiscountModel)
admin.site.register(ReviewModel)
admin.site.register(CharacteristicsModel)
