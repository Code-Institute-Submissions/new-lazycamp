# Generated by Django 3.0.6 on 2020-06-23 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Campspot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('county', models.CharField(max_length=254)),
                ('postcode', models.CharField(max_length=254)),
                ('postal_district', models.CharField(max_length=254)),
                ('first_line_address', models.CharField(max_length=254)),
                ('address_town_or_city', models.CharField(max_length=254)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('arrive_anytime', models.BooleanField(default=True)),
                ('arrive_dawn_to_dusk', models.BooleanField(default=True)),
                ('is_available', models.BooleanField(default=True)),
                ('dogs_welcome', models.BooleanField(default=False)),
                ('wi_fi', models.BooleanField(default=True)),
                ('good_phone_signal', models.BooleanField(default=True)),
                ('electric', models.BooleanField(default=True)),
                ('motorhome_service_point', models.TextField()),
                ('host_brief', models.TextField()),
                ('bare_all', models.TextField()),
                ('nearest_toilet_and_shower', models.TextField()),
                ('public_transport_options', models.TextField()),
                ('local_eatery_and_shop', models.TextField()),
                ('campspot_email', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='campspots.Category')),
            ],
        ),
    ]