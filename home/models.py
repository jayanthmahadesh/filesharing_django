from django.db import models
import uuid
import os
class folder(modles.Model):
    uid = models.UUIDField(editable=False,primary_key=True,default=uuid.uuid4)
    created_at=models.DateField(auto_now=True)


def get_upload_path(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)

class files(models.Model):
    folder = models.ForeignKey(folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at=models.DateField(auto_now=True)

# Create your models here.
