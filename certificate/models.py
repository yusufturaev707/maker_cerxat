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
    qr_code = models.ImageField(upload_to='qr_codes/', default='qe.png', blank=True, null=True, )

    def __str__(self):
        return f"{self.ism}"

    # def save(self, *args, **kwargs):
    #     # qrcode_img = qrcode.make(self.familiya)
    #     # canvas = Image.new('RGB', (10, 10), 'white')
    #     # draw = ImageDraw.Draw(canvas)
    #     filename = f'qr_code-{self.cer_nomer}.png'
    #     # buffer = BytesIO()
    #     # canvas.save(buffer, 'PNG')
    #     # self.qr_code.save(filename, File(buffer), save=False)
    #     # canvas.close()
    #     # super().save(*args, **kwargs)
    #
    #     qr = qrcode.QRCode(
    #         version=1,
    #         error_correction=qrcode.constants.ERROR_CORRECT_L,
    #         box_size=10,
    #         border=4,
    #     )
    #     qr.add_data('Some data')
    #     qr.make(fit=True)
    #
    #     self.qr_code = qr.make_image(fill_color="black", back_color="white")
    #     self.qr_code.save(filename, 'PNG')
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
