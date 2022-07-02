# Generated by Django 4.0.5 on 2022-07-02 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_cost', models.PositiveSmallIntegerField()),
                ('datetime_start', models.DateTimeField(auto_now_add=True)),
                ('duration_choice', models.PositiveSmallIntegerField(choices=[(10, '10 minutes'), (60, '1 hour'), (1440, '1 day')], default=10)),
                ('datetime_end', models.DateTimeField(blank=True, null=True)),
                ('is_ended', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.car')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveSmallIntegerField()),
                ('order_datetime_end', models.DateTimeField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auction')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.company')),
            ],
            options={
                'unique_together': {('company', 'auction')},
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Repair'), (2, 'Maintenance')])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('offer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auctions.offer')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.service'),
        ),
    ]
