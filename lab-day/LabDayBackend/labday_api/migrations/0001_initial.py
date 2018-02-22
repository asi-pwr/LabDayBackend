# Generated by Django 2.0.2 on 2018-02-08 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('img', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('room', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
                ('topic', models.TextField(blank=True)),
                ('dor1_img', models.TextField(blank=True)),
                ('dor2_img', models.TextField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('info', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(blank=True)),
                ('img', models.TextField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('info', models.TextField(blank=True)),
                ('img', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_start', models.BigIntegerField(blank=True, default=0)),
                ('time_end', models.BigIntegerField(blank=True, default=0)),
                ('event_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='labday_api.Event')),
                ('path_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='labday_api.Path')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='speaker_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='labday_api.Speaker'),
        ),
    ]