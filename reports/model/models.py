# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

# In forms.py...
from django import forms



class Algorithmversions(models.Model):
    algo_version = models.CharField(db_column='Algo_version', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'algorithmversions'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Autorun(models.Model):
    cycle_id = models.IntegerField(primary_key=True)
    algo_version = models.CharField(max_length=200, blank=True)
    params = models.CharField(max_length=600, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    avg_score = models.FloatField(blank=True, null=True)
    crash_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorun'


class Autorunvideo(models.Model):
    autorunvideo_id = models.IntegerField(primary_key=True)
    cycle = models.ForeignKey(Autorun, blank=True, null=True)
    video = models.ForeignKey('Videos', blank=True, null=True)
    average_score = models.FloatField(blank=True, null=True)
    avexception = models.CharField(max_length=600, blank=True)
    variance_score = models.FloatField(blank=True, null=True)
    final_score = models.FloatField(blank=True, null=True)
    aws_output = models.CharField(max_length=600, blank=True)

    class Meta:
        managed = False
        db_table = 'autorunvideo'


class Autorunvideoframe(models.Model):
    autorunvideoframe_id = models.IntegerField(primary_key=True)
    cycle = models.ForeignKey(Autorun, blank=True, null=True)
    video = models.ForeignKey('Videos', blank=True, null=True)
    frame_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    frame_exception = models.CharField(max_length=600, blank=True)

    class Meta:
        managed = False
        db_table = 'autorunvideoframe'


class AutorunvideoframeCopy1(models.Model):
    cycle_id = models.IntegerField(blank=True, null=True)
    video_id = models.IntegerField(blank=True, null=True)
    frame_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    frame_exception = models.CharField(max_length=600, blank=True)

    class Meta:
        managed = False
        db_table = 'autorunvideoframe_copy1'


class Crashcycle(models.Model):
    cycle_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'crashcycle'


class Crashrun(models.Model):
    cycle_id = models.IntegerField(primary_key=True)
    algo_version = models.CharField(max_length=200, blank=True)
    params = models.CharField(max_length=600, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    crash_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crashrun'


class Crashrunvideo(models.Model):
    crashrunvideo_id = models.IntegerField(primary_key=True)
    cycle = models.ForeignKey(Crashrun, blank=True, null=True)
    video = models.ForeignKey('Videos', blank=True, null=True)
    crvexception = models.CharField(max_length=600, blank=True)

    class Meta:
        managed = False
        db_table = 'crashrunvideo'


class Cycle(models.Model):
    cycle_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cycle'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Generalparams(models.Model):
    param_name = models.CharField(primary_key=True, max_length=45)
    param_val = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'generalparams'


class GetMovieScore(models.Model):
    video_name = models.CharField(max_length=200, blank=True)
    algo_version1 = models.CharField(max_length=200, blank=True)
    variance1 = models.FloatField(blank=True, null=True)
    average_score1 = models.FloatField(blank=True, null=True)
    algo_version2 = models.CharField(max_length=200, blank=True)
    variance2 = models.FloatField(blank=True, null=True)
    average_score2 = models.FloatField(blank=True, null=True)
    difference = models.FloatField(db_column='Difference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'get_movie_score'


class GetMovieScoreByAlgo12(models.Model):
    video_name = models.CharField(max_length=200, blank=True)
    algo_version1 = models.CharField(max_length=200, blank=True)
    variance1 = models.FloatField(blank=True, null=True)
    average_score1 = models.FloatField(blank=True, null=True)
    algo_version2 = models.CharField(max_length=200, blank=True)
    variance2 = models.FloatField(blank=True, null=True)
    average_score2 = models.FloatField(blank=True, null=True)
    difference = models.FloatField(db_column='Difference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'get_movie_score_by_algo12'


class Parameters(models.Model):
    parameter_id = models.IntegerField(primary_key=True)
    cycle_id = models.IntegerField(blank=True, null=True)
    algo_version = models.CharField(db_column='Algo_version', max_length=45, blank=True)  # Field name made lowercase.
    param_name = models.CharField(max_length=45, blank=True)
    param_min = models.FloatField(blank=True, null=True)
    param_max = models.FloatField(blank=True, null=True)
    param_change = models.FloatField(blank=True, null=True)
    param_default = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameters'


class Videos(models.Model):
    video_id = models.IntegerField(primary_key=True)
    video_name = models.CharField(max_length=200, blank=True)
    num_of_frames = models.IntegerField(blank=True, null=True)
    video_path = models.CharField(max_length=300, blank=True)
    ffmpeg = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'videos'


class View1(models.Model):
    cycle_id = models.IntegerField()
    algo_version = models.CharField(max_length=200, blank=True)
    video_name = models.CharField(max_length=200, blank=True)
    average_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view1'


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
