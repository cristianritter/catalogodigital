from django.db import models
from django.core.validators import URLValidator

class MultipleURLsField(models.TextField):          # Created Field Type For Multiple URL At The Same Field
    description = "Field to store multiple URLs separated by comma"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_urls(self, value):
        urls = value.split(',')
        validate_url = URLValidator()
        for url in urls:
            url = url.strip()
            if url:
                validate_url(url)

    def clean(self, value, model_instance):
        self.validate_urls(value)
        return value
