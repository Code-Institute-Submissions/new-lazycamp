# Generated by Django 3.0.6 on 2020-05-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_orderlineitem_pitch_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_book',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
