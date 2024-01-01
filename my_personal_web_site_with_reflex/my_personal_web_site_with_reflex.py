"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from my_personal_web_site_with_reflex.custom_components.navbar import navbar
from my_personal_web_site_with_reflex.views.header import header
from my_personal_web_site_with_reflex.views.footer import footer
from my_personal_web_site_with_reflex.custom_components.cv_sections.base_section import base_section
from my_personal_web_site_with_reflex.custom_components.cv_sections.education_section import education_section
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
                education_section(dates= ["2018-2021", "2014-2018", "2012-2014"], 
                                  studies=["Masters Degree in Space Systems", "Bachelors Degree in Aerospace Engineering", "High School"],
                                  places=["TECHNICAL UNIVERSITY OF MADRID", "TECHNICAL UNIVERSITY OF MADRID", "J.H. NEWMAN"],
                                  icon_src="/icons/book-open-reader-solid.svg"
                                  ),
                rx.spacer(),
                footer(),
                spacing = "1em"
            )
        



# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
