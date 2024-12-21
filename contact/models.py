from django.db import models

# contact message model
class ContactMessage(models.Model):
    first_name = models.CharField(
        max_length=100, 
        help_text="Enter your first name (max 100 characters)."
    )
    last_name = models.CharField(
        max_length=100, 
        help_text="Enter your last name (max 100 characters)."
    )
    email = models.EmailField(
        max_length=200, 
        help_text="Enter a valid email address (max 200 characters)."
    )
    subject = models.CharField(
        max_length=250, 
        help_text="Enter the subject of your message (max 250 characters)."
    )
    message = models.TextField(
        max_length=560, 
        help_text="Write your message here (max 560 characters)."
    )
    is_completed = models.BooleanField(
        default=False,
        help_text="Mark on read"   
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time this message was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time this message was last updated."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']  # Orders by newest messages first
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


# Contact Details model
class ContactDetail(models.Model):
    phone_number = models.CharField(
        max_length=15,
        help_text="Enter a valid phone number"      
    )
    contact_email = models.EmailField(
        max_length=100,
        help_text="Enter a valid contact email (max 100 characters)."
    )
    address = models.TextField(
        max_length=500,
        help_text="Enter the contact address (max 500 characters)."
    )
    facebook_link = models.URLField(
        max_length=255,
        default="https://facebook.com",
        help_text="Enter the Facebook profile URL (optional)."
    )
    twitter_link = models.URLField(
        max_length=255,
        default="https://x.com/?lang=en",
        help_text="Enter the Twitter profile URL (optional)."
    )
    instagram_link = models.URLField(
        max_length=255,
        default="https://www.instagram.com/",
        help_text="Enter the Instagram profile URL (optional)."
    )
    linkedin_link = models.URLField(
        max_length=255,
        default="https://bd.linkedin.com/",
        help_text="Enter the LinkedIn profile URL (optional)."
    )

    def __str__(self):
        return f"{self.contact_email} - {self.phone_number}"

    class Meta:
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Details"