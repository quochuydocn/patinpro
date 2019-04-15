# Generated by Django 2.1 on 2019-04-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listgiay',
            name='TimeReturn',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time returns'),
        ),
        migrations.AlterField(
            model_name='listgiay',
            name='Borrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listgiay',
            name='TimeBorrow',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Time borrows'),
        ),
        migrations.AlterField(
            model_name='listgiay',
            name='TotalTimeUsing',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Used time'),
        ),
    ]
