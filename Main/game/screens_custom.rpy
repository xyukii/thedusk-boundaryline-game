################################################################################
## Custom main-menu helper screens
################################################################################

## Screen that offers Start New or Load when player presses the main "Mulai" button.
screen start_or_load():

    tag menu

    use game_menu(_("Mulai")):

        vbox:
            spacing 30

            textbutton _("Mulai Baru"):
                style "navigation_button"
                action Start()

            textbutton _("Muat"):
                style "navigation_button"
                action ShowMenu("load")

            textbutton _("Kembali"):
                style "navigation_button"
                action Return()


## Combined settings hub that links to Preferences / About / Help. This keeps
## the original screens for each page intact and simply centralises access.
screen settings_menu():

    tag menu

    use game_menu(_("Setting")):

        vbox:
            spacing 20

            textbutton _("Setting"):
                style "navigation_button"
                action ShowMenu("preferences")

            textbutton _("Tentang"):
                style "navigation_button"
                action ShowMenu("about")

            textbutton _("Bantuan"):
                style "navigation_button"
                action ShowMenu("help")

            null height 20

            textbutton _("Kembali"):
                style "return_button"
                action Return()
