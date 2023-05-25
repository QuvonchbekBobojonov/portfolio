from django.db import models

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=200)
    years = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ResumeBody(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    direction = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.direction


class Servers(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    icon_class = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='images/portfolio')

    def __str__(self):
        return self.name


class PortfolioType(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
