from rest_framework.pagination import PageNumberPagination


class ListPaginator(PageNumberPagination):
    page_size = 5
