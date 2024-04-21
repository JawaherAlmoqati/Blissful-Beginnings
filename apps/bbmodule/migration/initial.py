from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Makeup artists', models.CharField(max_length=50)),
                ('Hair stylists', models.CharField(max_length=50)),
                ('Photographers', models.CharField(max_length=50)),
                ('Bridemaid', models.CharField(max_length=50)),
                ('Price', models.FloatField(default=0.0)),
            ],
        ),
    ]