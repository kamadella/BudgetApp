# Generated by Django 4.0.4 on 2022-06-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgethandling', '0004_alter_transaction_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='sum',
            new_name='suma',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='type',
            new_name='typek',
        ),
    ]
