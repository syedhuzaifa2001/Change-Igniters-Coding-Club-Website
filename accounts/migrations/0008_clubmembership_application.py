# Generated by Django 4.2 on 2023-04-26 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_clubapplication_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmembership',
            name='application',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='accounts.clubapplication'),
        ),
    ]