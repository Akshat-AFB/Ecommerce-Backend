# your_app/pagination.py
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # default `limit` if not provided
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 100
