from django.conf.urls import patterns, url
from penilaian import views

urlpatterns = patterns('penilaian',
    #url(r'^$', views.nilai, name='nilai'),
    url(r'^periode/$', views.periode, name='periode'),
    url(r'^periode/tambah/$', views.tambah_periode, name='tambah_periode'),
    url(r'^periode/ubah/(?P<idPeriode>\d+)/$', views.ubah_periode, name='ubah_periode'),
    url(r'^periode/hapus/(?P<idPeriode>\d+)/$', views.hapus_periode, name='hapus_periode'),
    url(r'^periode/aktif/(?P<idPeriode>\d+)/$', views.aktif_periode, name='aktif_periode'),
    url(r'^periode/verifikasi/(?P<idPeriode>\d+)/$', views.verifikasi, name='verifikasi_periode'),
    url(r'^rekap/$', views.rekap_pilih_mapel, name='rekap_pilih_mapel'),
    url(r'^rekap/siswa/$', views.rekap_pilih_siswa, name='rekap_siswa'),
    url(r'^rekap/sikap/(?P<idNSikap>\d+)/$', views.popup_sikap, name='entrynilai_sikap'),
    url(r'^rekap/keterampilan/(?P<idNKeterampilan>\d+)/$', views.popup_keterampilan, name='entrynilai_keterampilan'),
    url(r'^rekap/kognitif/(?P<idNKognitif>\d+)/$', views.popup_kognitif, name='entrynilai_kognitif'),
    url(r'^un/$', views.rekapun_pilih_kelas, name='rekapun_pilih_kelas'),
    url(r'^un/siswa/$', views.rekapun_pilih_siswa, name='rekapun_pilih_siswa'),
    url(r'^un/siswa/(?P<idSiswa>\d+)/$', views.rekapun_siswa, name='rekapun_siswa'),
    url(r'^un/entry/(?P<idNun>\d+)/$', views.popup_un, name='entrynilai_un'),
    url(r'^us/$', views.rekapus_pilih_kelas, name='rekapus_pilih_kelas'),
    url(r'^us/siswa/$', views.rekapus_pilih_siswa, name='rekapus_pilih_siswa'),
    url(r'^us/siswa/(?P<idSiswa>\d+)/$', views.rekapus_siswa, name='rekapus_siswa'),
    url(r'^us/entry/(?P<idNus>\d+)/$', views.popup_us, name='entrynilai_us'),
    url(r'^nilai/$', views.nilai_kelas, name='nilai_kelas'),
    url(r'^nilai/siswa/$', views.nilai_siswa, name='nilai_siswa'),
    url(r'^nilai/siswa/(?P<idMapel>\d+)/$', views.detil_mapel, name='detil_mapel'),
    url(r'^kompetensi/$', views.rekapkomp_pilih_kelas, name='rekapkomp_pilih_kelas'),
    url(r'^kompetensi/siswa/$', views.rekapkomp_pilih_siswa, name='rekapkomp_pilih_siswa'),
    url(r'^kompetensi/siswa/(?P<idSiswa>\d+)/$', views.rekapkomp_siswa, name='rekapkomp_siswa'),
    url(r'^kompetensi/entry/(?P<idNKompetensi>\d+)/$', views.popup_kompetensi, name='entrynilai_kompetensi'),
    url(r'^nilaiku/$', views.nilaiku, name='nilaiku'),
)