# ==============================================================================
# 1. INIT: KONFIGURASI UMUM & STYLE MENU
# ==============================================================================

# Inisialisasi Python untuk mendaftarkan channel audio "sfx"
init python:
    # Mendaftarkan channel khusus untuk Sound Effects
    renpy.music.register_channel("sfx", mixer="sfx", loop=False)

# --- Definisi Screen Menu Pilihan (Baru) ---
screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button"

# --- Style Menu Pilihan (Baru) ---
style choice_vbox:
    xalign 0.5
    yalign 0.5

style choice_button is button:
    # Ukuran & Layout
    xsize 800
    ysize 80
    xalign 0.5
    yalign 0.5
    padding (50, 15)
    
    # WARNA TOMBOL (Solid Color - Anti Error Gambar Hilang)
    # Idle: Abu gelap transparan
    background Solid("#263238cc") 
    # Hover: Abu terang solid (lebih jelas saat disentuh)
    hover_background Solid("#546e7add") 

style choice_button_text is text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 30
    
    color "#eceff1"      # Putih tulang
    hover_color "#ffd740"    # Kuning emas saat disentuh
    outlines [(2, "#00000044", 1, 1)] # Shadow teks halus

# ==============================================================================
# 2. DEFINISI KARAKTER, VARIABEL & ASET
# ==============================================================================

# --- Karakter (Baru) ---
define b = Character("Bima", color="#81d4fa", who_bold=True) # Biru Muda (Protagonis)
define h = Character("Pak Hartono", color="#ef5350", who_bold=True) # Merah (Antagonis)
define r = Character("Rina", color="#fff176") # Kuning Soft (Adik)
define n = Character(None, what_color="#000000", what_italic=True) # Narator

# --- Variabel Sistem Poin (Baru) ---
default mental_bima = 0    
default family_bond = 0    

# --- ASET GAMBAR KARAKTER (Diperbarui dengan path baru) ---
# Catatan: Ren'Py akan menggunakan file di folder images/char/ dengan nama yang sesuai.
image bima lelah = "images/char/arya_neutral.png"
image bima tegas = "images/char/arya_happy.png"
image bima marah = "images/char/arya_stress.png"

image hartono marah = "images/char/bima_angry.png"
image hartono dingin = "images/char/bima_neutral.png"

image rina cemas = "images/char/lina_sad.png"
image rina senyum = "images/char/lina_happy.png"
image rina nangis = "images/char/lina_sad.png"

# --- ASET GAMBAR LATAR BELAKANG (Diperbarui dengan path baru) ---
# im.Scale dihapus agar Ren'Py menggunakan penyesuaian skala default.
image bg kamar = im.Scale("images/office_newday.png", config.screen_width, config.screen_height)
image bg kantor = im.Scale("images/office_day.png", config.screen_width, config.screen_height)
image bg kantor_malam = im.Scale("images/office_night.png", config.screen_width, config.screen_height)
image bg rumah_sakit = im.Scale("images/hospital.png", config.screen_width, config.screen_height)
image bg hujan_jalan = im.Scale("images/rain_street.png", config.screen_width, config.screen_height)

# --- Efek Visual ---
define flash = Fade(0.1, 0.0, 0.5, color="#fff") 
define slow_dissolve = Dissolve(2.0)
define heart_beat = Fade(0.05, 0.05, 0.05, color="#000")

# --- Splash Screen Tetap Ada ---
label splashscreen:
    call splash_screen
    return

label splash_screen:
    scene black
    pause 1

    show text "{size=40}{color=#FFFFFF}Mojeng Presents{/color}{/size}" at truecenter
    with dissolve
    pause 2

    hide text with dissolve
    pause 1

    return

# ==============================================================================
# 3. CERITA UTAMA (FULL STORY - MASTERPIECE VERSION)
# ==============================================================================

