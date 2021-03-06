# Generated by Django 2.1.1 on 2018-11-20 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181120_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='todo_list',
        ),
        migrations.AddField(
            model_name='item',
            name='todo_task_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.IntegerField(choices=[(1, 'In Progress'), (2, 'Complete'), (3, 'Pending')]),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
