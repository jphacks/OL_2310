# Generated by Django 4.2.2 on 2023-10-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_book_lend_by_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='books', to='accounts.tag'),
        ),
    ]
