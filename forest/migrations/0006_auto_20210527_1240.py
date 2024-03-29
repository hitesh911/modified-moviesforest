# Generated by Django 3.2.2 on 2021-05-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forest', '0005_alter_post_screen_shots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='adventure', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='download_links',
            field=models.CharField(default=' {"480":"https://480", "720":"https://720","1080":"https://1080"}', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo_link',
            field=models.CharField(default='https://parrotsec.org/images/about/notebook.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(default='hollywood', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_caption',
            field=models.CharField(default='this is the caption for title', max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='trailer_link',
            field=models.CharField(default='https://tralerss', max_length=500),
        ),
    ]
