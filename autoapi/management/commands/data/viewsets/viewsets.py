from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import {model_name}
from ..serializers.{model_serializer} import {model_list_serializers}, {model_retrieve_serializers}, {model_write_serializers}
from ..utilities.importbase import *

class {viewset_name}(viewsets.ModelViewSet):
    serializer_class = {model_list_serializers}
    # permission_classes = [{app_name}Permission]
    # authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = {model_name}.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {{
    #     'id': ['exact'],
    # }}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return {model_write_serializers}
        elif self.action == 'retrieve':
            return {model_retrieve_serializers}
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

