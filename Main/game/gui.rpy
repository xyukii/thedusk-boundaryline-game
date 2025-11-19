################################################################################
## Inisialisasi
################################################################################

## pernyataan offset init menyebabkan pernyataan inisialisasi di file ini untuk
## berjalan lebih dahulu daripada pernyataan init di file lain nya.
init offset = -2

## Memanggil gui.init. mereset gaya ke value bawaan, dan menset lebar dan
## tinggi dari permainan.
init python:
    gui.init(1920, 1080)

## Mengaktifkan pemeriksaan untuk properti yang tidak valid atau tidak stabil
## di layar atau transformasi
define config.check_conflicting_properties = True


################################################################################
## Variabel konfigurasi GUI
################################################################################


## Warna #######################################################################
##
## Warna text pada antarmuka.

## Warna aksen yang digunakan sepanjang interface sampai pewarnaan text.
define gui.accent_color = '#ffffff'

## Warna yang di gunakan untuk warna tombol text jika di pilih atau di tekan.
define gui.idle_color = '#888888'

## Warna kecil yang di gunakan untuk text kecil, yang membutuhkan lebih terang/
## lebih gelap untuk mencapai efek yang sama
define gui.idle_small_color = '#aaaaaa'

## Warna yang di gunakan untuk tombol dan bar yang di pilih.
define gui.hover_color = '#dadada'

## Warna yang digunakan untuk text tombol ketika di pijit tapi tidak di fokus.
## Tombol di pilih jika terdapat di layar saat ini atau value preferensi.
define gui.selected_color = '#ffffff'

## Warna yang di gunakan untuk tombol text ketika tidak bisa di pilih.
define gui.insensitive_color = '#8888887f'

## Warna yang di gunakan untuk beberapa bagian dari bar yang tidak terisi. Ini
## tidak di gunakan secara langsung, Tapi di gunakan ketika me regenerasi file
## gambar bar.
define gui.muted_color = '#9e9e9e'
define gui.hover_muted_color = '#c7c7c7'

## Warna yang di gunakan untuk dialog dan text pilihan menu.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Font dan ukuran Font ########################################################

## Font yang digunakan untuk text in-game.
define gui.text_font = "DejaVuSans.ttf"

## Font yang di gunakan untuk nama karakter.
define gui.name_text_font = "DejaVuSans.ttf"

## Font yang digunakan untuk text di luar permainan.
define gui.interface_text_font = "DejaVuSans.ttf"

## Ukuran normal dialog text.
define gui.text_size = 33

## Ukuran dari nama karakter.
define gui.name_text_size = 45

## Ukuran text antarmuka permainan.
define gui.interface_text_size = 33

## Ukuran label di antarmuka permainan.
define gui.label_text_size = 36

## Ukuran dari text di layar notifikasi.
define gui.notify_text_size = 24

## Ukuran judul permainan.
define gui.title_text_size = 75


## Menu utama dan Menu permainan. ##############################################

## Gambar yang di gunakan untuk Menu utama dan Menu permainan.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialog ######################################################################
##
## Variabel ini mengendalikan bagaimana dialog di tampilkan pada layar pada
## satu waktu.

## Tinggi textbox yang berisi dialog.
define gui.textbox_height = 278

## Penempatan texbox secara vertikal pada layar. 0.0 adalah atas, 0.5 adalah
## tengah, dan 1.0 adalah bawah.
define gui.textbox_yalign = 1.0


## Penempatan nama karakter yang berbicara, hampir sama dengan kotak text. 
define gui.name_xpos = 360
define gui.name_ypos = 0

## Penempatan  horizontal nama karakter. Ini dapat berupa 0.0 untuk rata kiri,
## 0.5 untuk rata tengah, dan 1.0 untuk rata kanan. 
define gui.name_xalign = 0.0

## Lebar, panjang, dan tepi dari kotak berisi nama karakter, Atau None untuk
## secara otomatis mengukur nya.
define gui.namebox_width = None
define gui.namebox_height = None

## Tepi kotak bersisi urutan nama karakter, di kiri, atas, kanan, bawah.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Jika Benar, latar dari kotaknama akan di beri judul, jika Salah, latar dari
## kotaknama akan di ukur ulang.
define gui.namebox_tile = False


## Penempatan dialog itu relatif pada kotaktext. Ini dapat berisi angka dari
## pixel yang relativ mulai dari sisi kiri sampai atas dari kotaknama, atau 0.5
## untuk tengah.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Lebar maximum dari dialog text, dalam pixel.
define gui.dialogue_width = 1116

## rata tengah dari text dialog. Ini dapat berisi 0.0 untuk rata kiri, atau 0.5
## untuk tengah, dan 1.0 untuk kanan.
define gui.dialogue_text_xalign = 0.0


## Tombol ######################################################################
##
## Variabel-variabel ini, bersama dengan file gambar di gui/button, mengontrol
## aspek-aspek bagaimana tombol ditampilkan.

## Lebar dan tinggi tombol, dalam piksel. Jika tidak ada, Ren'Py akan
## menghitung ukuran.
define gui.button_width = None
define gui.button_height = None

## Batas di setiap sisi tombol, dalam urutan kiri, atas, kanan, bawah.
define gui.button_borders = Borders(6, 6, 6, 6)

## Jika Benar, gambar latar belakang akan dibuat ubin. Jika Salah, gambar latar
## belakang akan diskalakan secara linier.
define gui.button_tile = False

## Font yang digunakan oleh tombol.
define gui.button_text_font = gui.interface_text_font

## Ukuran teks yang digunakan oleh tombol.
define gui.button_text_size = gui.interface_text_size