label start:
    # Pastikan variabel direset untuk game baru
    $ mental_bima = 0
    $ family_bond = 0
    play music "audio/music/dark_space_ambient.mp3" loop volume 0.3 # Menggunakan musik default lama

    # --- SCENE 1: PAGI YANG BERAT ---
    scene black
    # play sfx "audio/sfx/notif.mp3" # Jika ada sfx alarm
    
    n "Jakarta, 05:30 WIB."
    n "Alarm itu berbunyi lagi. Suaranya seperti palu godam yang menghantam kepala setiap subuh."

    scene bg kamar with slow_dissolve
    show bima lelah at center with dissolve
    
    b "(Menghela napas berat) Hah... Badan rasanya remuk. Padahal baru merem 3 jam."
    b "Apa gue izin sakit aja ya hari ini? Bilang tifus kek..."
    
    # [CHOICE 1: MENENTUKAN MENTAL AWAL]
    menu:
        "Suara hati kecil Bima berkata..."

        "Paksa bangun. Tagihan tidak bisa nunggu.":
            $ mental_bima += 1
            $ renpy.notify("Mental Bima: Fokus (+1)")
            
            b "(Menepuk pipi sendiri) Nggak. Nggak bisa. Tagihan RS Ibu bulan ini belum lunas. PayLater Rina juga."
            b "Ayo Bim. Gerak. Jangan manja."

        "Maki-maki nasib. Rasanya ingin menyerah.":
            $ mental_bima -= 1
            $ renpy.notify("Mental Bima: Tertekan (-1)")
            
            b "Bangsat... Kenapa sih hidup gue gini amat? Orang lain tidur enak, gue kayak sapi perah."
            n "Bima bangun dengan aura gelap. Energi negatif sudah menumpuk sejak mata terbuka."

    # --- MASUK RINA ---
    show bima lelah:
        xalign 0.8
    show rina cemas at left with moveinleft
    
    r "Mas Bima? Mas kok pucet banget? Mas belum sarapan kan?"
    b "Nggak sempet, Dek. Si Hartono minta revisi jam 8 teng. Telat dikit, kepala Mas taruhannya."
    r "Mas... Ibu semalam nanyain Mas terus pas sadar. Katanya Mas janji mau nemenin kontrol hari ini."
    
    # [CHOICE 2: MENENTUKAN HUBUNGAN KELUARGA]
    menu:
        "Rina menagih janji. Bima sedang stress berat. Responnya?"

        "Tatap matanya, minta maaf tulus (Prioritas Keluarga).":
            $ family_bond += 1
            $ renpy.notify("Hubungan Keluarga: Erat (+1)")
            
            b "(Melembutkan suara) Maafin Mas ya, Dek. Mas janji, kelar proyek ini, Mas ganti waktu yang ilang."
            
            show rina senyum at left
            r "Janji ya, Mas? Yaudah hati-hati. Ini bekal rotinya dibawa."
            n "Rina sedikit lega. Ada setitik harapan di matanya."

        "Ngegas/Marah karena merasa ditekan (Prioritas Ego).":
            $ family_bond -= 1
            $ renpy.notify("Hubungan Keluarga: Renggang (-1)")
            
            b "Dek, ngertiin dikit napa?! Mas kerja banting tulang buat siapa?! Jangan nambah beban pikiran deh pagi-pagi!"
            
            show rina nangis at left
            r "..."
            n "Rina mundur selangkah, kaget dibentak. Bima langsung menyesal, tapi gengsinya terlalu tinggi untuk minta maaf."

    hide rina
    hide bima
    with dissolve
    
    n "Bima berangkat menembus macetnya Jakarta. Langit mendung pekat, seolah tahu badai akan datang menimpa hidupnya hari ini."

    # --- SCENE 2: KANTOR NERAKA ---
    scene bg kantor with fade
    # play sfx "audio/sfx/kibot.mp3" loop # Jika ada sfx keyboard
    
    n "Jam 10:00. Ruangan Divisi Kreatif hening mencekam. Aura pembunuh terasa di udara."

    show bima lelah at left
    show hartono marah at right with vpunch # Layar getar
    
    # stop sfx
    
    h "BIMA! SINI KAMU!"
    b "I-iya, Pak?"
    h "Ini desain apaan?! Hah?! Saya minta konsep 'Elegan', kenapa kamu kasih sampah warna-warni kayak brosur sedot WC gini?!"
    h "Kamu lulusan desain beneran bukan sih?! Anak magang aja kerjanya lebih becus dari kamu!"
    
    b "Tapi Pak, kemarin Bapak sendiri yang bilang referensinya..."
    h "JANGAN JAWAB! Salah ya salah! Rombak total! Saya nggak mau tau, besok pagi harus ada di meja saya."
    h "Kalau nggak... SP 3 turun. Silakan kamu angkat kaki dari sini dan bawa kardusmu."
    
    hide hartono with moveoutright
    n "Pak Hartono membanting pintu ruangan. Bima terpaku di tengah kantor. Harga dirinya serasa diludahi di depan rekan kerjanya."

    # [CHOICE 3: DILEMA TENGAH]
    menu:
        "Darah mendidih. Rasanya ingin meledak. Apa yang Bima lakukan?"

        "Tahan emosi. Fokus cari solusi (Logis).":
            $ mental_bima += 1
            $ renpy.notify("Mental Bima: Stabil (+1)")
            
            show bima tegas at left
            b "(Tarik napas panjang) Oke. Tenang Bim. Lo jago. Lo bisa benerin ini. Anggap aja dia radio rusak."
            n "Bima mencoba memisahkan perasaan dari pekerjaan. Dia kembali duduk dengan sisa tenaga terakhir."

        "Muak. Mengutuk dalam hati (Emosional).":
            $ mental_bima -= 1
            $ renpy.notify("Mental Bima: Retak (-1)")
            
            show bima marah at left
            b "(Mengepalkan tangan sampai putih) Awas lo tua bangka... Suatu saat gue bales... Liat aja nanti."
            n "Dendam itu menggerogoti fokus Bima. Dia bekerja dengan hati yang penuh racun."

    # --- SCENE 3: KLIMAKS (THE CALL) ---
    scene bg kantor_malam with dissolve
    # play sfx "audio/music/angin.mp3" loop fadein 2.0
    
    n "Jam 23:45 WIB."
    n "Hujan badai mengguyur kaca kantor lantai 15. Kantor sudah kosong. Hanya sisa Bima dan cahaya monitor yang menyakitkan mata."
    
    # play sfx "audio/sfx/notif.mp3" loop # Jika ada sfx ringtone
    
    # Efek Visual Jantung
    scene bg kantor_malam with heart_beat
    pause 0.2
    scene bg kantor_malam with heart_beat
    
    "{b}{color=#ff5252}INCOMING CALL: RINA{/color}{/b}"
    
    # stop sfx
    b "(Mengangkat telepon dengan tangan gemetar) Halo... Dek?"
    
    r "{i}(Suara tangis pecah, nyaris berteriak){/i} MAS BIMA! MAS DIMANA?!"
    r "Ibu Mas... Napas Ibu sempet berenti tadi! Dokter lagi pompa jantung Ibu sekarang!"
    r "Mas cepetan ke sini... Aku takut sendirian Mas... Aku nggak mau Ibu pergi..."
    
    n "Dunia Bima runtuh seketika. Suara hujan mendadak hilang. Yang terdengar hanya denging panjang di telinganya."
    b "Mas... Mas jalan sekarang."

    # HARTONO MUNCUL MENGHALANGI
    show hartono dingin at right with dissolve
    
    h "Eits. Mau kemana kamu?"
    h "Saya lihat email, file revisinya belum masuk. Jangan bilang kamu mau kabur."
    
    b "Pak... Ibu saya sekarat. Di UGD. Saya harus pergi detik ini juga."
    
    h "(Tertawa kecil) Halah. Alasan klasik. Kemarin sakit, sekarang sekarat."
    h "Dengar ya Bima. Klien besok datang jam 8 pagi. Kalau kamu melangkah keluar dari pintu itu sebelum file ini selesai..."
    h "Simpan saja ID Card kamu. Jangan harap kamu bisa kerja di industri ini lagi. Saya pastikan nama kamu saya blacklist dari semua agensi."
    
    b "..."
    h "Pikir pake otak, bukan pake perasaan. Kamu butuh duit buat bayar RS kan? Selesaikan kerjamu, baru jadi pahlawan kesiangan."

    # --- LOGIC GATE (PENENTUAN ENDING) ---
    n "Waktu seakan berhenti. Di kiri ada pintu keluar (Keluarga). Di depan ada layar monitor (Karir/Uang)."
    n "Apa yang tersisa di hati Bima setelah seharian ini?"

    # SYARAT ENDING MASTERPIECE
    if mental_bima >= 1 and family_bond >= 1:
        jump ending_smart_masterpiece
    elif family_bond >= 1:
        jump ending_rebel_masterpiece
    else:
        jump ending_slave_masterpiece

