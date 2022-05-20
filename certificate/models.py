from django.db import models
import qrcode
from django.utils.translation import gettext_lazy as _
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Course(models.Model):
    name = models.CharField(_("Kurs nomi"), max_length=255, null=True)
    description = models.TextField(_("Text"), null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    Months = (
        ('yanvar', _('Yanvar')),
        ('fevral', _('Fevral')),
        ('mart', _('Mart')),
        ('aprel', _('Aprel')),
        ('may', _('May')),
        ('iyun', _('Iyun')),
        ('iyul', _('Iyul')),
        ('avgust', _('Avgust')),
        ('sentabr', _('Sentabr')),
        ('oktabr', _('Oktabr')),
        ('dekabr', _('Dekabr')),
    )

    familiya = models.CharField(_("Familiya"), max_length=255, blank=True, null=True)
    ism = models.CharField(_("Ism"), max_length=255, blank=True, null=True)
    sharf = models.CharField(_("Sharf"), max_length=255, blank=True, null=True, default=" ")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.CharField(_("Kurs boshlangan kun"),max_length=3,  null=True, blank=True)
    end_date = models.CharField(_("Kurs tugagan kun"), max_length=3, null=True, blank=True)
    month = models.CharField(_("Oy"), max_length=50, null=True, blank=True, default="yanvar", choices=Months)
    cer_nomer = models.BigIntegerField(_("Sertifikat raqami"), default=0, null=True)
    qr_code = models.ImageField(_("QR Code"), upload_to='qr_codes/', default="qe.png")
    status = models.BooleanField(_("Status"), default=True)

    def __str__(self):
        return f"{self.familiya} {self.ism} {self.sharf}"

    # def save(self, *args, **kwargs):
    #     super(Certificate, self).save(*args, **kwargs)
    #     # data = f"{self.familiya} {self.ism} {self.sharf}"
    #     data = "https://dtm.uz/page/ilmiy_markaz/"
    #     qrcode_img = qrcode.make(data=data)
    #     canvas = Image.new("RGB", (500, 500), "white")
    #     ImageDraw.Draw(canvas)
    #     canvas.paste(qrcode_img)
    #     filename = f'qr_code-{self.cer_nomer}.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(filename, File(buffer), save=False)
    #     canvas.close()

    class Meta:
        # filter = ['id']
        verbose_name = _('Sertifikat')
        verbose_name_plural = _('Sertifikatlar')
