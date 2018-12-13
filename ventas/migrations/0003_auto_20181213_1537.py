# Generated by Django 2.1.4 on 2018-12-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_post_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreproducto', models.CharField(max_length=150)),
                ('costopresupuesto', models.CharField(max_length=150)),
                ('costoreal', models.CharField(max_length=150)),
                ('notaadicional', models.TextField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]