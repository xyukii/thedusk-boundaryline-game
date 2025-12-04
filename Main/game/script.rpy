# ==============================================================================
# 1. SYSTEM & UI SETUP (CODING STYLE - AMAN & BERSIH)
# ==============================================================================

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25

        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button"

style choice_vbox:
    xalign 0.5
    yalign 0.5

style choice_button is button:
    # --- STYLE MODERN DARK (TANPA GAMBAR) ---
    xsize 900
    ysize 85
    xalign 0.5
    yalign 0.5
    padding (50, 10)
    
    # Background Idle: Hitam Abu Transparan
    background Solid("#212121e6") 
    # Background Hover: Abu Terang Solid (Visual Feedback)
    hover_background Solid("#455a64") 

style choice_button_text is text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 30
    color "#cfd8dc"          # Abu muda
    hover_color "#ffffff"    # Putih terang
    outlines [(2, "#00000088", 1, 1)] 

# ==============================================================================
# 2. KARAKTER & VARIABEL
# ==============================================================================

define b = Character("Bima", color="#29b6f6", who_bold=True) 
define h = Character("Pak Hartono", color="#d32f2f", who_bold=True)
define r = Character("Rina", color="#ffee58")
define n = Character(None, what_color="#000000", what_italic=True) # Narator

# --- VARIABEL SISTEM POIN ---
default mental_bima = 0   
default family_bond = 0   

# --- ASET GAMBAR ---
# Gunakan file yang sudah ada
image bima lelah = "images/char/Bima_stress.png"
image bima tegas = "images/char/Bima_netral.png"
image bima marah = "images/char/Bima_marah.png"
image hartono marah = "images/char/Hartono_marah.png"
image hartono dingin = "images/char/Hartono_sombong.png"
image rina cemas = "images/char/Adek_sedih.png"
image rina senyum = "images/char/Adek_netral.png"
image rina nangis = "images/char/Adek_nangis.png"

image bg kamar = "images/office_newday.png"
image bg kantor = "images/office_day.png"
image bg kantor_malam = "images/office_night.png" # Kita pakai ini untuk scene frustasi
image bg rumah_sakit = "images/hospital.png"
image bg hujan_jalan = "images/rain_street.png"

# --- EFEK VISUAL ---
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define heart_beat = Fade(0.05, 0.05, 0.05, color="#000")
define slow_dissolve = Dissolve(2.0) 

# ==============================================================================
# 3. CERITA UTAMA (FULL NARRATIVE - REVISI SCENE FRUSTASI)
# ==============================================================================