# ==============================================================================
# 4. ENDING SECTION (DETAILED & EMOTIONAL)
# ==============================================================================

# --- ENDING 1: BONEKA BERNYAWA (BAD ENDING) ---
label ending_slave_masterpiece:
    stop music
    play music "audio/music/sad_piano.mp3" loop 
    
    show bima lelah at left
    
    b "(Menunduk dalam, air mata menetes) ..."
    b "(Dalam hati) Pak Hartono bener. Kalau gue dipecat, gue bayar RS pake apa? Gue nggak punya pilihan."
    
    b "Maaf, Pak. Saya... saya selesaikan. Tolong jangan pecat saya."
    
    h "Nah, gitu dong. Itu baru profesional. Jangan cengeng. Saya tunggu di ruangan saya."
    hide hartono with moveoutright

    scene bg kantor_malam
    n "Bima duduk kembali ke kursinya. Kursi yang terasa seperti penjara."
    n "Dia mengetik revisi dengan air mata yang terus menetes ke keyboard. Setiap 'klik' mouse terasa seperti menikam hatinya sendiri."
    n "Jam 03:00 Pagi. Pekerjaan selesai. File terkirim."

    scene bg rumah_sakit with slow_dissolve
    n "Bima berlari menyusuri lorong rumah sakit yang bau obat-obatan. Sepi. Dingin."
    
    show rina senyum at center
    # show rina nangis at center (Lebih emosional jika dia terlihat sedih)
    
    b "Dek! Ibu gimana? Mas udah transfer gaji Mas semua buat obat. Cukup kan?"
    
    r "..."
    r "Uangnya udah masuk, Mas. Makasih. Administrasi lunas."
    
    b "Syukurlah... Mas boleh masuk? Mas mau minta maaf sama Ibu."
    
    r "(Menatap Bima dingin, matanya bengkak) Ibu udah tidur, Mas."
    r "Tadi... pas Ibu kritis, Ibu manggil nama Mas Bima terus. Sampai suaranya habis."
    r "Sekarang Ibu udah nggak sakit lagi. Mas pulang aja. Mas bau kantor."
    
    hide rina with dissolve
    n "Rina masuk ke ruang rawat dan mengunci pintu. Klik."
    n "Bima berdiri sendiri di lorong dingin itu. Dia memegang dompetnya yang tebal berisi gaji, tapi dadanya terasa kosong melompong."
    n "Dia sadar, dia telah menjual jiwanya, dan tidak ada kembaliannya."

    scene black with fade
    pause 2.0
    "{b}{size=40}{color=#ff0000}BAD ENDING: BONEKA BERNYAWA{/color}{/size}{/b}\n\n(Kamu memilih keamanan finansial, tapi kehilangan kehangatan rumah selamanya.)"
    return

