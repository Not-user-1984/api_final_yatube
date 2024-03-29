# Generated by Django 2.2.16 on 2022-10-11 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_follow_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Выберите группу', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group', verbose_name='Группа'),
        ),
    ]