label start:
    # --- PROLOG: BEBAN DI PUNDAK ---
    scene black
    n "Jakarta, 05:30 WIB."
    n "Alarm HP berbunyi. Suara default 'Radar' yang menyebalkan itu terasa seperti bor yang menembus gendang telinga."
    
    scene bg kamar with fade
    show bima lelah at center with dissolve
    
    b "(Mata masih terpejam) Hhh... Matiin nggak ya? Lima menit lagi..."
    b "Badan gue rasanya kayak abis digebukin warga. Tulang punggung nyeri, kepala berat."
    b "(Melirik jam) Kalau gue bangun sekarang, gue masih sempet mandi. Kalau gue tidur lagi... gue bisa lupa sama semua masalah ini."

    # CHOICE 1: MENTALITAS PAGI (BLIND)
    menu:
        "Apa yang ada di pikiran Bima saat membuka mata?"

        "Ingat Tagihan RS Ibu. Harus Kuat.":
            # Efek baru muncul SETELAH klik
            $ mental_bima += 1
            $ renpy.notify("Mental Bima: Fokus (+1)")
            
            b "(Menampar pipi pelan) Sadar, Bima. Sadar."
            b "Tagihan chemo Ibu bulan depan 8 juta. PayLater Rina belum lunas."
            b "Lo nggak punya privilege buat sakit. Ayo bangun."
            n "Bima memaksakan tubuhnya tegak. Dia membasuh muka dengan air dingin untuk membekukan perasaannya."

        "Mengeluh soal Nasib.":
            $ mental_bima -= 1
            $ renpy.notify("Mental Bima: Tertekan (-1)")
            
            b "Sialan... Kenapa sih gue nggak lahir jadi anak orang kaya aja?"
            b "Kerja kayak kuda, gaji cuma numpang lewat. Kapan gue bisa napas lega?"
            n "Bima bangun dengan langkah berat. Aura di sekelilingnya terasa gelap dan menyesakkan."

    # --- SCENE: INTERAKSI KELUARGA ---
    show bima lelah:
        xalign 0.8
    show rina cemas at left with moveinleft
    
    r "Mas Bima? Mas kok pucet banget? Bibir Mas kering gitu."
    b "Nggak apa-apa, Dek. Kurang minum doang. Mas buru-buru, si Hartono minta revisi."
    r "Mas... Ibu semalam sadar sebentar. Ibu nyariin Mas."
    r "Katanya: 'Bima mana? Bima janji mau nemenin Ibu kontrol hari ini'."
    
    b "..."
    n "Langkah Bima terhenti saat memasang sepatu. Janji itu. Dia lupa total karena deadline."

    # CHOICE 2: HUBUNGAN KELUARGA (BLIND)
    menu:
        "Rina menatap dengan mata penuh harap. Bima merasa terpojok."

        "Jelaskan baik-baik & Minta Maaf.":
            $ family_bond += 1
            $ renpy.notify("Hubungan Keluarga: Erat (+1)")
            
            b "(Berlutut sedikit menyamakan tinggi dengan Rina) Dek, dengerin Mas."
            b "Maafin Mas ya. Mas lupa. Kepala Mas isinya kerjaan semua."
            b "Tolong bilangin Ibu, Mas cari uang obat dulu. Kelar ini Mas langsung ke RS. Janji."
            
            show rina senyum at left
            r "Iya Mas... Rina ngerti kok. Mas hati-hati ya. Jangan ngebut."
            n "Rina tersenyum tipis. Dia tahu kakaknya berjuang keras."

        "Marah karena merasa ditekan.":
            $ family_bond -= 1
            $ renpy.notify("Hubungan Keluarga: Renggang (-1)")
            
            b "Dek! Bisa nggak sih pagi-pagi jangan bikin Mas makin stress?!"
            b "Mas kerja banting tulang buat siapa?! Buat Ibu juga kan?! Jangan nuntut macem-macem deh!"
            
            show rina nangis at left
            r "..."
            n "Rina mundur ketakutan. Bima langsung menyambar helm dan keluar tanpa pamit, meninggalkan adiknya yang menangis."

    hide rina
    hide bima
    with dissolve
    
    # TRANSISI PERJALANAN 
    scene bg hujan_jalan with fade
    n "Jalanan Jakarta macet total. Klakson bersahut-sahutan."
    n "Di balik helm, Bima merasa tercekik. Antara rasa bersalah pada Rina, dan ketakutan pada Bosnya."

    # --- SCENE: KANTOR (THE CONFLICT) ---
    scene bg kantor with fade
    n "Jam 10:00 WIB. Ruangan Divisi Kreatif."
    n "Hening. Semua karyawan menunduk, takut melakukan kontak mata dengan 'Raja Iblis' di ruangan kaca."

    show bima lelah at left
    show hartono marah at right with vpunch
    
    h "BIMA PRATAMA!"
    b "(Tersentak) S-saya Pak?"
    
    h "Sini kamu! Liat layar ini!"
    h "Saya minta konsep 'Elegan & Mewah'. Kenapa kamu kasih saya desain pasar malam begini hah?!"
    h "Warna apa ini? Norak! Font-nya murahan! Kamu ini Sarjana Desain atau tukang sablon?!"
    
    b "Tapi Pak... di brief awal Bapak bilang referensinya 'Colorful'..."
    
    h "JANGAN NGEJAWAB!"
    h "Salah ya salah! Klien itu Raja! Kalau Klien nggak suka, berarti desainmu SAMPAH!"
    h "Rombak total. Saya nggak mau tau, besok pagi jam 8 sudah harus ada di meja saya."
    h "Kalau nggak... SP 3. Dan jangan harap pesangon cair."
    
    hide hartono with moveoutright
    n "Pak Hartono membanting pintu ruangan. Bima berdiri terpaku di tengah kantor. Harga dirinya serasa diludahi di depan rekan kerjanya."

    # CHOICE 3: RESPON MENTAL (BLIND)
    menu:
        "Dada Bima sesak. Emosi bercampur aduk."

        "Tahan Bima. Fokus Solusi.":
            $ mental_bima += 1
            $ renpy.notify("Mental Bima: Stabil (+1)")
            b "(Tarik napas panjang, hembuskan) Oke... Oke."
            b "Dia cuma orang tua yang lagi stress. Jangan dimasukin hati. Lo butuh gaji ini."
            b "Fokus revisi. Semakin cepet kelar, semakin cepet gue bisa ke RS."

        "Simpan Dendam & Mengumpat.":
            $ mental_bima -= 1
            $ renpy.notify("Mental Bima: Retak (-1)")
            b "(Mengepalkan tangan di saku celana) Tua bangka sialan..."
            b "Liat aja nanti. Kalau gue sukses, gue beli mulut sombong lo itu."
            n "Bima duduk dengan kasar. Dia mengetik keyboard seolah ingin menghancurkannya."

    # --- SCENE SPESIAL: MID-GAME IMPACT (REVISI: FRUSTASI DI MEJA) ---
    # Scene ini berubah tergantung poin mental, tapi tetap pakai aset yang ada.
    
    scene bg kantor_malam with dissolve
    n "Jam 21:00 WIB. Kantor sudah sepi."
    n "Hanya tersisa Bima. Lampu ruangan berkedip-kedip."

    if mental_bima < 0:
        # === JALUR MENTAL RUSAK (FRUSTASI) ===
        # Tidak perlu aset baru, cukup efek suara dan gerakan
        
        n "Tekanan di kepala Bima sudah tidak tertahankan. Suara bentakan Hartono terus terngiang seperti kaset rusak."
        
        show bima marah at center with vpunch
        
        "{b}BRAKK!!!{/b}"
        n "Bima menggebrak meja kerjanya sekuat tenaga."
        
        b "Kenapa sih?! Kenapa hidup gue nggak pernah mudah?!"
        b "Gue udah lakuin semuanya bener! Gue kerja keras, gue nurut... tapi tetep aja diinjek-injek!"
        
        n "Napasnya memburu. Dia menjambak rambutnya sendiri, merasa terjebak."
        b "(Lirih) Gue capek Bu... Gue capek jadi orang yang selalu ngalah. Kapan giliran Bima bahagia?"
        
        n "Bima menelungkupkan wajahnya di antara tumpukan kertas revisi. Hatinya lelah."

    else:
        # === JALUR MENTAL KUAT (TENANG) ===
        
        n "Mata Bima terasa panas, tapi pikirannya masih jernih."
        n "Dia berdiri sejenak, melihat ke jendela luar yang menampilkan hujan Jakarta."
        
        show bima tegas at center
        
        b "(Menghela napas panjang) Huh..."
        b "Sabar Bim. Badai pasti berlalu. Inget muka Ibu. Inget Rina."
        b "Lo kerja bukan buat si Hartono. Lo kerja buat orang-orang yang lo sayang."
        
        n "Bima meminum sisa air putih di botolnya. Dinginnya air sedikit menenangkan pikirannya."
        b "Oke. Satu ronde lagi. Ayo kita selesaikan."
        
        n "Dia kembali duduk tegak. Jari-jemarinya kembali menari di atas keyboard dengan fokus tajam."

    # --- SCENE: KLIMAKS (THE CALL) ---
    
    n "Jam 23:45 WIB. Hujan badai mengguyur kaca jendela."
    
    # Efek Jantung
    scene bg kantor_malam with heart_beat
    pause 0.5
    scene bg kantor_malam with heart_beat
    
    "{b}{color=#e53935}INCOMING CALL: RINA{/color}{/b}"
    
    b "(Jantung seakan berhenti) Halo... Dek?"
    
    r "{i}(Suara tangis histeris, nyaris tidak jelas){/i} MAS BIMA! MAS DIMANA?!"
    r "Ibu Mas... Napas Ibu sempet berenti tadi! Dokter lagi pompa jantung Ibu sekarang!"
    r "Mas cepetan ke sini... Aku takut sendirian Mas... Aku nggak mau Ibu pergi..."
    
    n "Dunia Bima runtuh seketika. Laptop, Deadline, Karir... semuanya mendadak menjadi debu."
    b "Mas... Mas jalan sekarang."

    # HARTONO BLOCKS THE WAY
    show hartono dingin at right with dissolve
    
    h "Eits. Mau kemana kamu? Buru-buru amat."
    h "Saya cek email, file revisinya belum masuk. Jangan bilang kamu mau kabur."
    
    b "Pak... Ibu saya kritis. Di UGD. Saya harus pergi detik ini juga."
    
    h "(Tertawa meremehkan) Halah. Alasan klasik. Kemarin sakit, sekarang sekarat. Drama banget hidup kamu."
    h "Dengar ya Bima. Klien besok datang jam 8 pagi. Proyek ini nilainya Milyaran."
    h "Kalau kamu melangkah keluar dari pintu itu sebelum file ini selesai..."
    h "Simpan saja ID Card kamu. Saya pastikan nama kamu saya blacklist dari semua agensi di Jakarta. Karirmu tamat."
    
    b "..."
    h "Pikir pake logika, Bima. Kamu butuh duit buat bayar RS kan? Selesaikan kerjamu, baru jadi pahlawan kesiangan."

    # --- LOGIC GATE (PENENTUAN ENDING) ---
    n "Waktu seakan berhenti. Di kiri pintu keluar (Cinta). Di depan monitor (Logika/Uang)."
    
    if mental_bima < 0:
        n "Bima menatap tangannya yang masih sakit karena menggebrak meja tadi."
        n "Dia merasa terlalu lemah untuk melawan..."
    else:
        n "Bima teringat janjinya pada diri sendiri. Pikirannya jernih."
        n "Dia tahu apa yang benar..."

    # SYARAT ENDING
    if mental_bima >= 1 and family_bond >= 1:
        jump ending_true_masterpiece
    elif family_bond >= 1:
        jump ending_neutral_masterpiece
    else:
        jump ending_bad_masterpiece

