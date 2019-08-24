# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_name = models.CharField(max_length=20)
    blog_body = models.TextField()
    blog_time = models.DateTimeField()
    blog_viewnumber = models.IntegerField(db_column='blog_viewNumber')  # Field name made lowercase.
    blog_likenumber = models.IntegerField(db_column='blog_likeNumber')  # Field name made lowercase.
    blog_state = models.IntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog'


class BlogTag(models.Model):
    blog_id = models.IntegerField(unique=True)
    tag_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'blog_tag'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    review_time = models.DateTimeField()
    review_body = models.TextField()
    return_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'tag'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=20)
    user_password = models.CharField(max_length=20)
    user_mail = models.CharField(unique=True, max_length=255)
    user_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
