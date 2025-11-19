# -*- coding: utf-8 -*-
define a = Character("Arya", color="#87CEEB")
define b = Character("Bima", color="#FF6347")
define l = Character("Lina", color="#FFD700")
define n = Character(None, what_color="#000000")

label splashscreen:
    call splash_screen
    return

# splash screen
label splash_screen:
    scene black
    pause 1

    show text "{size=40}{color=#FFFFFF}Mojeng Presents{/color}{/size}" at truecenter
    with dissolve
    pause 2

    hide text with dissolve
    pause 1

    return

image arya happy = "images/char/arya_happy.png"
image arya neutral = "images/char/arya_neutral.png"
image arya stress = "images/char/arya_stress.png"
image bima angry = "images/char/bima_angry.png"
image bima neutral = "images/char/bima_neutral.png"
image girl = "images/char/girl.png"
image lina happy = "images/char/lina_happy.png"
image lina sad = "images/char/lina_sad.png"
image mom happy = "images/char/mom_happy.png"
image mom neutral = "images/char/mom_neutral.png"

# Backgrounds - scale to screen size so they fill the whole screen
# Using config.screen_width / config.screen_height ensures they fit default window size.
image bg office_night = im.Scale("images/office_night.png", config.screen_width, config.screen_height)
image bg office_morning = im.Scale("images/office_morning.png", config.screen_width, config.screen_height)
image bg office_day = im.Scale("images/office_day.png", config.screen_width, config.screen_height)
image bg office_meeting = im.Scale("images/office_meeting.png", config.screen_width, config.screen_height)
image bg office_newday = im.Scale("images/office_newday.png", config.screen_width, config.screen_height)
image bg rain_street = im.Scale("images/rain_street.png", config.screen_width, config.screen_height)
image bg hospital = im.Scale("images/hospital.png", config.screen_width, config.screen_height)
image bg bus_night = im.Scale("images/bus_night.png", config.screen_width, config.screen_height)
image bg sunset_city = im.Scale("images/sunset_city.png", config.screen_width, config.screen_height)
image bg office_window = im.Scale("images/office_window.png", config.screen_width, config.screen_height)

label start:
    scene bg office_night with fade
    show arya stress at center
    play sound "audio/music/angin.mp3" loop
    n "Kantor sudah sepi. Jam hampir menunjukkan tengah malam."
    play sound "audio/sfx/kibot.mp3" loop
    n "Di antara deretan meja yang gelap, hanya satu layar monitor yang masih menyala — milik Arya, analis data berumur 28 tahun."

    a "Angka-angka ini kayak mimpi buruk yang nggak kelar-kelar."
    stop sound
    play sound "audio/sfx/notif.mp3"
    n "(Notifikasi ponsel berbunyi.)"
    stop sound
    show lina sad at left
    l "(Mas, besok batas bayar kos. Aku udah kehabisan cara, Mas…)"
    a "(Maaf, Lin… sebentar lagi selesai)."

    show bima angry at right
    b "Arya, tolong revisi data malam ini. Klien minta jam 6 pagi. Jangan tidur dulu."
    a "Seolah aku mesin yang nggak boleh berhenti."

    menu:
        "Tetap kerja lembur sampai pagi":
            jump ep1_lembur
        "Matikan laptop dan istirahat":
            jump ep1_tidur

label ep1_lembur:
    show arya neutral at center
    a "Udah biasa kok. Nanti bisa istirahat setelah ini…"
    play sound "audio/sfx/kibot.mp3" loop
    n "Layar monitor perlahan redup, tapi matanya masih terbuka."
    n "Pagi datang tanpa sempat bermimpi."
    hide arya
    jump episode2

label ep1_tidur:
    show arya neutral at center
    a "Udah cukup. Aku butuh tidur… bukan lagi angka."
    n "Ia menatap langit malam. Tidak ada bintang — hanya dirinya sendiri."
    hide arya
    jump episode2


label episode2:
    scene bg office_morning with fade
    show arya stress at center
    n "Kopi ketiga belum juga mengusir kantuk."
    n "Arya menghadiri rapat pagi dengan mata merah."

    show bima neutral at right
    b "Lumayan kerja kamu semalam. Tapi formatnya salah. Ulang lagi."
    a "Baik, Pak."
    stop sound
    play sound "audio/sfx/notif.mp3"
    n "(Telepon berdering. Nama 'Lina' muncul.)"
    show lina sad at left
    l "(Mas, aku diancam mau diusir hari ini!)"

    b "Arya! Matikan HP! Fokus dulu, ini rapat penting!"

    menu:
        "Angkat telepon dan bantu Lina":
            hide bima
            hide lina
            jump ep2_telpon
        "Abaikan telepon dan terus kerja":
            hide bima
            hide lina
            jump ep2_kerja

label ep2_telpon:
    show arya neutral at center
    a "Pak, maaf. Saya harus angkat telepon sebentar."
    show bima angry at right
    b "Kalau keluar ruangan, jangan balik lagi!"
    n "Kadang, memilih orang yang kamu sayang artinya kehilangan dunia lain."
    hide bima
    hide arya
    jump episode3

label ep2_kerja:
    show arya neutral at center
    a "Maaf, Lin…"
    show lina sad at left
    l "Iya, Mas. Nggak apa."
    n "Tapi nada suaranya tidak lagi sama."
    hide lina
    hide arya
    jump episode3


