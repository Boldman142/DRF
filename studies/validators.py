from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        correct_data = "https://www.youtube.com/"
        tmp_val = dict(value).get(self.field)
        if not tmp_val:
            return
        if correct_data not in tmp_val:
            raise ValidationError('You can add url only from YOUTUBE')
