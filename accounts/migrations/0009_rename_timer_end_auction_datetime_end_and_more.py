# Generated by Django 4.0.5 on 2022-06-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_is_finished_auction_is_company_chosen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='timer_end',
            new_name='datetime_end',
        ),
        migrations.RenameField(
            model_name='auction',
            old_name='timer_start',
            new_name='datetime_start',
        ),
        migrations.AddField(
            model_name='auction',
            name='task_id',
            field=models.IntegerField(default=0),
        ),
    ]