label episode3:
    scene bg office_day with fade
    show arya stress at center
    stop sound
    play sound "audio/sfx/kibot.mp3" loop
    n "Hari berganti tanpa sadar. Arya hanya mengenal tiga hal: layar, kopi, dan tekanan."

    show bima angry at right
    stop sound
    b "Data ini masih salah! Ulang dari awal!"
    a "Pak, saya udah kerja tiga malam tanpa tidur…"
    b "Itu urusan kamu, bukan saya!"

    n "(Telepon lagi — Lina.)"
    show lina sad at left
    l "(Mas, Ibu pingsan! Aku di rumah sakit. Tolong datang!)"

    menu:
        "Pergi ke rumah sakit":
            hide bima
            hide lina
            jump ep3_rumahsakit
        "Tetap di kantor":
            hide bima
            hide lina
            jump ep3_kantor
        "Rekam semua percakapan dengan Bima":
            hide bima
            hide lina
            jump ep3_rekam

label ep3_rumahsakit:
    scene bg hospital with fade
    show arya stress at center
    a "Maaf, Pak… tapi kali ini, aku nggak bisa tinggal diam."
    n "(Arya berlari keluar gedung, wajahnya basah oleh hujan.)"
    scene bg hospital with fade
    show lina sad at left
    l "Mas, aku takut banget…"
    a "Tenang, Lin. Kita hadapi bareng."
    hide lina
    hide arya
    jump episode4

label ep3_kantor:
    show arya stress at center
    a "Kerja ini… nggak sepadan dengan yang hilang."
    n "(Pesan masuk: 'Mas… Ibu di UGD.')"
    hide lina
    hide arya
    jump episode4

label ep3_rekam:
    show arya neutral at center
    n "Arya diam, menyalakan perekam suara di bawah meja."
    n "Setiap kata dari Bima jadi saksi."
    hide arya
    jump episode4


label episode4:
    scene bg office_meeting with fade
    n "Hari itu, semua meledak."
    show arya stress at center
    show bima angry at right
    b "Kamu pikir kamu siapa?! Kamu bikin klien marah besar!"
    n "Karyawan lain terdiam. Arya menatap kosong."

    menu:
        "Diam dan minta maaf (Pelarian)":
            hide bima
            hide arya
            jump route_pelarian
        "Balas membentak tanpa bukti (Keberanian)":
            hide bima
            hide arya
            jump route_berani
        "Ungkap bukti rekaman (jika ada)":
            if BuktiTerkumpul:
                hide bima
                hide arya
                jump route_bukti
            else:
                n "Arya ingin membalas, tapi tak punya bukti apapun."
                hide bima
                hide arya
                jump route_berani


label route_berani:
    show arya neutral at center
    a "Selama ini saya kerja siang malam! Tapi Bapak nggak pernah lihat!"
    show bima angry at right
    b "Karena kamu gagal!"
    a "Mungkin gagal jadi budak, iya."
    b "Kamu dipecat!"
    a "Terima kasih. Akhirnya saya bebas juga."
    hide bima
    hide arya
    jump episode5_berani

label route_bukti:
    n "(Arya menyalakan rekaman suara Bima.)"
    show arya neutral at center
    show bima neutral at right
    b "Revisi malam ini. Jangan tidur. Jam 6 standby."
    n "Karyawan lain berbisik: 'Dia nyuruh lembur segitu parahnya?'"
    a "Bapak pikir cuma saya yang lelah? Semua orang di sini sama."
    n "(HRD masuk. Suasana berubah tegang.)"
    hide bima
    hide arya
    jump episode5_bukti

label route_pelarian:
    show arya neutral at center
    n "Arya hanya diam. Ia tunduk, meminta maaf."
    n "Tapi di dalam hatinya, sesuatu perlahan retak."
    hide arya
    jump episode5_pelarian


label episode5_berani:
    scene bg sunset_city with fade
    n "Beberapa minggu berlalu."
    show arya happy at center
    show lina happy at left
    l "Mas kelihatan beda sekarang."
    a "Beda gimana?"
    l "Lebih hidup. Meski nggak punya apa-apa."
    a "Akhirnya aku tahu rasanya bernapas."
    n "💪 RUTE 2 – Keberanian (Tanpa Bukti)"
    return

label episode5_bukti:
    scene bg office_newday with fade
    show arya happy at center
    show lina happy at left
    n "Bima dipecat, dan kantor berubah sistemnya."
    a "Bukan soal menang… tapi soal berani bilang ‘cukup’."
    l "Mas, aku bangga."
    n "📱 RUTE 3 – Keadilan (Dengan Bukti)"
    return

label episode5_pelarian:
    scene bg bus_night with fade
    show arya neutral at center
    n "Bus malam melaju ke arah barat. Langit oranye perlahan pudar."
    a "Entah ke mana aku pergi. Tapi untuk pertama kalinya… aku bisa tidur."
    n "🚌 RUTE 4 – Pelarian"
    return

label episode5_patuh:
    scene bg office_window with fade
    show arya stress at center
    a "Aku naik jabatan, punya uang… tapi nggak punya siapa-siapa."
    a "Mungkin aku cuma hidup di layar yang sama tiap hari."
    n "🏢 RUTE 1 – Kemenangan Kosong"
    return
