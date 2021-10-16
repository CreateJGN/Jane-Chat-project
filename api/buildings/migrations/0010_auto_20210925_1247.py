# Generated by Django 3.2.7 on 2021-09-25 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0009_auto_20210629_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='buildings.building', verbose_name='parent id'),
        ),
        migrations.AlterField(
            model_name='building',
            name='broken_utilities',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='broken utilities'),
        ),
        migrations.AlterField(
            model_name='building',
            name='certified_expert',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='certified expert'),
        ),
        migrations.AlterField(
            model_name='building',
            name='disconnected_utilities',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='disconnected utilities'),
        ),
        migrations.AlterField(
            model_name='building',
            name='examination_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='examination year'),
        ),
        migrations.AlterField(
            model_name='building',
            name='land_registry_number',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='land registry number'),
        ),
        migrations.AlterField(
            model_name='building',
            name='observations',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='observations'),
        ),
        migrations.AlterField(
            model_name='building',
            name='proximal_utilities_description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='proximal utilities description'),
        ),
        migrations.AlterField(
            model_name='building',
            name='public_owners',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='public owners'),
        ),
        migrations.AlterField(
            model_name='building',
            name='registration_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='registration number'),
        ),
        migrations.AlterField(
            model_name='building',
            name='year_built',
            field=models.IntegerField(blank=True, null=True, verbose_name='year built'),
        ),
    ]