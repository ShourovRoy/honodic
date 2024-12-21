from django.db import models

# Category model

class Category(models.Model):
    title = models.CharField(
        max_length=100, 
        unique=True, 
        help_text="Enter a unique title for the category."
    )
    desc = models.TextField(
        max_length=400, 
        blank=True, 
        help_text="Provide a short description of the category (max 400 characters)."
    )
    image = models.ImageField(
        upload_to="categories/", 
        blank=True, 
        null=True, 
        help_text="Upload an image for the category."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when the category was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when the category was last updated."
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]  # Newest categories first

    def __str__(self):
        return f"{self.title} ({self.created_at.strftime('%Y-%m-%d')})"
