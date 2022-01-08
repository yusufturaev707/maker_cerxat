from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Certificate(models.Model):
    familiya = models.CharField(max_length=255, blank=True, null=True, verbose_name="Familiya")
    ism = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ism")
    sharf = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sharf")
    kurs_kuni = models.DateField(null=True, blank=True, verbose_name="Kurs o\'tagan vaqti")
    cer_nomer = models.BigIntegerField(default=0, null=True, verbose_name="Sertifikat raqami")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, )

    def __str__(self):
        return f"{self.familiya} {self.ism} {self.sharf}"

    def save(self, *args, **kwargs):
        self.cer_nomer = "{:05d}".format(self.cer_nomer)
        # data = f"{self.familiya} {self.ism} {self.sharf}"
        data = "https://dtm.uz/page/ilmiy_markaz/"
        qrcode_img = qrcode.make(data=data)
        canvas = Image.new("RGB", (500, 500), "white")
        ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        filename = f'qr_code-{self.cer_nomer}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(filename, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
