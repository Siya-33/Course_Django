# Generated by Django 4.0.4 on 2022-06-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_student_birthday_alter_student_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('cno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('ccredit', models.DecimalField(decimal_places=1, max_digits=2)),
                ('cteacher', models.CharField(max_length=20)),
            ],
        ),
    ]