# ==============================================================================
# 4. ENDINGS (FINAL PAYOFF - FULL DETAIL)
# ==============================================================================

label ending_bad_masterpiece:
    # Syarat: Mental Hancur ATAU Hubungan Keluarga Hancur
    
    show bima lelah at left
    b "(Menunduk dalam, air mata menetes) ..."
    b "(Dalam hati) Pak Hartono bener. Kalau gue dipecat dan di-blacklist, gue bayar RS pake apa? Gue nggak punya pilihan."
    
    b "Maaf, Pak. Saya... saya selesaikan. Tolong jangan pecat saya."
    h "Nah, gitu dong. Itu baru profesional. Jangan cengeng. Saya tunggu di ruangan saya."
    hide hartono with moveoutright

    scene bg kantor_malam
    n "Bima duduk kembali ke kursinya. Kursi yang terasa seperti kursi listrik."
    n "Dia mengetik revisi dengan air mata yang terus menetes ke keyboard. Dia menjual momen terakhir ibunya demi keamanan finansial."
    n "Jam 03:00 Pagi. File terkirim."
    
    scene bg rumah_sakit with slow_dissolve
    n "Subuh. Bima berlari menyusuri lorong RS. Sepi. Dingin."
    show rina senyum at center
    # Rina senyum kosong
    
    b "Dek! Ibu gimana? Mas udah transfer gaji Mas semua buat obat."
    r "..."
    r "Uangnya udah masuk, Mas. Makasih. Tapi Ibu udah nggak butuh obat lagi."
    
    b "Maksud kamu...?"
    r "(Menatap Bima dingin) Ibu udah tidur selamanya, Mas. Tadi Ibu nungguin Mas sampai napas terakhir."
    r "Ibu manggil 'Bima... Bima...' terus. Tapi Mas nggak dateng."
    r "Mas pulang aja. Urus aja kerjaan Mas yang penting itu. Rina bisa urus pemakaman sendiri."
    
    hide rina with dissolve
    n "Bima berdiri sendiri di lorong. Dia punya uang, dia punya karir. Tapi dia sendirian di dunia ini."
    
    "{b}{size=40}{color=#ff0000}BAD ENDING: BONEKA BERNYAWA{/color}{/size}{/b}\n(Kamu selamat secara finansial, tapi jiwamu mati malam ini.)"
    return

