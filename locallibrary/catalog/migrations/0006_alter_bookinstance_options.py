# Generated by Django 4.0.2 on 2022-08-31 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['status', 'due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]