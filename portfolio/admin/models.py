from django.db import models

class TextContent(models.Model):

    section_choices = {
        "about_me": "About Me",
    }
    section = models.CharField(max_length=none)
    order = models.IntegerField(default=0)
    description = models.TextField
    
    def __str__(self):
        return self.description

class Resume(models.Model):
    name = models.CharField(max_length=25)
    position = models.CharField(max_length=50)
    summary = models.TextField()
    def __str__(self):
        return self.name

class Skill(models.Model):
    category_choices = {
        "language" = "Language",
        "technology" = "Technology"
    }

    resume = models.ForeignKey(Resume)

    category = models.CharField(max_length=20, choices=category_choices)
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    img_url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class TechTimeline(models.Model):
    timePeriod = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.description

class Experience(models.Model):
    category_choices = {
        "project" = "Project"
        "career" = "Career"
    }

    resume = models.ForeignKey(Resume)

    category = models.CharField(max_length=25, choices=category_choices)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    description = models.TextField()
    resume_description = models.TextField()
    skills = models.ManyToManyField(Skill)
    tags = models.ManyToManyField(Tag)
    demo_link = models.CharField(max_length=255)
    begun = models.DateTimeField(blank=True)
    concluded = models.DateTimeField(blank=True)
    has_concluded = models.BooleanField()
    
    def __str__(self):
        return self.title

class ResumeBullet(models.Model):
    experience = models.ForeignKey(Experience, on_delete = models.CASCADE)
    order = models.PositiveIntegerField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Contact(models.Model):

    resume = models.OneToOneField(Resume)

    email = models.EmailField(max_length=100)
    country_code = models.CharField(max_length=2)
    number = models.CharField(max_length=10)
    linkedin = model.URLField(max_length=200)
    github = model.URLField(max_length=200)
    website = model.URLField(max_length=100)

    def __str__(self):
        return self.email

