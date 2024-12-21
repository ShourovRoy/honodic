from django.db import models

# Create your models here.
class SectionOneContent(models.Model):
    title = models.CharField(
        max_length=400, 
        default="", 
        help_text="Enter the main title for this section (up to 400 characters)."
    )
    sub_title = models.CharField(
        max_length=400, 
        default="", 
        help_text="Enter the subtitle or supporting title for this section (up to 400 characters)."
    )
    desc = models.TextField(
        max_length=550, 
        default="", 
        help_text="Provide a detailed description for this section (up to 550 characters)."
    )
    featured_image = models.ImageField(
        upload_to="about/images", 
        help_text="Upload the main image to be featured in this section."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when this section content was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when this section content was last updated."
    )

    def __str__(self):
        return self.title
    

# section two content
class SectionTwoContent(models.Model):
    title = models.CharField(
        max_length=300, 
        default="", 
        help_text="Enter the title for this section (up to 300 characters)."
    )
    desc = models.TextField(
        max_length=550, 
        default="", 
        help_text="Provide a detailed description for this section (up to 550 characters)."
    )
    featured_image = models.ImageField(
        upload_to="about/images", 
        help_text="Upload the main image to be featured in this section."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when this section content was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when this section content was last updated."
    )

    def __str__(self):
        return self.title


# create frequently asked questions
class FrequentlyAskedQuention(models.Model):
    title = models.CharField(
        max_length=200, 
        default="", 
        help_text="Enter the question title or summary (up to 200 characters)."
    )
    desc = models.TextField(
        max_length=450, 
        default="", 
        help_text="Provide the detailed answer or description for the question (up to 450 characters)."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when this FAQ was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when this FAQ was last updated."
    )

    def __str__(self):
        return self.title