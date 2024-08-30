# Generated by Django 5.1 on 2024-08-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0002_alter_patient_phone_alter_patient_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, null=True)),
                ('image', models.FileField(db_index=True, null=True, upload_to='donar_image')),
                ('Nationality', models.CharField(choices=[('Indian', 'Indian'), ('Others', 'Others')], max_length=100)),
                ('age', models.IntegerField(db_index=True, null=True)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=100)),
                ('email', models.CharField(db_index=True, max_length=200, null=True)),
                ('phone', models.BigIntegerField(db_index=True, null=True)),
                ('address', models.TextField(db_index=True, null=True)),
                ('blood_type', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('date_of_donation', models.DateField()),
                ('total_validation', models.IntegerField(db_index=True, null=True)),
                ('donation', models.CharField(choices=[('Whole blood', 'Whole blood'), ('Red cell', 'Red cell'), ('plasma', 'plasma'), ('platelate', 'platelate')], max_length=100)),
                ('donar_status', models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('pending', 'pending')], max_length=100)),
                ('volume', models.BigIntegerField(db_index=True, null=True)),
                ('hemoglobin', models.IntegerField(db_index=True, null=True)),
                ('wieght', models.IntegerField(db_index=True, null=True)),
                ('medical_history', models.TextField(db_index=True, null=True)),
                ('overall_health', models.CharField(choices=[('good', 'good'), ('best', 'best'), ('need improvement', 'need improvement')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]