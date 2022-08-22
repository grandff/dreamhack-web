from django.db import migrations


def inscribe_flag(apps, schema_editor):
    Inscription = apps.get_model('tablet', 'Inscription')
    Content = apps.get_model('tablet', 'Content')
    
    inscription = Inscription(inscriber='The Sage', title='FLAG')
    content = Content(data=open('/flag', 'rt').read(), inscription=inscription)
    
    inscription.save()
    content.save()


class Migration(migrations.Migration):

    dependencies = [
        ('tablet', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(inscribe_flag),
    ]
