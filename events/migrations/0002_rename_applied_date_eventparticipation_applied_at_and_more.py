# Generated by Django 4.2 on 2023-04-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventparticipation',
            old_name='applied_date',
            new_name='applied_at',
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, default='\\media\\static-images\\events\\event1.jpg', upload_to='events_pics'),
        ),
        migrations.AddField(
            model_name='eventparticipation',
            name='cover_picture',
            field=models.ImageField(blank=True, default='\\media\\participations_coverpics\\TeamBTC.png', upload_to='participations_coverpics'),
        ),
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, default='\\media\teams_logos\\TeamBTC.png', upload_to='teams_logos'),
        ),
    ]
