# Generated by Django 2.0 on 2019-06-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_house_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='apartment',
            field=models.CharField(choices=[('0', '不限'), ('1', '单间'), ('2', '合租'), ('3', '一室一厅'), ('4', '两室一厅'), ('5', '其它')], default='0', max_length=20, verbose_name='户型'),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(choices=[('0', '不限'), ('1', '整租'), ('2', '合租')], default='1', max_length=20, verbose_name='类型（整租，合租）'),
        ),
    ]
