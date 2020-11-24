from rest_framework import serializers, fields
from .models import (
    Category,
    Ingredient_Category,
    Ingredient,
    Menu,
    Store,
    Day,
    Order,
    Order_detail,
    Customer,
    History
)
from .models import SaleSize, Payment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("category_id", "category_name")


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient_Category
        fields = ("ingredient_category_id", "name")


class IngredientSerializer(serializers.ModelSerializer):
    Ingredient_category = IngredientCategorySerializer()

    class Meta:
        model = Ingredient
        fields = ("ingredient_id", "ingredient_name", "Ingredient_category", "image")


class SalesizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleSize
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ingredient = IngredientSerializer(many=True)
    salesize = SalesizeSerializer(many=True)

    class Meta:
        model = Menu
        fields = ("menu_id", "name", "category", "ingredient", "salesize", "image")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    menu = MenuSerializer()
    size = SalesizeSerializer()

    class Meta:
        model = Order_detail
        fields = ("order_detail_id", "order", "menu", "size", "quantity")


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    open_day = fields.MultipleChoiceField(choices=Day)

    class Meta:
        model = Store
        fields = (
            "store_id",
            "storename",
            "detail",
            "open_time",
            "close_time",
            "open_day",
            "open_order",
            "close_order",
            "open_day",
            "email",
            "phone",
            "fbpage",
            "lineac",
            "igac",
            "address",
        )


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["image"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"