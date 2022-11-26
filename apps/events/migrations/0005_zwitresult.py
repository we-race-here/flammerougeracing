# Generated by Django 4.0.8 on 2022-11-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_races_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZwitResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DT_RowId', models.CharField(max_length=200)),
                ('ftp', models.CharField(max_length=200)),
                ('friend', models.CharField(max_length=200)),
                ('pt', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
                ('zid', models.CharField(max_length=200)),
                ('pos', models.CharField(max_length=200)),
                ('position_in_cat', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('cp', models.CharField(max_length=200)),
                ('zwid', models.CharField(max_length=200)),
                ('res_id', models.CharField(max_length=200)),
                ('lag', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('time_gun', models.CharField(max_length=200)),
                ('gap', models.CharField(max_length=200)),
                ('vtta', models.CharField(max_length=200)),
                ('vttat', models.CharField(max_length=200)),
                ('male', models.CharField(max_length=200)),
                ('tid', models.CharField(max_length=200)),
                ('topen', models.CharField(max_length=200)),
                ('tname', models.CharField(max_length=200)),
                ('tc', models.CharField(max_length=200)),
                ('tbc', models.CharField(max_length=200)),
                ('tbd', models.CharField(max_length=200)),
                ('zeff', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
                ('avg_hr', models.CharField(max_length=200)),
                ('max_hr', models.CharField(max_length=200)),
                ('hrmax', models.CharField(max_length=200)),
                ('hrm', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('power_type', models.CharField(max_length=200)),
                ('display_pos', models.CharField(max_length=200)),
                ('src', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('zada', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=200)),
                ('div', models.CharField(max_length=200)),
                ('divw', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('skill_b', models.CharField(max_length=200)),
                ('skill_gain', models.CharField(max_length=200)),
                ('np', models.CharField(max_length=200)),
                ('hrr', models.CharField(max_length=200)),
                ('hreff', models.CharField(max_length=200)),
                ('avg_power', models.CharField(max_length=200)),
                ('avg_wkg', models.CharField(max_length=200)),
                ('wkg_ftp', models.CharField(max_length=200)),
                ('wftp', models.CharField(max_length=200)),
                ('wkg_guess', models.CharField(max_length=200)),
                ('wkg1200', models.CharField(max_length=200)),
                ('wkg300', models.CharField(max_length=200)),
                ('wkg120', models.CharField(max_length=200)),
                ('wkg60', models.CharField(max_length=200)),
                ('wkg30', models.CharField(max_length=200)),
                ('wkg15', models.CharField(max_length=200)),
                ('wkg5', models.CharField(max_length=200)),
                ('w1200', models.CharField(max_length=200)),
                ('w300', models.CharField(max_length=200)),
                ('w120', models.CharField(max_length=200)),
                ('w60', models.CharField(max_length=200)),
                ('w30', models.CharField(max_length=200)),
                ('w15', models.CharField(max_length=200)),
                ('w5', models.CharField(max_length=200)),
                ('is_guess', models.CharField(max_length=200)),
                ('upg', models.CharField(max_length=200)),
                ('penalty', models.CharField(max_length=200)),
                ('reg', models.CharField(max_length=200)),
                ('fl', models.CharField(max_length=200)),
                ('pts', models.CharField(max_length=200)),
                ('pts_pos', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
                ('info_notes', models.CharField(max_length=200)),
                ('log', models.CharField(max_length=200)),
                ('lead', models.CharField(max_length=200)),
                ('sweep', models.CharField(max_length=200)),
                ('actid', models.CharField(max_length=200)),
                ('anal', models.CharField(max_length=200)),
            ],
        ),
    ]
