from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # 상속을 위해서만 쓰겠다는 의미
    class Meta:
        abstract = True