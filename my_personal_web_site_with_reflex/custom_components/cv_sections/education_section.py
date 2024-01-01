import reflex as rx
from typing import List
from my_personal_web_site_with_reflex.styles.styles import styles


def education_accordion(data:List[List[str]]=None) -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                rx.vstack(
                    # Study (Masters degree in Space Systems)
                    rx.hstack(
                        rx.text(f"{data[0]}", font_family = "Bookman", font_size = "1em", text_align = "left", text_color = "#2F4F4F", as_="b", width = "100%",),
                        rx.accordion_icon(),
                    ),  
                    # Date  (2014-2018)             
                    rx.text(f"{data[1]}", font_family = "Bookman", font_size = "0.7em", text_align = "left", text_color = "#2F4F4F", width = "100%",),
                    spacing="0.5em",
                )
            ),
            rx.accordion_panel(
                rx.text(f"{data[2]}", font_family = "Bookman", font_size = "1em", text_align = "left", text_color = "#2F4F4F", width = "100%",),
                bg="white" 
            )
        ),
        allow_multiple=True,
        width="100%",
        # bg="#FFF8DC", #Cornsilk   
        box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
    )

def education_section(dates:list[str], studies:list[str], places:list[str], icon_src:str, title:str= "EDUCATION") -> rx.Component:
    education_data: List[List[str]] = []
    for study, date, place in zip(studies, dates, places):
        education_data += [[study, date, place]]

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
            *[education_accordion(data) for data in education_data]
        ),
        style=styles["cv_section_style"],
    )