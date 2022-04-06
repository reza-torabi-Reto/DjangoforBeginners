# Generated by Django 4.0.3 on 2022-03-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی پی')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='blog.ipaddress', verbose_name='بازدیدها'),
        ),
    ]
