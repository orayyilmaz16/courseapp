# Generated by Django 5.1.4 on 2024-12-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='courses.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(db_index=True, default='', max_length=50, unique=True),
        ),
    ]