label ending_neutral_masterpiece:
    # Syarat: Hubungan Keluarga Bagus (Mental boleh jelek)
    # Reaksi Emosional / Nekat
    
    show bima marah at left with vpunch
    b "CUKUP PAK!!! SAYA MUAK!"
    
    h "Hah?! Kamu bentak saya?!"
    b "Bapak pikir saya ini robot?! Ibu saya lagi bertaruh nyawa di sana!"
    b "Persetan sama Klien! Persetan sama Blacklist Bapak! Saya resign detik ini juga!"
    
    n "Bima melempar ID Card-nya tepat ke wajah Hartono. Dia berlari keluar tanpa menoleh."
    
    scene bg hujan_jalan with flash
    n "Bima memacu motornya menembus badai. Basah kuyup. Dingin. Dia tahu besok dia pengangguran."
    n "Tapi anehnya... dadanya terasa lapang. Beban ribuan ton baru saja diangkat."

    scene bg rumah_sakit with slow_dissolve
    show rina nangis at left
    show bima tegas at right
    
    b "DEK! IBU!"
    r "Mas Bima! Mas dateng!"
    
    n "Rina memeluk kakaknya erat. Dokter keluar dari ruangan dan mengangguk."
    r "Ibu selamat Mas... Kritisnya lewat. Ibu kuat banget."
    
    b "(Jatuh terduduk lemas) Alhamdulillah..."
    b "Dek, maafin Mas ya. Mas udah keluar dari kerjaan. Mas sekarang pengangguran."
    b "Kita mungkin bakal susah makan besok. Motor Mas mungkin harus dijual."
    
    r "(Tersenyum sambil menghapus air mata) Nggak apa-apa Mas. Kita makan nasi garem bareng-bareng."
    r "Yang penting Mas Bima ada di sini. Itu udah cukup buat Rina."
    
    "{b}{size=40}{color=#FFD700}NEUTRAL ENDING: KEBEBASAN YANG NEKAT{/color}{/size}{/b}\n(Kamu kehilangan karir, tapi memenangkan kembali keluargamu.)"
    return

