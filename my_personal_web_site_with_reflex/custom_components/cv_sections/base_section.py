import reflex as rx
from my_personal_web_site_with_reflex.styles.styles import styles

def base_section(title:str, body_text:str, icon_src:str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.image(
                    src = icon_src,
                ),
                rx.text(
                    f"{title}",
                    style=styles["cv_title_style"],
                ),
                width = "100%",
            ),       
            rx.text(
                f"{body_text}",
                style=styles["cv_body_style"],
            ),
        ),        
        style=styles["cv_section_style"],
    )