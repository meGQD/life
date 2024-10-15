from django.db import migrations, models
import datetime

def set_default_birth_and_death_dates(apps, schema_editor):
    User = apps.get_model('core', 'User')
    for user in User.objects.all():
        if not user.birth_date:
            user.birth_date = datetime.date(1990, 1, 1)  # Default birth date
        if not user.expected_death_date:
            user.expected_death_date = datetime.date(2060, 1, 1)  # Default death date
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.date(1990, 1, 1)),  # Enforce non-null with default
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='expected_death_date',
            field=models.DateField(default=datetime.date(2060, 1, 1)),  # Enforce non-null with default
            preserve_default=False,
        ),
        migrations.RunPython(set_default_birth_and_death_dates),  # Apply defaults to existing users
    ]
