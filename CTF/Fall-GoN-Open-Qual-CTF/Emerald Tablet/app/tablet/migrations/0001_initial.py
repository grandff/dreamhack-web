from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscriber', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('key', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('inscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tablet.inscription')),
            ],
        ),
    ]
