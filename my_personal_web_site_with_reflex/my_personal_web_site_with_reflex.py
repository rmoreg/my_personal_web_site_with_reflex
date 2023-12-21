"""Welcome to Reflex!."""

from my_personal_web_site_with_reflex import styles

# Import all the pages.
from my_personal_web_site_with_reflex.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
