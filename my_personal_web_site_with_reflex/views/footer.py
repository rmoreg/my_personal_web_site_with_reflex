import reflex as rx
from my_personal_web_site_with_reflex.styles.styles import styles

from datetime import datetime

def footer() -> rx.Component:
    year = datetime.now().year
    return rx.box(
        rx.text(f"{year}", color="#FFFAF0", text_align="right"),  
        bg = "#000080",
        width="100%",
        bottom = "0",
        padding = "1em"
    )