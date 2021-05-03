# Generated by Django 3.2 on 2021-05-02 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=999999)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=999999)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
    ]
