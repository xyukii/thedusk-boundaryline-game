## File ini berisi opsi yang dapat di ubah untuk mengkustomisasi game mu.
##
## Baris yang di awali dengan dua 'tanda '#' adalah komentar, dan kamu
## tidak seharusnya menghapus nya. Baris dengan satu '#' adalah kode yang di
## komentari, kamu dapat menghapus tanda '#' jika di butuhkan.    


## Dasar #######################################################################

## Nama game yang dapat dibaca oleh manusia. Ini digunakan untuk menset judul
## jendela, dan juga di tampilkan di antarmuka dan laporan kesalahan. 
##
## Tanda _() yang mengelilingi string menandai itu dapat di terjemahkan.

define config.name = _("The Dusk Boundary Line")


## Meng determinasikan apakah judul yang di berikan di atas di tampilkan di
## menu utama. Set ini ke False untuk menyembunyikan judul.

define gui.show_name = True


## Versi Permainan.

define config.version = "1.0"


## Teks yang ditempatkan pada layar tentang game. Tempatkan teks di antara
## tanda kutip tiga, dan biarkan baris kosong di antara paragraf.

define gui.about = _p("""
{b}THE DUSK BOUNDARY LINE{/b}
Sebuah Visual Novel tentang dilema moral dan kerasnya kehidupan.

{b}CREDITS:{/b}
Story & Direction: Mojeng
Art & Design: Mojeng Studio
Music: Kevin MacLeod & YouTube Audio Library

Terima kasih telah memainkan game ini. 
Dukungan kalian sangat berarti bagi pengembang indie seperti saya.
""")
## Nama pendek permainan yang di gunakan untuk executable dan direktori di
## bangunan distribusi. Ini harus hanya berisi karakter ASCII-saja, dan tidak
## boleh mengandung  spasi, koma, atau kutip.

define build.name = "TheDuskBoundaryLine"


## Suara dan musik #############################################################

## Ketiga variabel ini mengontrol, antara lain, mixer mana yang ditampilkan
## kepada pemain secara default. Menetapkan salah satu dari variabel ini ke
## False akan menyembunyikan mixer yang sesuai.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Untuk mengijinkan pengguna memainkan test suara di chanel suara atau musik,
## silahkan hapus tag komentar nya '#' dan set sampel suara untuk di mainkan.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Silahkan hapus komentar dari baris berikut ini untuk men set file audio
## yang akan di mainkan ketika pemain berada di menu utama. File ini akan terus
## dimainkan sampai permainan di mulai, sampai di hentikan atau file lain di
## mainkan.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transisi ####################################################################
##
## Variabel ini menset transisi yang digunakan ketika event tertentu terjadi.
## Setiap variabel harus di set ke transisi, atau 'None' Untuk mengindikasikan
## bahwa tidak ada transisi yang harus di gunakan.

## Memasuki atau keluar dari menu permainan.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Antara layar dari menu permainan

define config.intra_transition = dissolve


## Transisi yang di gunakan setelah game di load.

define config.after_load_transition = None


## Digunakan ketika memasuki menu utama setelah game berakhir.

define config.end_game_transition = None


## Variabel untuk menset transisi yang digunakan ketika mulai game tidak
## tersedia. Melainkan, menggunakan pernyataan with setelah menunjukan layar
## tertentu.


## Managemen Jendela ###########################################################
##
## Ini mengendalikan kapan dialog di tampilkan. Jika "show", berarti selalu
## di tampilkan. Juka "hide", berarti itu hanya di tampilkan ketika dialog
## tersedia. jika "auto", jendela di sembunyikan sebelum pernyataan scene dan di
## tunjukkan kembali jika dialog ditampilkan.
##
## Setelah permainan di mulai, ini dapat di ganti dengan pernyataan "window
## show", "window hide", dan "window auto".

define config.window = "auto"


## Transisi yang digunakan untuk menunjukan dan menampilkan jendela dialog

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferensi defaults #########################################################

## Mengendalikan kecepatan text default. Default nya, 0, ini berarti infiniti,
## Sementara angka yang lain adalah berapa karakter per detik yang akan di
## tampilkan.

default preferences.text_cps = 0


## Delay default otomatis-maju. Nomor yang lebih besar berujung kepada waktu
## menunggu lebih lama, 0 sampai 30 adalah jarak yang valid.

default preferences.afm_time = 15


## Direktori penyimpanan #######################################################
##
## Mengendalikan tempat penyimpanan file save untuk game ini secara spesifik
## untuk setiap platform. File akan di taruh di:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Ini shearus nya tidak usah di ganti, dan juga iya, harus selalu berisi
## string, bukan expresi.

define config.save_directory = "TheDuskBoundaryLine-1760550754"


## Ikon ########################################################################
##
## Ikon yang di tampilkan di taskbar atau dock.

define config.window_icon = "gui/window_icon.png"


## Pengaturan Build ############################################################
##
## Bagian ini mengendalikan bagaimana Ren'Py mengubah proyek mu ke file
## distribusi.

init python:

    ## Fungsi berikut mengambil pola file. Pola file merupakan case-
    ## insensitiv, dan sama dengan arah direktori dasar, dengan atau tanpa
    ## awalan /. Jika banyak pola sama, yang pertama yang akan di gunakan.
    ##
    ## Di dalam pola:
    ##
    ## / Ini adlaah
    ##
    ## * mencocokan semua karakter, kecuali pemisah direktori.
    ##
    ## ** mencocokan semua karakter, termasuk pemisah direktori.
    ##
    ## Contohnya, "*.txt" mencocokan file txt di direktori dasar, "game/**.ogg"
    ## matches ogg files in the game directory or any of its subdirectories, and
    ## "**.psd" matches psd files anywhere in the project.

    ## Mengklasifikasi file sebagai None  untuk memisahkannya dari distribusi
    ## build.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Untuk mengarsipkan file, mengklasifikasikannya sebagai 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Alur Dokumentasi pencocokan file di duplikasikan di build app mac, jadi
    ## mereka tampil di kedua aplikasi dan juga file zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Kunci lisensi Google Play diperlukan untuk melakukan pembelian dalam
## aplikasi. Kunci ini dapat ditemukan di konsol pengembang Google Play, di
## bawah "Monetisasi" > "Pengaturan Monetisasi" > "Lisensi".

# define build.google_play_key = "..."


## Nama pengguna dan nama proyek yang di asosiasikan dengan proyek itch.io, di
## pisahkan dengan garis miring.

# define build.itch_project = "renpytom/test-project"
