# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=26)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=85)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=33)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=42)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=84)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookRank(models.Model):
    bookid = models.AutoField(db_column='BookId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=6, blank=True, null=True)
    href = models.CharField(max_length=26, blank=True, null=True)
    keyword1 = models.CharField(db_column='KeyWord1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword2 = models.CharField(db_column='KeyWord2', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword3 = models.CharField(db_column='KeyWord3', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword4 = models.CharField(db_column='KeyWord4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword5 = models.CharField(db_column='KeyWord5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword6 = models.CharField(db_column='KeyWord6', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword7 = models.CharField(db_column='KeyWord7', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword8 = models.CharField(db_column='KeyWord8', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword9 = models.CharField(db_column='KeyWord9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword10 = models.CharField(db_column='KeyWord10', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword11 = models.CharField(db_column='KeyWord11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword12 = models.CharField(db_column='KeyWord12', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword13 = models.CharField(db_column='KeyWord13', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword14 = models.CharField(db_column='KeyWord14', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword15 = models.CharField(db_column='KeyWord15', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword16 = models.CharField(db_column='KeyWord16', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword17 = models.CharField(db_column='KeyWord17', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword18 = models.CharField(db_column='KeyWord18', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword19 = models.CharField(db_column='KeyWord19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword20 = models.CharField(db_column='KeyWord20', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword21 = models.CharField(db_column='KeyWord21', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword22 = models.CharField(db_column='KeyWord22', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword23 = models.CharField(db_column='KeyWord23', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword24 = models.CharField(db_column='KeyWord24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword25 = models.CharField(db_column='KeyWord25', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword26 = models.CharField(db_column='KeyWord26', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword27 = models.CharField(db_column='KeyWord27', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword28 = models.CharField(db_column='KeyWord28', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword29 = models.CharField(db_column='KeyWord29', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword30 = models.CharField(db_column='KeyWord30', max_length=6, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=3, blank=True, null=True)
    writer = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_rank'


class BrsPerson(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=84)

    class Meta:
        managed = False
        db_table = 'brs_person'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=66)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=33)
    model = models.CharField(max_length=33)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=85)
    name = models.CharField(max_length=85)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=13)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Newbook(models.Model):
    newbookid = models.AutoField(db_column='NewBookId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=6, blank=True, null=True)
    href = models.CharField(max_length=26, blank=True, null=True)
    keyword1 = models.CharField(db_column='KeyWord1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword2 = models.CharField(db_column='KeyWord2', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword3 = models.CharField(db_column='KeyWord3', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword4 = models.CharField(db_column='KeyWord4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword5 = models.CharField(db_column='KeyWord5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword6 = models.CharField(db_column='KeyWord6', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword7 = models.CharField(db_column='KeyWord7', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword8 = models.CharField(db_column='KeyWord8', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword9 = models.CharField(db_column='KeyWord9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword10 = models.CharField(db_column='KeyWord10', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword11 = models.CharField(db_column='KeyWord11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword12 = models.CharField(db_column='KeyWord12', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword13 = models.CharField(db_column='KeyWord13', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword14 = models.CharField(db_column='KeyWord14', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword15 = models.CharField(db_column='KeyWord15', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword16 = models.CharField(db_column='KeyWord16', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword17 = models.CharField(db_column='KeyWord17', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword18 = models.CharField(db_column='KeyWord18', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword19 = models.CharField(db_column='KeyWord19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword20 = models.CharField(db_column='KeyWord20', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword21 = models.CharField(db_column='KeyWord21', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword22 = models.CharField(db_column='KeyWord22', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword23 = models.CharField(db_column='KeyWord23', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword24 = models.CharField(db_column='KeyWord24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword25 = models.CharField(db_column='KeyWord25', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword26 = models.CharField(db_column='KeyWord26', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword27 = models.CharField(db_column='KeyWord27', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword28 = models.CharField(db_column='KeyWord28', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword29 = models.CharField(db_column='KeyWord29', max_length=6, blank=True, null=True)  # Field name made lowercase.
    keyword30 = models.CharField(db_column='KeyWord30', max_length=6, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newbook'


class Sortkeywords(models.Model):
    skwid = models.AutoField(primary_key=True)
    skw = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sortkeywords'
