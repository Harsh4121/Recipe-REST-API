# Generated by Django 5.0.1 on 2024-01-25 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_receipe_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegistration',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.AlterField(
            model_name='receipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='receipe_images/'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_name',
            field=models.CharField(max_length=255),
        ),
    ]