import re
from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        correct_data = "https://www.youtube.com/"
        tmp_val = dict(value).get(self.field)[:24]
        if correct_data != tmp_val:
            raise ValidationError('You can add url only from YOUTUBE')

