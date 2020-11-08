from django.urls import path, include
from .models import Plan
from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','name','tipoPlan','p_internet','p_fibraOptica','p_tvCable',
        'p_canalesPremium','p_telefoniaFija','p_internetMovilIlimitado','p_minutosLibres',
        'p_redesSocialesGratis','price']

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','name','tipoPlan']
    search_fields = ['id','name','tipoPlan']
    serializer_class = PlanSerializer

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]