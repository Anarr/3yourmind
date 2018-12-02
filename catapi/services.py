import requests 
from django.conf import settings
from django.core.cache import cache


class CatService:
    """
        Args:
            CATAPI_URL: External api url
            CACHE_TIMEOUT: CATAPI_URL response cache timeout duration
    """
    CATAPI_URL, CACHE_TIMEOUT = settings.CATAPI_URL, settings.CACHE_TIMEOUT

    def get_cats(self, tag, limit): 
        """
        function get cat images from catapi service.
        
        Args:
            tag: The first parameter and display cat image.
            limit: The count of fetched data

        Returns:
            Dictionary
        """

        if tag is not None:
            cachedCatData = cache.get("{}_{}".format(tag, limit))
            if cachedCatData:
                return cachedCatData

            tag, limit = str(tag), int(limit)
            # if tag not exists inside of category_ids thecatapi also return different data
            category_ids = self.__find_category_id_by_tag(tag)
            try:
                headers = {'x-api-key': settings.CATAPI_KEY}
                payload = {
                    'limit': limit, 
                    'category_ids': category_ids
                }

                r = requests.get(self.CATAPI_URL + '/v1/images/search', headers=headers, params=payload)
                cache.set("{}_{}".format(tag, limit), r.json(), self.CACHE_TIMEOUT)
                content = r.json()
                return content
            except:
                return {}
        else:
            return {}

    def get_categories(self, limit=5):
        """
        function get categories  fetch available categories from catapi.

        Args:
            limit: The count of fetched data.

        Returns:
            Dictionary
        """

        cachedCategoryData = cache.get('categories')

        if cachedCategoryData:
            return cachedCategoryData

        limit = int(limit)
        headers = {'x-api-key': settings.CATAPI_KEY}
        payload = {'limit': limit}
        r = requests.get(self.CATAPI_URL + '/v1/categories', headers=headers, params=payload)
        
        cache.set('categories', r.json(), self.CACHE_TIMEOUT)
        content = r.json()
        return content

    def __find_category_id_by_tag(self, tag):
        categories = self.get_categories()
        categoriesArr = categories
        
        categoryId = [category['id'] for category in categoriesArr if tag == category['name'] ]

        return categoryId
        
