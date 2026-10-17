################################################################################
## 08_extras.rpy — Galería y Finales (provisional)
################################################################################

screen galeria():
    tag menu
    use game_menu(_("Galería")):
        text "Próximamente: aquí irán los CG que desbloquees." size 30

screen finales():
    tag menu
    use game_menu(_("Finales")):
        text "Próximamente: aquí irán los finales que descubras." size 30