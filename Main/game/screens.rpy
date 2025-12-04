
################################################################################
## Inisialisasi
################################################################################

init offset = -1


################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Layar In-game
################################################################################


## Layar Say ###################################################################
##
## Layar say di gunakan untuk menampilkan dialog kepada pemain. Ini menggunakan
## dua parameter, who dan what, yang merupakan nama karakter yang berbicara dan
## text yang akan di tampilkan, masing-masing. (Kedua parameter dapat berisi
## None jika tidak ada nama yang di berikan.
##
## Layar ini harus membuat text yang dapat di tampilkan dengan id "what", yang
## di mana Ren'Py menggunakan ini untuk mengatur tampilan text. Ini juga dapat
## membuat sesuatu yang dapat di tampilkan dengan id "who" dan id "window" untuk
## mengaplikasikan properti gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jika ada gambar di sisi, tampilkan di atas text. Jangan tampilkan di
    ## versi HP[Handphone)(Android) - Karena tidak ada ruang.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Layar masukkan/input ########################################################
##
## Layar ini di gunakan untuk menampilkan renpy.input. Parameter prompt
## digunakan untuk meneruskan text yang di prompt/minta.
##
## Layar ini harus membuat input yang dapat di tampilkan dengan id "input"
## untuk menerima berbagai parameter masukan.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Layar Pilihan ###############################################################
##
## Layar ini digunakan untuk menampilkan pilihan dalam game yang disajikan oleh
## menu statement. Satu parameter, item, adalah daftar objek, masing-masing
## dengan bidang keterangan dan tindakan.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# =========================================================
# CHOICE MENU - VERSI CODING (FINAL & FIXED)
# =========================================================

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20 # Jarak antar tombol

        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button"

# ---------------------------------------------------------
# STYLE DEFINITION
# ---------------------------------------------------------

style choice_vbox:
    xalign 0.5
    yalign 0.5

style choice_button is button:
    # --- BAGIAN YANG DIPERBAIKI ---
    # Hapus baris 'properties' sepenuhnya.
    # Kita atur manual di sini:
    
    # 1. Ukuran Tombol
    xsize 700
    ysize 70
    xalign 0.5
    yalign 0.5
    
    # 2. Warna Background (Pakai Kode Warna / Solid)
    # Format: "#RRGGBB" (Hex Color) atau "#RRGGBBAA" (Transparan)
    
    # Saat diam (Abu-abu Gelap Transparan)
    background Solid("#212121cc") 
    
    # Saat disentuh (Abu-abu Terang)
    hover_background Solid("#505050ff")
    
    # 3. Jarak teks ke pinggir
    padding (50, 10)

style choice_button_text is text:
    # Hapus baris 'properties' text juga biar aman
    
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 30
    
    # Warna Teks
    color "#ffffff"          # Putih
    hover_color "#ffcc00"    # Kuning Emas saat di-hover
    
    # Outline (Garis pinggir teks biar jelas)
    outlines [(1, "#00000088", 1, 1)]## Layar Menu Cepat/Quick Menu #################################################
##
## Menu cepat ditampilkan dalam game untuk memudahkan akses ke menu di luar
## game.

screen quick_menu():

    ## Memastikan ini muncul di atas layar yang lain.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Kembali") action Rollback()
            textbutton _("Riwayat") action ShowMenu('history')
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Simpan") action ShowMenu('save')
            textbutton _("Simpan.C") action QuickSave()
            textbutton _("Muat.C") action QuickLoad()
            textbutton _("Setting") action ShowMenu('preferences')


## Kode ini memastikan layar quick_menu di tampilkan di dalam permainan,
## kapanpun player tidak secaralangsung menyembunyikan antarmuka.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Layar Menu Utama dan Menu Permainan
################################################################################

## Layar navigasi ##############################################################
##
## Layar ini di ikutsertakan di menu utama dan permainan, dan menyediakan
## navigasi ke menu lainnya, dan untuk memulai permainan.

