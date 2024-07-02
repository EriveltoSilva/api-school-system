from django.db import models

# Base class used for everyone
class Course(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural='Courses'
        ordering = ['title',]

    def __str__(self) -> str:
        return self.title
    
class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255)
    comment = models.TextField(blank=True, default='')
    review = models.DecimalField(max_digits=2, decimal_places=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural='Reviews'
        ordering = ['name', 'created_at']
        unique_together = ['email', 'course']

    def __str__(self) -> str:
        return f'{self.name} avaliou o curso com {self.review}'
    