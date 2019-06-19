# Generated by Django 2.0 on 2019-06-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20190612_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='house_type',
            field=models.CharField(choices=[('0', '其它'), ('1', '单间'), ('2', '合租'), ('3', '一室一厅'), ('4', '两室一厅')], default='1', max_length=20, verbose_name='户型'),
        ),
    ]