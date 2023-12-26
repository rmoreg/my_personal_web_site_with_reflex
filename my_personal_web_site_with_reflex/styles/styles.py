shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"

styles = dict()
navbar_style = dict(padding="2em",
                    box_shadow=shadow,
                    position="sticky",
                    width="100%",
                    max_height = "5em",
                    top="0px",
                    z_index="999",
                    bg = "#FFF5EE"
                    )

styles["navbar_style"] = navbar_style

header_box_style_1 = dict(
    # padding="1em",
    # border_radius="5px",
    margin_y="0.5em",
    #box_shadow=shadow,
    max_width="30em",
    #display="inline-block",
    #bg="#F8F8FF",
    font_size="2em", 
    text_align="center",
    font_family = "Impact",
    text_color = "#191970"
)

styles["header_box_style_1"] = header_box_style_1

# CV SECTIONS
cv_section_style = dict(
    padding="1em",
    box_shadow=shadow,
    width="95%",
    #max_height = "5em",
    bg = "#FDF5E6", # OldLace
    # text_align = "left",
    margin_y = "20em",
)
cv_title_style = dict(
    font_family = "Georgia",
    font_size = "1.2em",
    # text_align = "left",
    text_color = "#191970", #MidnightBlue
    text_decoration = "underline",
    width = "100%",
    # as_ = "u",
)
cv_body_style = dict(
    font_family = "Bookman",
    font_size = "0.9em",
    # text_align = "left",
    text_color = "#2F4F4F", #DarkSlateGray
    width = "100%",
)

styles["cv_section_style"] = cv_section_style
styles["cv_title_style"] = cv_title_style
styles["cv_body_style"] = cv_body_style



