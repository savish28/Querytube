from django.db import models

class Query(models.Model):
	query = models.CharField(max_length=200,unique = True)

class Video(models.Model):
	title = models.CharField(max_length=200)
	desc = models.CharField(max_length=500)
	videoId = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField()
	thumbnail = models.CharField(max_length=200)
	channelId = models.CharField(max_length=200)
	channelTitle = models.CharField(max_length=200)
	query = models.ForeignKey(Query,on_delete = models.DO_NOTHING)

