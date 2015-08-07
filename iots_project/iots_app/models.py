from django.db import models

# Create your models here.
class Title(models.Model):
	name = models.CharField(max_length=20)
	notes = models.CharField(max_length=50)

class PushModel(models.Model):
    push_message = models.CharField(max_length=100)
    push_url = models.URLField()

    def __str__(self):
        return self.push_message

class Person(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()

class ShowPushMessage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    raw_data_id = models.IntegerField(blank=True, null=True)
    sent_message = models.TextField()
    sent_url = models.TextField(blank=True, null=True)
    sent_number = models.IntegerField(blank=True, null=True)
    recv_number = models.IntegerField(blank=True, null=True)
    open_number = models.IntegerField(blank=True, null=True)
    sent_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'show_push_message'

class ShowEndAlive(models.Model):
    uuid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    mac_address = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    product_id = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=32, blank=True, null=True)
    kernel_version = models.CharField(max_length=32, blank=True, null=True)
    cpu_model = models.CharField(max_length=64, blank=True, null=True)
    bios_version = models.CharField(max_length=16)
    graphics_model = models.CharField(max_length=128, blank=True, null=True)
    graphics_driver_version = models.CharField(max_length=32, blank=True, null=True)
    client_version = models.CharField(max_length=8, blank=True, null=True)
    online_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'show_end_alive'
        unique_together = (('id', 'bios_version'),)