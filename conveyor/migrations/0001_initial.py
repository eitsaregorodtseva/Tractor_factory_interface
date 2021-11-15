# Generated by Django 3.2.8 on 2021-11-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ButtonsBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buttons_block_number', models.IntegerField()),
                ('count_click', models.IntegerField()),
                ('status_block', models.CharField(max_length=10)),
                ('posts', models.ManyToManyField(related_name='posts', related_query_name='posts_set', to='conveyor.PostsState')),
            ],
        ),
    ]
