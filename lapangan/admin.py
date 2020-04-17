from django.contrib import admin

from .models import Lapangan, Rumput, Waktu, Harga, Booking


class LapanganAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jenis_rumput')


class HargaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga')

class WaktuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'waktu', 'harga')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('kode_booking', 'tanggal')

admin.site.register(Lapangan, LapanganAdmin)
admin.site.register(Rumput)
admin.site.register(Waktu, WaktuAdmin)
admin.site.register(Harga, HargaAdmin)
admin.site.register(Booking, BookingAdmin)
