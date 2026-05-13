from django.db import models


class Category(models.Model):
    """
    Product Category
    Like :
            coffee,
            sandwich,
            hot-drinks,
            cold-bar,
            ...
    """
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, help_text="ایموجی یا متن کوتاه مثل ☕")
    priority_order = models.IntegerField(default=0)

    def __str__(self):
        if self.icon:
            return f'{self.name}--({self.icon})'
        return f'{self.name}'

    class Meta:
        ordering = ['priority_order']


class MenuItem(models.Model):
    """
    Menu Item:
            black Coffee
            chocolate cake
            latte
            afogato
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_available = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    preparation_time = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    priority_order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}--({self.category})'

    class Meta:
        ordering = ['category__priority_order', 'priority_order', 'category']
