# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 21:18
from __future__ import unicode_literals

from django.db import migrations


def create_companies(apps, schema_editor):
    Company = apps.get_model('reports', 'Company')

    Company.objects.create(
        name='cocacolacanada',
        page_id='cocacolacanada',
    )

    Company.objects.create(
        name='pepsi',
        page_id='pepsi',
    )


def delete_companies(apps, schema_editor):
    Company = apps.get_model('reports', 'Company')
    Company.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_companies, delete_companies),
    ]