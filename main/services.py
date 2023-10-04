from django.conf import settings
from django.core.cache import cache

def get_cache_categories(self):
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = self.object_list.all()
            cache.set(key, category_list)
    else:
        category_list = self.object_list.all()

    return category_list