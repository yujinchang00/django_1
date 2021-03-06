# Generated by Django 4.0.1 on 2022-02-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('KR', '한식'), ('EA', '양식'), ('CH', '중식'), ('JP', '일식'), ('SF', '분식'), ('BR', '베이커리'), ('BEV', '커피음료'), ('OTHERS', '그외')], max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]