# --- ENDING 2: KEBEBASAN YANG NEKAT (NEUTRAL/EMOTIONAL ENDING) ---
label ending_rebel_masterpiece:
    stop music
    play music "audio/music/bright_acoustic.mp3" loop 
    
    show bima marah at left with vpunch
    b "CUKUP PAK!!!"
    
    h "Hah?! Kamu bentak saya?!"
    
    b "Bapak pikir saya ini mesin?! Ibu saya lagi bertaruh nyawa di sana!"
    b "Persetan sama Klien! Persetan sama Blacklist Bapak! Saya nggak peduli!"
    b "Saya resign. Detik ini juga. Makan tuh deadline!"
    
    play sfx "audio/sfx/table_slams.mp3" noloop volume 2 # Menggunakan SFX bentak meja untuk lempar kartu
    n "Bima melempar ID Card-nya tepat ke dada Pak Hartono. Plak! Dia berlari keluar tanpa menoleh."
    
    scene bg hujan_jalan with flash
    n "Bima memacu motornya menembus badai. Basah kuyup. Dingin. Dia tahu besok dia pengangguran."
    n "Tapi anehnya... dadanya terasa lapang. Seperti baru pertama kali bernapas lega dalam 5 tahun terakhir."

    scene bg rumah_sakit with slow_dissolve
    
    show rina nangis at left
    show bima tegas at right
    
    b "DEK! IBU!"
    
    r "Mas Bima! Mas dateng!"
    n "Rina langsung memeluk kakaknya erat. Tangisnya pecah, tapi kali ini tangis lega."
    
    r "Ibu udah lewat masa kritisnya Mas... Dokter bilang Ibu kuat."
    
    b "(Lemas, jatuh terduduk) Alhamdulillah..."
    b "Dek, maafin Mas ya. Mas udah keluar dari kerjaan. Mas sekarang pengangguran. Kita mungkin bakal susah makan besok."
    
    r "(Tersenyum sambil menghapus air mata) Nggak apa-apa Mas. Kita bisa makan nasi garem."
    r "Yang penting Mas Bima ada di sini. Itu udah cukup buat Rina sama Ibu."
    
    scene black with fade
    n "Malam itu, di ruang tunggu RS yang sempit, Bima tidur dengan nyenyat."
    n "Masa depan gelap, dompet tipis, tapi hatinya penuh."
    
    "{b}{size=40}{color=#FFD700}NEUTRAL ENDING: KEBEBASAN YANG NEKAT{/color}{/size}{/b}\n\n(Kamu kehilangan karir, tapi memenangkan kembali keluargamu.)"
    return

