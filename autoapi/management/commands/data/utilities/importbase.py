from rest_framework import viewsets

from ..utilities.pagination import MyPageNumberPagination
from ..utilities.permissions import {app_name}Permission
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication