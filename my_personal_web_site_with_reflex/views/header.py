import reflex as rx
from my_personal_web_site_with_reflex.styles.styles import styles

def header() -> rx.Component:
    # return rx.box(
    #         rx.vstack(
    #             rx.text(
    #                 "Welcome to my personal web site", 
    #                 style=styles["header_box_style_1"]
    #                 ), 
    #             rx.text(
    #                 "In this page you will find usefull information about my personal profiles, carrer, personal interests, etc.", 
    #                 font_size="0.8em", 
    #                 text_align = "center"
    #                 ),  
    #             ),
    #             spacing="10em",
    #         )

    return rx.vstack(
        rx.box(
            rx.text(
                "Welcome to my personal web site", 
                style=styles["header_box_style_1"]
                ),
        ),
        rx.box(
            rx.text(
                "In this page you will find useful information about my personal profiles, carrer, personal interests, etc.", 
                font_size="0.8em", 
                text_align = "center"
                ),
        ),
        spacing="1px",
    )
                  
            
    


    


