from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
    register_custom_property,
)
from pygubu.i18n import _
from ._config import _designer_tabs, nsctk, GCONTAINER
from .ctkbase import CTkBaseMixin

from customtkinter import CTkScrollableFrame


class CTkScrollableFrameBO(CTkBaseMixin, BuilderObject):
    class_ = CTkScrollableFrame
    container = True
    # CTkScrollableFrame does some weird things
    # with layout so I disable container layout here on purpose.
    container_layout = False
    properties = (
        "width",
        "height",
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "border_color",
        "scrollbar_fg_color",
        "scrollbar_button_color",
        "scrollbar_button_hover_color",
        "label_fg_color",
        "label_text_color",
        "label_text",
        "label_font",
        "label_anchor",
        "orientation",
    )
    ro_properties = ("orientation",)


register_widget(
    nsctk.CTkScrollableFrame,
    CTkScrollableFrameBO,
    "CTkScrollableFrame",
    _designer_tabs,
    group=GCONTAINER,
)
