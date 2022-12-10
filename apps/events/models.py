from django.db import models

# Create your models here.


class Events(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    description = models.TextField()
    logo = models.FileField()


class RaceSeries(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    logo = models.FileField()
    slider_logo = models.FileField()
    small_logo = models.FileField()

    def __str__(self) -> str:
        return self.name


class Races(models.Model):
    race_series = models.ForeignKey(RaceSeries, on_delete=models.CASCADE,null=True, blank=True, related_name='races')
    name = models.CharField(max_length=200)
    zwift_id = models.IntegerField()
    start_time = models.DateTimeField()


class ZwiftResult(models.Model):
    zwift_id = models.IntegerField(null=True, blank=True)
    DT_RowId = models.CharField(null=True, blank=True, max_length=200)
    ftp = models.CharField(null=True, blank=True, max_length=200)
    friend = models.CharField(null=True, blank=True, max_length=200)
    pt = models.CharField(null=True, blank=True, max_length=200)
    label = models.CharField(null=True, blank=True, max_length=200)
    zid = models.CharField(null=True, blank=True, max_length=200)
    pos = models.CharField(null=True, blank=True, max_length=200, verbose_name="Position")
    position_in_cat = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(null=True, blank=True, max_length=200, verbose_name="Rider")
    cp = models.CharField(null=True, blank=True, max_length=200)
    zwid = models.CharField(null=True, blank=True, max_length=200)
    res_id = models.CharField(null=True, blank=True, max_length=200)
    lag = models.CharField(null=True, blank=True, max_length=200)
    uid = models.CharField(null=True, blank=True, max_length=200)
    time = models.CharField(null=True, blank=True, max_length=200)
    time_gun = models.CharField(null=True, blank=True, max_length=200)
    gap = models.CharField(null=True, blank=True, max_length=200)
    vtta = models.CharField(null=True, blank=True, max_length=200)
    vttat = models.CharField(null=True, blank=True, max_length=200)
    male = models.CharField(null=True, blank=True, max_length=200)
    tid = models.CharField(null=True, blank=True, max_length=200)
    topen = models.CharField(null=True, blank=True, max_length=200)
    tname = models.CharField(null=True, blank=True, max_length=200)
    tc = models.CharField(null=True, blank=True, max_length=200)
    tbc = models.CharField(null=True, blank=True, max_length=200)
    tbd = models.CharField(null=True, blank=True, max_length=200)
    zeff = models.CharField(null=True, blank=True, max_length=200)
    category = models.CharField(null=True, blank=True, max_length=200)
    height = models.CharField(null=True, blank=True, max_length=200)
    flag = models.CharField(null=True, blank=True, max_length=200)
    avg_hr = models.CharField(null=True, blank=True, max_length=200)
    max_hr = models.CharField(null=True, blank=True, max_length=200)
    hrmax = models.CharField(null=True, blank=True, max_length=200)
    hrm = models.CharField(null=True, blank=True, max_length=200)
    weight = models.CharField(null=True, blank=True, max_length=200)
    power_type = models.CharField(null=True, blank=True, max_length=200)
    display_pos = models.CharField(null=True, blank=True, max_length=200)
    src = models.CharField(null=True, blank=True, max_length=200)
    age = models.CharField(null=True, blank=True, max_length=200)
    zada = models.CharField(null=True, blank=True, max_length=200)
    note = models.CharField(null=True, blank=True, max_length=200)
    div = models.CharField(null=True, blank=True, max_length=200)
    divw = models.CharField(null=True, blank=True, max_length=200)
    skill = models.CharField(null=True, blank=True, max_length=200)
    skill_b = models.CharField(null=True, blank=True, max_length=200)
    skill_gain = models.CharField(null=True, blank=True, max_length=200)
    np = models.CharField(null=True, blank=True, max_length=200)
    hrr = models.CharField(null=True, blank=True, max_length=200)
    hreff = models.CharField(null=True, blank=True, max_length=200)
    avg_power = models.CharField(null=True, blank=True, max_length=200)
    avg_wkg = models.CharField(null=True, blank=True, max_length=200)
    wkg_ftp = models.CharField(null=True, blank=True, max_length=200)
    wftp = models.CharField(null=True, blank=True, max_length=200)
    wkg_guess = models.CharField(null=True, blank=True, max_length=200)
    wkg1200 = models.CharField(null=True, blank=True, max_length=200)
    wkg300 = models.CharField(null=True, blank=True, max_length=200)
    wkg120 = models.CharField(null=True, blank=True, max_length=200)
    wkg60 = models.CharField(null=True, blank=True, max_length=200)
    wkg30 = models.CharField(null=True, blank=True, max_length=200)
    wkg15 = models.CharField(null=True, blank=True, max_length=200)
    wkg5 = models.CharField(null=True, blank=True, max_length=200)
    w1200 = models.CharField(null=True, blank=True, max_length=200)
    w300 = models.CharField(null=True, blank=True, max_length=200)
    w120 = models.CharField(null=True, blank=True, max_length=200)
    w60 = models.CharField(null=True, blank=True, max_length=200)
    w30 = models.CharField(null=True, blank=True, max_length=200)
    w15 = models.CharField(null=True, blank=True, max_length=200)
    w5 = models.CharField(null=True, blank=True, max_length=200)
    is_guess = models.CharField(null=True, blank=True, max_length=200)
    upg = models.CharField(null=True, blank=True, max_length=200)
    penalty = models.CharField(null=True, blank=True, max_length=200)
    reg = models.CharField(null=True, blank=True, max_length=200)
    fl = models.CharField(null=True, blank=True, max_length=200)
    pts = models.CharField(null=True, blank=True, max_length=200)
    pts_pos = models.CharField(null=True, blank=True, max_length=200)
    info = models.CharField(null=True, blank=True, max_length=200)
    info_notes = models.CharField(null=True, blank=True, max_length=200)
    log = models.CharField(null=True, blank=True, max_length=200)
    lead = models.CharField(null=True, blank=True, max_length=200)
    sweep = models.CharField(null=True, blank=True, max_length=200)
    actid = models.CharField(null=True, blank=True, max_length=200)
    anal = models.CharField(null=True, blank=True, max_length=200)

