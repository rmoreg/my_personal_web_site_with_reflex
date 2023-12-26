"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from my_personal_web_site_with_reflex.custom_components.navbar import navbar
from my_personal_web_site_with_reflex.views.header import header
from my_personal_web_site_with_reflex.views.footer import footer
from my_personal_web_site_with_reflex.custom_components.cv_sections.base_section import base_section
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    personal_profile_body = """
        Aerospace engineer specialized in space systems 
        with +2 years of professional experience in software development 
        using Python and C++ for structural analysis. 
        Proficient in continuous improvement, teamwork and problem solving.
    """

    return  rx.vstack(
                navbar(),
                header(),
                rx.image(src="skyline_madrid.png"),
                base_section("PERSONAL PROFILE", personal_profile_body, "/icons/user-regular.svg"),
                footer(),
                spacing = "3em"
            )
        



# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
