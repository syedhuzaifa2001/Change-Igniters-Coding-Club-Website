# Generated by Django 4.2 on 2023-04-26 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('criteria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_size', models.IntegerField(choices=[(1, 'One Member'), (2, 'Two Members'), (3, 'Three Members'), (4, 'Four Members')])),
                ('rank', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')], null=True)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='events.event')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.team')),
                ('team_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_lead', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
