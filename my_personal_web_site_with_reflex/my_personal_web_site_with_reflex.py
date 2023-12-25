"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from my_personal_web_site_with_reflex.custom_components.navbar import navbar
from my_personal_web_site_with_reflex.views.header import header
from my_personal_web_site_with_reflex.views.footer import footer
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return  rx.vstack(
                navbar(),
                header(),
                rx.image(src="skyline_madrid.png"),
                footer(),
            )
        



# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