# --- ENDING 3: KESEIMBANGAN SEMPURNA (TRUE/GOOD ENDING) ---
label ending_smart_masterpiece:
    stop music
    play music "audio/music/achievement.mp3" loop
    
    show bima tegas at left
    b "(Menutup mata sejenak, menarik napas dalam, lalu menatap tajam Hartono)"
    b "Pak Hartono. Dengar saya baik-baik."
    
    h "Apa lagi? Mau nyerah?"
    
    b "Saya akan pergi ke RS sekarang. Itu tidak bisa ditawar."
    b "TAPI... Saya bawa laptop saya. Saya akan kerjakan revisi itu di ruang tunggu RS."
    
    h "Hah? Kamu pikir saya percaya?"
    
    b "Bapak tahu kualitas saya. Selama 3 tahun saya tidak pernah mengecewakan Bapak."
    b "Subuh nanti file sudah ada di email Bapak. Klien puas, Bapak aman, dan saya bisa menemani Ibu saya."
    b "Tapi kalau Bapak tetap menghalangi saya keluar dari pintu itu..."
    b "Saya pastikan saya akan teriak sekencang-kencangnya kalau Bapak menahan karyawan yang orang tuanya sekarat. Biar satu gedung dengar."
    
    h "..."
    h "(Terdiam, melihat sorot mata Bima yang tidak main-main)"
    h "Cih. Dasar keras kepala."
    h "Sana pergi. Tapi awas kalau jam 5 pagi belum masuk email saya!"
    
    b "Terima kasih, Pak."
    
    scene bg rumah_sakit with fade
    n "Suasana RS tenang. Bunyi monitor jantung terdengar teratur."
    
    show bima lelah at center
    n "Bima duduk di lantai, memangku laptopnya. Matanya merah kurang tidur, tapi jarinya menari lincah di atas keyboard."
    n "Di sebelahnya, Rina tertidur di bahu Bima. Dan di ranjang, Ibu bernapas dengan tenang."
    
    b "(Tersenyum tipis) Selesai. Send."
    
    n "Bima menutup laptopnya. Dia berhasil. Dia tidak mengorbankan siapapun hari ini."
    n "Dia membuktikan bahwa dia bukan lagi anak buah yang bisa diinjak, melainkan seorang Pria yang punya prinsip."
    
    scene black with slow_dissolve
    pause 2.0
    "{b}{size=40}{color=#00e676}TRUE ENDING: MASTER OF LIFE{/color}{/size}{/b}\n\n(Selamat! Logika dan Hatimu berjalan seirama. Kamu menang telak.)"
    return