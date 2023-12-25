import reflex as rx
from my_personal_web_site_with_reflex.styles.styles import styles

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            #rx.icon(tag="hamburger"),
            rx.image(src="/icons/house-solid.svg"),
            rx.spacer(),
            rx.button("Profile", variant="link", text_color="#000080"),
            rx.button("Carreer", variant="link", text_color="#000080"),
            rx.button("Links", variant="link", text_color="#000080"),
            rx.spacer(),
            rx.text("R. M. Ginés", font_size="0.6em"),
        ),
        style = styles["navbar_style"]
    )
