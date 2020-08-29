# Generated by Django 2.2 on 2019-10-19 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('poll', models.CharField(max_length=200, verbose_name='Опрос')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=200, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='polls_choice', to='webapp.Choice', verbose_name='варианты')),
            ],
        ),
    ]
