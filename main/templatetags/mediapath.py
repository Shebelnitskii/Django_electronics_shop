from django import template
from django.conf import settings

register = template.Library()

@register.filter
def mediapath(image_path):
    if image_path:
        return settings.MEDIA_URL + str(image_path)
    else:
        return settings.MEDIA_URL + 'product_images/product.noimage.png'