## Warna tombol text di berbagai kondisi.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Alignment horisontal tombol text. (0.0 itu kiri, 0.5 tengah, 1.0 kanan).
define gui.button_text_xalign = 0.0


## Variabel-variabel ini mengganti pengaturan untuk berbagai jenis tombol.
## Silakan lihat dokumentasi gui untuk mengetahui jenis tombol yang tersedia,
## dan untuk apa tombol tersebut digunakan.
##
## Kustomisasi ini digunakan oleh antarmuka default:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Anda juga dapat menambahkan kustomisasi Anda sendiri, dengan menambahkan
## variabel yang diberi nama yang tepat. Sebagai contoh, Anda dapat menghapus
## baris berikut ini untuk mengatur lebar tombol navigasi.

# define gui.navigation_button_width = 250


## Tombol Pilihan ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Tombol Slot File ############################################################
##
## Tombol slot file adalah jenis tombol khusus. Tombol ini berisi gambar mini,
## dan teks yang menjelaskan isi slot penyimpanan. Slot penyimpanan menggunakan
## file gambar dalam gui/tombol, seperti jenis tombol lainnya.

## Tombol simpan slot.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Lebar dan tinggi gambar mini yang digunakan oleh slot penyimpanan.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Jumlah kolom dan baris dalam kisi-kisi slot penyimpanan.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Pemosisian dan Spasi ########################################################
##
## Variabel-variabel ini mengontrol pemosisian dan jarak berbagai elemen
## antarmuka pengguna.

## Posisi sisi kiri tombol navigasi, relatif terhadap sisi kiri layar.
define gui.navigation_xpos = 60

## Posisi vertikal indikator lompatan.
define gui.skip_ypos = 15

## Posisi vertikal layar notifikasi.
define gui.notify_ypos = 68

## Jarak spasi di antara pilihan menu.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Mengontrol jumlah spasi di antara preferensi.
define gui.pref_spacing = 15

## Mengontrol jumlah spasi di antara tombol preferensi.
define gui.pref_button_spacing = 0

## Jarak antara tombol halaman file.
define gui.page_spacing = 0

## Jarak antara slot file.
define gui.slot_spacing = 15

## posisi text menu utama.
define gui.main_menu_text_xalign = 1.0


## Frame #######################################################################
##
## Variabel ini mengontrol tampilan frame yang dapat berisi komponen antarmuka
## pengguna ketika overlay atau jendela tidak ada.

## Frame generic
define gui.frame_borders = Borders(6, 6, 6, 6)

## Bingkai yang digunakan sebagai bagian dari layar konfirmasi.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Bingkai yang digunakan sebagai bagian dari layar lewati.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Bingkai yang digunakan sebagai bagian dari layar pemberitahuan.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Haruskah latar belakang bingkai dibuat berubin?
define gui.frame_tile = False


## Bilah, Bilah Gulir, dan Geser ###############################################
##
## Ini mengontrol tampilan dan ukuran bilah, bilah gulir, dan penggeser.
##
## GUI Bawaan hanya menggunakan slider dan scrollbars vertikal. Bar lainnya
## hanya di gunakan pada layar GUI yang di tulis sendiri oleh pembuat/creator.

## Ketinggian bilah horizontal, bilah gulir, dan penggeser. Lebar bilah
## vertikal, bilah gulir, dan penggeser.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Benar jika gambar batang harus diubin. Salah jika gambar harus diskalakan
## secara linier.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Batas horizontal.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Batas vertikal.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Sejarah #####################################################################
##
## Layar riwayat menampilkan dialog yang telah diberhentikan oleh pemain.

## Jumlah blok riwayat dialog yang akan disimpan Ren'Py.
define config.history_length = 250

## Ketinggian entri layar riwayat, atau Tidak Ada untuk membuat variabel
## ketinggian dengan mengorbankan kinerja.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Posisi, lebar, dan perataan label yang memberikan nama karakter yang
## berbicara.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Posisi, lebar, dan perataan teks dialog.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## Layar mode NVL menampilkan dialog yang diucapkan oleh karakter mode NVL.

## Batas latar belakang jendela latar belakang mode NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Jumlah maksimum entri mode NVL yang akan ditampilkan Ren'Py. Ketika lebih
## banyak entri daripada ini akan ditampilkan, entri tertua akan dihapus.
define gui.nvl_list_length = 6

## Ketinggian entri mode NVL. Atur ini ke None (Tidak Ada) agar entri
## menyesuaikan tinggi secara dinamis.
define gui.nvl_height = 173

## Spasi antara entri mode NVL ketika gui.nvl_height adalah None, dan antara
## entri mode NVL dan menu mode NVL.
define gui.nvl_spacing = 15

## Posisi, lebar, dan perataan label yang memberikan nama karakter yang
## berbicara.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Posisi, lebar, dan perataan teks dialog.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Posisi, lebar, dan perataan teks nvl_thought (teks yang diucapkan oleh
## karakter nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Posisi tombol menu nvl.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Lokalisasi ##################################################################

## Ini mengendalikan dimana line break di ijinkan. Pengaturan bawaan sudah
## cocok untuk kebanyakan bahasa. Daftar value yang tersedia dapat di lihat di
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Perangkat mobile
################################################################################

init python:

    ## Ini meningkatkan ukuran tombol cepat agar lebih mudah disentuh pada
    ## tablet dan ponsel.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Ini mengubah ukuran dan spasi berbagai elemen GUI untuk memastikan
    ## elemen-elemen tersebut mudah terlihat pada ponsel.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Sesuaikan lokasi kotak teks.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Ubah ukuran dan jarak dari berbagai hal.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Tata letak tombol file.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Mode NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