screen navigation():

    vbox:
        style_prefix "navigation"

        # POSISI MENU (Kiri Tengah - Gaya Modern)
        xpos 120
        yalign 0.5
        
        spacing 10 # Jarak antar tombol

        if main_menu:
            textbutton _("MULAI") action Start()
        else:
            textbutton _("RIWAYAT") action ShowMenu("history")
            textbutton _("SIMPAN") action ShowMenu("save")

        textbutton _("MUAT") action ShowMenu("load")
        textbutton _("SETTING") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("AKHIRI REPLAY") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("MENU UTAMA") action MainMenu()

        textbutton _("TENTANG") action ShowMenu("about")

        if renpy.variant("pc"):
            # Beri jarak sedikit untuk tombol keluar
            null height 30
            textbutton _("KELUAR") action Quit(confirm=not main_menu)

# --- GAYA TOMBOL NAVIGASI MODERN ---

# --- GAYA TOMBOL NAVIGASI MODERN (FIXED) ---

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    
    # --- BAGIAN PERBAIKAN ---
    # HAPUS baris 'properties ...' sepenuhnya.
    # Kita atur manual ukuran dan backgroundnya di sini:
    
    # Ukuran area tombol
    xsize 400
    ysize 60
    
    # Background: Transparan saat diam, Putih Transparan saat disentuh
    background None
    hover_background Solid("#ffffff15") 

style navigation_button_text:
    # HAPUS juga properties di sini
    
    # Font & Ukuran
    # Saya comment font-nya agar tidak error "File Not Found" jika kamu belum punya file font-nya
    # font "gui/font/DejaVuSans.ttf" 
    
    size 40
    xalign 0.0 # Rata Kiri
    
    # WARNA TEKS
    color "#b0bec5"          # Abu-abu kebiruan (Idle)
    hover_color "#ffca28"    # Kuning Emas (Hover/Disentuh)
    selected_color "#ffffff" # Putih (Saat menu aktif)
    
    # ANIMASI MIKRO
    # Teks akan geser 15 pixel ke kanan saat disentuh mouse
    hover_xoffset 15 
    
    # Outline biar teks tajam
    outlines [(2, "#000000", 2, 2)]

# --- GAYA JUDUL GAME ---
style main_menu_title:
    properties gui.text_properties("title")
    size 80
    
    # Baris font saya hapus juga
    # font "gui/font/DejaVuSans.ttf"
    
    color "#ffffff"
    outlines [(3, "#000000", 2, 2)]

style main_menu_version:
    properties gui.text_properties("version")
    size 24


## Layar Menu utama ############################################################
##
## Digunakan untuk menampilkan menu utama ketika Ren'Py dimulai.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Tag ini memastikan layar menu lain diganti.
    tag menu

    # 1. Background Gambar Utama
    add gui.main_menu_background

    # 2. OVERLAY GRADASI (Biar teks kebaca & Cinematic)
    # Kita pakai Solid color hitam transparan (Alpha 0.6)
    add Transform(Solid("#00000099"), alpha=0.7)

    # 3. NAVIGASI (Tombol Mulai, dll)
    use navigation

    # 4. JUDUL GAME & VERSI (Rata Kanan Bawah)
    if gui.show_name:

        vbox:
            # Posisi Judul
            xalign 0.95
            yalign 0.90
            spacing 10

            text "[config.name!t]":
                style "main_menu_title"
                xalign 1.0 # Rata kanan

            text "v[config.version]":
                style "main_menu_version"
                xalign 1.0 # Rata kanan
                color "#cfd8dc" # Abu terang


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## layar Menu Permainan ########################################################
##
## Ini menjalaskan struktur dasar yang paling sering di gunakan di layar
## menu permainan, ini ditampilkan beserta layar judul, dan menampilkan latar
## belakang,judul,dan navigasi.
##
## Parameter scroll dapat berisi 'None', atau "viewport" dan "vpgrid". Layar
## ini di maksudkan untuk di gunakan dengan cabang satu atau lebih, yang di
## tempatkan di dalamnya.

# --- UPDATE FIX: MENAMBAHKAN SPACING ---

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    # 1. PASANG GAMBAR BACKGROUND GAME
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.background_menu

    # 2. BERI EFEK "DARK GLASS" (Overlay Hitam Transparan)
    # Ini bikin terlihat mewah. Tidak hitam polos, tapi tidak nabrak teks.
    add Solid("#000000e6") # Hitam 90% (Ganti e6 jadi cc kalau mau lebih terang)

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Navigasi Kiri
            frame:
                style "game_menu_navigation_frame"

            ## Konten Kanan
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    vbox:
                        spacing spacing
                        transclude

    use navigation

    text title:
        style "game_menu_label_text"

    ## Tombol Kembali (Opsional, biasanya sudah tercover oleh navigasi)
    # textbutton _("Return"):
    #    style "return_button"
    #    action Return()


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    background None # Pastikan bersih
    bottom_padding 30
    top_padding 120
    left_padding 30
    right_padding 30

