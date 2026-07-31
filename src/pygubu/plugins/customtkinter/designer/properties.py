import customtkinter as ctk
from pygubu.i18n import _
from pygubu.api.v1 import register_custom_property
from .._config import namespace, nsctk

_builder_all = f"{namespace}.*"

_maxsize_help = _("Set the maximum window size.")
_minsize_help = _("Set the minimum window size.")
_tabview_tab_label_help = _(
    "The 'name' argument of method: CTkTabview.add(self, name: str)"
)
_ctk_values_help = _(
    "Specifies the list of values to display. "
    "In code you can pass any iterable. "
    'In Designer, a json like list: ["item1", "item2"]'
)
_ctk_bg_color_help = _("Color behind the widget if it has rounded corners.")
_ctk_fg_color_help = _("Main color of the widget.")

int_editor = dict(editor="naturalnumber")
boolean_editor = dict(
    editor="choice",
    values=("", "True", "False"),
    state="readonly",
)
font_editor = dict(editor="fontentry")
color_editor = dict(editor="colorentry")

plugin_properties = dict(
    # BEGIN INT
    # pname=dict(buid=_builder_all, editor="naturalnumber"),
    border_width=dict(buid=_builder_all, **int_editor),
    border_spacing=dict(buid=_builder_all, **int_editor),
    button_corner_radius=dict(buid=_builder_all, **int_editor),
    button_length=dict(buid=_builder_all, **int_editor),
    corner_radius=dict(buid=_builder_all, **int_editor),
    height=dict(buid=_builder_all, **int_editor),
    from_=dict(buid=_builder_all, **int_editor),
    to=dict(buid=_builder_all, **int_editor),
    number_of_steps=dict(buid=_builder_all, **int_editor),
    width=dict(buid=_builder_all, **int_editor),
    checkbox_width=dict(buid=_builder_all, **int_editor),
    checkbox_height=dict(buid=_builder_all, **int_editor),
    radiobutton_width=dict(buid=_builder_all, **int_editor),
    radiobutton_height=dict(buid=_builder_all, **int_editor),
    border_width_unchecked=dict(buid=_builder_all, **int_editor),
    border_width_checked=dict(buid=_builder_all, **int_editor),
    switch_width=dict(buid=_builder_all, **int_editor),
    switch_height=dict(buid=_builder_all, **int_editor),
    minimum_pixel_length=dict(buid=_builder_all, **int_editor),
    determinate_speed=dict(buid=_builder_all, editor="realnumber"),
    indeterminate_speed=dict(buid=_builder_all, editor="realnumber"),
    # END INT
    # BEGIN BOOL
    # pname=dict(buid=_builder_all, **boolean_editor),
    dynamic_resizing=dict(buid=_builder_all, **boolean_editor),
    hover=dict(buid=_builder_all, **boolean_editor),
    activate_scrollbars=dict(buid=_builder_all, **boolean_editor),
    round_width_to_even_numbers=dict(buid=_builder_all, **boolean_editor),
    round_height_to_even_numbers=dict(buid=_builder_all, **boolean_editor),
    # END BOOL
    # BEGIN FONT
    # pname=dict(buid=_builder_all, **font_editor),
    font=dict(buid=_builder_all, **font_editor),
    dropdown_text_font=dict(buid=_builder_all, **font_editor),
    dropdown_font=dict(buid=_builder_all, **font_editor),
    label_font=dict(buid=_builder_all, **font_editor),
    # END FONT
    # BEGIN COLOR
    # pname=dict(buid=_builder_all, **color_editor),
    bg_color=dict(buid=_builder_all, help=_ctk_bg_color_help, **color_editor),
    border_color=dict(buid=_builder_all, **color_editor),
    button_color=dict(buid=_builder_all, **color_editor),
    button_hover_color=dict(buid=_builder_all, **color_editor),
    checkmark_color=dict(buid=_builder_all, **color_editor),
    dropdown_color=dict(buid=_builder_all, **color_editor),
    dropdown_hover_color=dict(buid=_builder_all, **color_editor),
    dropdown_text_color=dict(buid=_builder_all, **color_editor),
    dropdown_fg_color=dict(buid=_builder_all, **color_editor),
    fg_color=dict(buid=_builder_all, heop=_ctk_fg_color_help, **color_editor),
    hover_color=dict(buid=_builder_all, **color_editor),
    placeholder_text_color=dict(buid=_builder_all, **color_editor),
    progress_color=dict(buid=_builder_all, **color_editor),
    segmented_button_fg_color=dict(buid=_builder_all, **color_editor),
    segmented_button_selected_color=dict(buid=_builder_all, **color_editor),
    segmented_button_selected_hover_color=dict(
        buid=_builder_all, **color_editor
    ),
    segmented_button_unselected_color=dict(buid=_builder_all, **color_editor),
    segmented_button_unselected_hover_color=dict(
        buid=_builder_all, **color_editor
    ),
    text_color=dict(buid=_builder_all, **color_editor),
    text_color_disabled=dict(buid=_builder_all, **color_editor),
    scrollbar_button_color=dict(buid=_builder_all, **color_editor),
    scrollbar_button_hover_color=dict(buid=_builder_all, **color_editor),
    scrollbar_fg_color=dict(buid=_builder_all, **color_editor),
    background_corner_colors=dict(buid=_builder_all, **color_editor),
    label_fg_color=dict(buid=_builder_all, **color_editor),
    label_text_color=dict(buid=_builder_all, **color_editor),
    # END COLOR
    appearance_mode=dict(
        buid=_builder_all,
        editor="choice",
        values=("", "dark", "light"),
        state="readonly",
    ),
    color_theme=dict(
        buid=_builder_all,
        editor="choice",
        values=("", "blue", "green", "dark-blue", "sweetkind"),
        state="readonly",
        help=_("Default color theme."),
    ),
    command=[
        dict(buid=_builder_all, editor="simplecommandentry"),
        dict(buid=nsctk.CTkScrollbar, editor="scrollcommandentry"),
    ],
    label=dict(
        buid=[nsctk.CTkTabviewTab, nsctk.OldCTkTabview.Tab],
        editor="entry",
        help=_tabview_tab_label_help,
    ),
    label_text=dict(buid=_builder_all, editor="text"),
    label_anchor=dict(
        buid=nsctk.CTkScrollableFrame,
        editor="choice",
        values=(
            "",
            "n",
            "ne",
            "nw",
            "e",
            "w",
            "s",
            "se",
            "sw",
            "center",
        ),
        state="readonly",
    ),
    minsize=dict(
        buid=[nsctk.CTk, nsctk.CTkToplevel],
        editor="whentry",
        help=_minsize_help,
    ),
    maxsize=dict(
        buid=[nsctk.CTk, nsctk.CTkToplevel],
        editor="whentry",
        help=_maxsize_help,
    ),
    orientation=[
        dict(
            buid=_builder_all,
            editor="choice",
            values=("vertical", "horizontal"),
            default_value="horizontal",
            state="readonly",
        ),
        dict(
            buid=[nsctk.CTkScrollableFrame, nsctk.CTkScrollbar],
            editor="choice",
            values=("vertical", "horizontal"),
            default_value="vertical",
            state="readonly",
        ),
    ],
    placeholder_text=dict(buid=_builder_all, editor="entry"),
    state=[
        dict(
            buid=_builder_all,
            editor="choice",
            values=("", "normal", "active", "disabled"),
            state="readonly",
        ),
        dict(
            buid=[nsctk.CTkOptionMenu, nsctk.CTkComboBox],
            editor="choice",
            values=("", "normal", "disabled", "readonly"),
            state="readonly",
        ),
    ],
    text=dict(buid=_builder_all, editor="text"),
    values=[
        dict(buid=_builder_all, editor="entry"),
        dict(
            buid=[
                nsctk.CTkOptionMenu,
                nsctk.CTkComboBox,
                nsctk.CTkSegmentedButton,
            ],
            editor="json_entry",
            json_type=list,
            help=_ctk_values_help,
        ),
    ],
    variable=[
        dict(buid=_builder_all, editor="tkvarentry"),
        dict(
            buid=[nsctk.CTkProgressBar, nsctk.CTkSlider],
            editor="tkvarentry",
            type_choices=("int", "double"),
            type_default="int",
        ),
    ],
    wrap=dict(
        buid=nsctk.CTkTextbox,
        editor="choice",
        values=("", ctk.CHAR, ctk.WORD, ctk.NONE),
        state="readonly",
    ),
)

for prop in plugin_properties:
    definitions = plugin_properties[prop]
    if isinstance(definitions, dict):
        definitions = [definitions]
    for definition in definitions:
        builders = definition.pop("buid", _builder_all)
        if isinstance(builders, str):
            builders = [builders]
        editor = definition.pop("editor", "entry")
        for builder_uid in builders:
            register_custom_property(builder_uid, prop, editor, **definition)
