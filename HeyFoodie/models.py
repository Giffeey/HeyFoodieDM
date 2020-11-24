from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.safestring import mark_safe
from multiselectfield import MultiSelectField
import datetime

Day = (
    (1, "จันทร์"),
    (2, "อังคาร"),
    (3, "พุธ"),
    (4, "พฤหัสบดี"),
    (5, "ศุกร์"),
    (6, "เสาร์"),
    (7, "อาทิตย์"),
)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    storename = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    open_order = models.TimeField()
    close_order = models.TimeField()
    open_day = MultiSelectField(choices=Day, max_choices=7, max_length=20, null=False)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    fbpage = models.CharField(max_length=100, null=True)
    lineac = models.CharField(max_length=100, null=True)
    igac = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.storename


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Ingredient_Category(models.Model):
    ingredient_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=50, unique=True)
    Ingredient_category = models.ForeignKey(
        Ingredient_Category, on_delete=models.CASCADE
    )
    image = models.ImageField(blank=True, upload_to="Image", null=True)

    def __str__(self):
        return self.ingredient_name


class SaleSize(models.Model):
    salesize_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s %d" % (self.size, self.price)

    def setId(self, salesize_id):
        self.salesize_id = salesize_id


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient)
    salesize = models.ManyToManyField(SaleSize)
    image = models.ImageField(blank=True, upload_to="Image", null=True)

    def __str__(self):
        return self.name

    def setId(self, menu_id):
        self.menu_id = menu_id


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, null=True)
    image = models.ImageField(blank=True, upload_to="Image", null=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    def setId(self, customer_id):
        self.customer_id = customer_id


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ("WAITING", "Waiting"),
        ("COOKING", "Cooking"),
        ("READYTOPICKUP", "Ready To Pickup"),
        ("DONE", "Done"),
        ("CANCEL", "Cancel")
    )

    order_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.datetime.now)
    order_status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default="WAITING"
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s %s" % (self.order_id, self.order_status, self.customer)


class Order_detail(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    size = models.ForeignKey(SaleSize, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "%s x %s" % (self.menu, self.quantity)


class Payment(models.Model):
    PAYMENT_CHOICES = (
        ("CASH", "Cash"),
        ("CREDIT", "Credit/Debit"),
    )

    PAYMENT_STATUS = (("complete", "Complete"), ("waiting", "Waiting"), ("cancel", "Cancel"))

    payment_id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default="CASH")
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    purchase_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="waiting")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return " %s %d %s %s %s" % (
            self.order,
            self.amount,
            self.method,
            self.status,
            self.purchase_date,
        )


class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.customer, self.payment)