style game_menu_navigation_frame:
    xsize 400
    yfill True

style game_menu_content_frame:
    left_margin 420
    top_margin 10

style game_menu_label_text:
    size 60
    color "#ffffff" # Putih Bersih
    xalign 0.0
    ypos 40
    xpos 480 
    # Outline tipis biar tajam
    outlines [(2, "#00000088", 2, 2)]

## Layar About #################################################################
##
## Layar ini menampilkan credit dan informasi copyright tentang game dan Ren.Py.
##
## Tidak ada yang spesial dengan layar ini, semenjak ini juga berperan sebagai
## contoh bagaimana membuat layar custom.

screen about():

    tag menu

    ## Kita gunakan game_menu yang sudah kita perbaiki tadi (Background gelap)
    use game_menu(_("TENTANG"), scroll="viewport"):

        style_prefix "about"

        vbox:
            spacing 20 # Jarak antar elemen

            # 1. Judul Game (Besar & Keren)
            label "[config.name!t]":
                style "about_header" 

            # 2. Versi Game
            text _("Version [config.version!t]"):
                style "about_version"

            # 3. Garis Pemisah (Divider) biar rapi
            add Solid("#ffffff33", xsize=800, ysize=2)

            # 4. Isi "About" (Credits/Deskripsi)
            # Pastikan kamu isi gui.about di options.rpy nanti
            if gui.about:
                text "[gui.about!t]":
                    style "about_text"

            # 5. Credits Engine (Wajib ada lho, biar legal)
            null height 20
            text _("Dibuat dengan {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
                style "about_text_small"

# --- GAYA MENU TENTANG (PROFESSIONAL LOOK) ---

style about_header is gui_label
style about_version is gui_text
style about_text is gui_text
style about_text_small is gui_text

# Judul Game di halaman About
style about_header_text:
    color "#ffca28"    # Kuning Emas
    size 50
    xalign 0.0
    outlines [(2, "#000000", 2, 2)] # Outline tebal

# Teks Versi
style about_version:
    color "#b0bec5"    # Abu kebiruan
    size 24
    xalign 0.0

# Teks Utama (Isi Credits)
style about_text:
    color "#eceff1"    # Putih Tulang (Nyaman di mata)
    size 26
    xalign 0.0
    layout "subtitle"  # Agar paragraf rapi
    line_spacing 5

# Teks Kecil (Lisensi Renpy)
style about_text_small:
    color "#78909c"    # Abu Gelap
    size 20
    xalign 0.0
    
# Style Hyperlink (Biar link RenPy kelihatan bagus)
style hyperlink_text:
    color "#4fc3f7"    # Biru Muda Neon
    hover_color "#ffffff"
    underline False

## Layar Load and Save #########################################################
##
## Layar ini bertanggungjawab untuk mengijinkan pemain menyimpan dan
## meload lagi. Semenjak mereke hampir memiliki hal yang sama, keduanya di
## implementasinan di percabangan layar ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Simpan"))


screen load():

    tag menu

    use file_slots(_("Muat"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Otomatis Save"), quick=_("Save Cepat"))

    use game_menu(title):

        fixed:
            order_reverse True

            ## JUDUL HALAMAN (Geser ke Kiri, Warna Putih)
            button:
                style "page_label"
                key_events True
                xalign 0.90 # Geser ke 0.90 (Aman dari potongan layar)
                yalign 0.03
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## GRID SLOT (3 Kolom x 2 Baris = 6 Slot)
            ## Solusi anti kepotong.
            grid 3 2:
                style_prefix "slot"
                xalign 0.5
                yalign 0.45
                spacing 25

                for i in range(3 * 2):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        
                        text FileTime(slot, format=_("{#file_time}%d %b %Y, %H:%M"), empty=_("Slot Kosong")):
                            style "slot_time_text"
                        
                        text FileSaveName(slot):
                            style "slot_name_text"
                        
                        key "save_delete" action FileDelete(slot)

            ## NAVIGASI BAWAH
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 0.96
                spacing 10

                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("Q") action FilePage("quick")
                for page in range(1, 6):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
                key "save_page_next" action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

# --- GAYA SLOT SAVE/LOAD MODERN ---

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_button:
    xsize 380
    ysize 260
    
    # Warna Semi-Transparan (Biar background game kelihatan dikit)
    background Solid("#263238cc") 
    hover_background Solid("#37474fee")
    padding (10, 10)

style slot_button_text:
    size 20
    color "#eceff1"
    xalign 0.5

style slot_time_text:
    size 16
    color "#90a4ae"
    xalign 0.5

style page_label:
    xpadding 50
    ypadding 5
    xalign 0.5

style page_button:
    # Hapus properties default
    # properties gui.button_properties("page_button")
    
    # Gaya tombol halaman minimalis
    xpadding 15
    ypadding 10
    background None
    hover_background Solid("#ffffff20") # Highlight halus

style page_button_text:
    # Hapus properties default
    # properties gui.text_properties("page_button")
    
    color "#b0bec5"
    hover_color "#ffca28" 
    size 30
    
    # HAPUS BARIS FONT DI BAWAH INI:
    # font "gui/font/DejaVuSans.ttf"

style page_label_text:
    color "#ffffff"
    size 28
    outlines [(2, "#000000", 1, 1)]




## Layar preferensi/opsi #######################################################
##
## Layar preferensi mengijinkan pemain untuk mengkonfigurasi permainan untuk
## menyesuaikan gaya bermain masing masing individu.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Setting"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Tampilan")
                        textbutton _("Jendela") action Preference("display", "window")
                        textbutton _("Layar Penuh") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Lompati")
                    textbutton _("Belum Terlihat") action Preference("skip", "toggle")
                    textbutton _("Setelah Pilihan") action Preference("after choices", "toggle")
                    textbutton _("Transisi") action InvertSelected(Preference("transitions", "toggle"))

                ## Tipe tambahan vboxes "radio_pref" atau "check_pref" dapat di
                ## tambahkan disini, untuk menambahkan tambahan preferensi yang
                ## dibuat creator.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Kecepatan Text")

                    bar value Preference("text speed")

                    label _("Waktu Otomatis-Maju")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume Musik")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume Suara")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Tes") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume Vokal")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Tes") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Senyapkan Semua"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Layar Riwayat ###############################################################
##
## Layar yang menampilkan History dialog kepada pemain. Semenjak tidak ada
## yang spesial tentang layar ini, ini memiliki akses ke history dialog yang di
## simpan di _history_list.
##
## https://www.renpy.org/doc/html/history.html

## Layar Riwayat (History) #####################################################

screen history():

    tag menu

    ## Prediksi dimatikan karena layar ini bisa sangat panjang
    predict False

    use game_menu(_("RIWAYAT"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Layout dasar: Nama di atas, Teks di bawahnya (Lebih rapi)
                has vbox:
                    xfill True
                    spacing 5

                ## Bagian Nama Karakter
                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        ## Gunakan warna asli karakter jika ada
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                ## Bagian Teks Dialog
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Riwayat dialog kosong.")


## Ini menentukan tag apa yang diizinkan ditampilkan di layar sejarah/catatan.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height
    
    # Beri sedikit jarak antar percakapan
    bottom_margin 20 

style history_name:
    xpos 0
    xalign 0.0
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign 0.0
    align (0.0, 0.5)
    
    # Warna Nama Default (Kalau karakter ga punya warna)
    color "#ffca28" 
    size 24
    bold True

style history_text:
    xpos 0
    ypos 2
    xanchor 0.0
    xsize 1000 # Batasi lebar teks biar ga nabrak kanan
    
    textalign 0.0
    layout ("subtitle" if gui.history_text_xalign else "tex")
    
    # --- BAGIAN PENTING: WARNA TEKS ---
    color "#eceff1" # Putih Tulang (Kontras dengan background gelap)
    size 22

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Layar Bantuan ###############################################################
##
## Layar yang memberikan informasi tentang keyboard dan mouse binding. Ini
## menggunakan layar lain (keyboard_help, mouse_help, and gamepad_help) untuk
## menampilkan bantuan yang sebenarnya.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Bantuan"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Papanketik") action SetScreenVariable("device", "keyboard")
                textbutton _("Tetikus") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Masukkan")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Spasi")
        text _("Dialog tingkat lanjut tanpa memilih pilihan.")

    hbox:
        label _("Tombol Panah")
        text _("Navigasi di antarmuka")

    hbox:
        label _("Melarikan diri")
        text _("Akses menu permainan.")

    hbox:
        label _("Ctrl")
        text _("Lompati dialog ketika di tahan.")

    hbox:
        label _("Tab")
        text _("Nyala/Matikan lompati dialog.")

    hbox:
        label _("Halaman Atas")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Page Down")
        text _("Putar maju ke dialog berikut.")

    hbox:
        label "H"
        text _("Sembunyikan antarmuka.")

    hbox:
        label "S"
        text _("Ambiil tangkapan layar.")

    hbox:
        label "V"
        text _("Nyalakan assisten {a=https://www.renpy.org/l/voicing}suara-sendiri{/a}")

    hbox:
        label "Shift+A"
        text _("Membuka menu aksesibilitas.")


screen mouse_help():

    hbox:
        label _("Klik Kiri")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Klik Tengah")
        text _("Sembunyikan antarmuka.")

    hbox:
        label _("Klik Kanan")
        text _("Akses menu permainan.")

    hbox:
        label _("Roda Mouse Atas")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Roda Mouse Bawah")
        text _("Putar maju ke dialog berikut.")


screen gamepad_help():

    hbox:
        label _("Trigger Kanan\nA/Tombol Bawah")
        text _("Dialog tingkat lanjut dan mengaktifkan antarmuka.")

    hbox:
        label _("Trigger Kiri\nBahu Kiri")
        text _("Putar mundur ke dialog sebelumnya.")

    hbox:
        label _("Pundak Kanan")
        text _("Putar maju ke dialog berikut.")

    hbox:
        label _("D-Pad, Stick")
        text _("Navigasi di antarmuka")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Akses menu permainan.")

    hbox:
        label _("Y/Tombol Atas")
        text _("Sembunyikan antarmuka.")

    textbutton _("Kalibrasi") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Layar Tambahan
################################################################################


## Layar konfirmasi ############################################################
##
## Layar konfirmasi di panggil ketika Ren'Py mau menanyakan ke pemain
## pertanyaan ya atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Memastikan layar lain tidak mendapatkan input ketika layar ini di
    ## panggil.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Ya") action yes_action
                textbutton _("Tidak") action no_action

    ## Klik kanan dan jawaban escape "Tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Lompati indikator layar #####################################################
##
## layar skip_indicator di tampilkan untuk mengindikasian proses skipping
## sedang dalam proses.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melompati")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## transform digunakan untuk mengkedipkan panah setelah yang lain.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami harus menggunakan font yang mempunyai glyph BLACK RIGHT-POINTING
    ## SMALL TRIANGLE didalamnya.
    font "DejaVuSans.ttf"


## Layar pemberitahuan #########################################################
##
## layar notify digunakan untuk menampilkan pesan kepada pemain. (Seperti,
## ketika game di simpan cepat atau screenshot di ambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Layar NVL ###################################################################
##
## Layar ini digunakan untuk dialog dan menu mode-NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Menampilkan dialog pada vpgrid atau vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Menampilkan menu, jika diberikan. Menu dapat ditampilkan dengan
        ## tidak benar jika config.narrator_menu diatur ke True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengendalikan angka maksimum entri mode-NVL yang dapat di tampilkan
## sekaligus.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Layar gelembung #############################################################
##
## Layar gelembung digunakan untuk menampilkan dialog kepada pemain saat
## menggunakan gelembung ucapan. Layar gelembung mengambil parameter yang sama
## dengan layar ucapkan, harus membuat tampilan dengan id "apa", dan dapat
## membuat tampilan dengan id "kotak nama", "siapa", dan "jendela".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Versi Mobile(HP/Handphone/Android)
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Semenjak mouse tidak ada, kami mengganti menu cepat dengan yang menggunakan
## tombol yang lebih besar dan sedikit, yang memudahkan untuk di sentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Kembali") action Rollback()
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900