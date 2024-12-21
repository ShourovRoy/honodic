from django.db import models

# slider model
class Slider(models.Model):
    title = models.CharField(
        max_length=100, 
        default="", 
        help_text="Enter the slider title. This will appear prominently on the slider."
    )
    desc = models.TextField(
        max_length=500, 
        default="", 
        help_text="Enter a brief description to display on the slider (max 500 characters)."
    )
    button_name = models.CharField(
        max_length=20, 
        default="Click Me", 
        help_text="Text to display on the slider button (e.g., 'Learn More')."
    )
    image = models.ImageField(
        upload_to="home/sliders/", 
        null=True, 
        help_text="Upload an image for the slider. Recommended size: 1920x1080px."
    )
    button_url = models.URLField(
        help_text="Enter the URL where the button should redirect when clicked."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when the slider was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when the slider was last updated."
    )

    def __str__(self):
        return self.title



# about model
class AboutDetail(models.Model):
    title = models.CharField(
        max_length=100, 
        default="", 
        help_text="Enter the title for the About section. This will be prominently displayed."
    )
    desc = models.TextField(
        max_length=300, 
        default="", 
        help_text="Provide a brief description about your business or organization (max 300 characters)."
    )
    featured_image = models.ImageField(
        upload_to="home/images/", 
        help_text="Upload an image to visually represent the About section. Recommended size: 800x600px."
    )
    video_link = models.URLField(
        default="", 
        help_text="Enter a URL to a video (e.g., a YouTube or Vimeo link) to include in the About section."
    )
    video = models.FileField(
        upload_to="home/videos/", 
        help_text="Upload a video file to feature in the About section. Supported formats: MP4, AVI, etc."
    )
    button_name = models.CharField(
        max_length=50, 
        default="Click me", 
        help_text="Enter the text for the button (e.g., 'Learn More')."
    )
    button_link = models.URLField(
        default="", 
        help_text="Provide the URL where the button should redirect when clicked."
    )

    def __str__(self) -> str:
        return self.title


# Unique feature model
class UniqueFeature(models.Model):
    title = models.CharField(
        max_length=120, 
        default="", 
        help_text="Enter a title for the unique feature (up to 120 characters)."
    )
    image = models.ImageField(
        upload_to="home/images/",
        help_text="Upload an image that represents this unique feature."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when this feature was created. Automatically set when the object is first created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when this feature was last updated. Automatically updated on every save."
    )

    def __str__(self):
        return self.title


# featured product details model
class FeaturedProductDetail(models.Model):
    title = models.CharField(
        max_length=300, 
        default="", 
        help_text="Enter the title of the featured product (up to 300 characters)."
    )
    desc = models.TextField(
        max_length=500, 
        default="", 
        help_text="Provide a brief description of the featured product (up to 500 characters)."
    )

    def __str__(self):
        return self.title
