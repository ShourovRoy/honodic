from django.db import models
from category.models import Category
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField(
        max_length=200, 
        help_text="Enter the product title. Make it descriptive and unique."
    )
    short_desc = models.TextField(
        max_length=400, 
        blank=True, 
        help_text="Enter a brief description of the product (max 400 characters)."
    )
    # desc = models.TextField(
    #     max_length=2000, 
    #     help_text="Enter a detailed description of the product (max 2000 characters)."
    # )
    image = models.ImageField(
        upload_to="products/", 
        blank=True, 
        null=True, 
        help_text="Upload a product image. Recommended size: 800x800px."
    )
    # price = models.FloatField(default=0.0, help_text="Enter product price.")
    categories = models.ManyToManyField(
        Category, 
        related_name="products", 
        help_text="Select one or more categories for the product."
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        blank=True, 
        help_text="Slug for the product URL. Leave blank to auto-generate."
    )
    is_featured = models.BooleanField(
        default=False, 
        help_text="Mark as featured to highlight this product."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when the product was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when the product was last updated."
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically generate a slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