label ending_true_masterpiece:
    # Syarat: Mental Kuat (+1) DAN Hubungan Keluarga Kuat (+1)
    # Reaksi Cerdas / Negosiasi
    
    show bima tegas at left
    b "(Menatap tajam mata Hartono, aura wibawanya keluar)"
    b "Pak Hartono. Minggir."
    
    h "Kamu berani ngelawan?"
    
    b "Saya tidak melawan. Saya bernegosiasi."
    b "Saya pergi ke RS sekarang membawa laptop ini. Saya kerjakan di sana."
    b "File sampai di email Bapak subuh nanti. Klien puas, Bapak aman. Win-win solution."
    
    h "Kalau saya bilang nggak boleh?"
    
    b "Maka saya akan teriak sekarang juga. Saya rekam percakapan ini."
    b "Akan saya sebar ke sosmed bahwa 'Hartono Agency' menahan karyawan yang ibunya sekarat."
    b "Bapak mau reputasi Bapak hancur dalam semalam? Netizen suka berita ginian, Pak."
    
    h "..."
    h "(Wajahnya pucat, sadar dia kalah) ...Cih."
    h "Pergi sana. Awas kalau file-nya jelek."
    
    scene bg rumah_sakit with fade
    n "Suasana RS tenang."
    show bima lelah at center
    
    n "Bima duduk di lantai ruang tunggu, memangku laptopnya. Di sebelahnya Rina tertidur lelap di bahunya."
    n "Di ranjang, Ibu bernapas dengan tenang. Kritisnya sudah lewat."
    
    b "(Menekan tombol Enter) Sent. Revisi selesai."
    
    n "Bima menutup laptopnya perlahan. Dia berhasil."
    n "Dia tidak menjadi budak, dan dia tidak menjadi pemberontak yang bodoh."
    n "Dia membuktikan bahwa dia adalah seorang Pria yang memegang kendali atas hidupnya sendiri."
    
    "{b}{size=40}{color=#00e676}TRUE ENDING: MASTER OF LIFE{/color}{/size}{/b}\n(Logika dan Hatimu berjalan seirama. Kamu menang telak.)"
    return