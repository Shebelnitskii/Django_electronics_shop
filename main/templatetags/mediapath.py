from django import template
from django.conf import settings

register = template.Library()

@register.filter
def mediapath(image_path, is_published):
    if is_published:
        if image_path:
            return settings.MEDIA_URL + str(image_path)
        else:
            return settings.MEDIA_URL + 'product_images/product.noimage.png'
    else:
        return settings.MEDIA_URL + 'product_images/cKT-aXyWtCA.jpg'