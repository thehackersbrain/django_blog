# Generated by Django 2.2.3 on 2019-08-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_ctg_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='test', max_length=500),
            preserve_default=False,
        ),
    ]
