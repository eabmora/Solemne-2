from django.test import TestCase
from .models import Plan

# Create your tests here.

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            name= "Plan S",
            price= 15990
        )

        Plan.objects.create(
            name= "Plan M",
            price= 22990
        )

        Plan.objects.create(
            name= "Plan L",
            price= 29990
        )

        Plan.objects.create(
            name= "Plan XL",
            price= 35990
        )

    
    def test_plan_price(self):
        plan = Plan.objects.get(name="Plan S")
        self.assertEqual(plan.price, 15990)

    def test_assert_equal_generar_descuento(self):
        plan = Plan.objects.get(name="Plan M")
        self.assertEqual(plan.generarDescuento(), 0.1)

    def test_assert_equal_precio_final(self):
        plan = Plan.objects.get(name="Plan L")
        self.assertEqual(plan.calcularPrecioFinal(), 23992)

        plan = Plan.objects.get(name="Plan XL")
        self.assertEqual(plan.calcularPrecioFinal(), 21594)