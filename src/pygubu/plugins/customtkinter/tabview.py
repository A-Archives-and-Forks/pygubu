from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
    register_custom_property,
)
from ._config import _designer_tabs, nsctk, GCONTAINER
from .ctkbase import CTkBaseMixin

from customtkinter import CTkTabview


class CTkTabviewBO(CTkBaseMixin, BuilderObject):
    class_ = CTkTabview
    allow_bindings = False
    container = True
    properties = (
        "width",
        "height",
        "corner_radius",
        "border_width",
        "bg_color",
        "fg_color",
        "border_color",
        "segmented_button_fg_color",
        "segmented_button_selected_color",
        "segmented_button_selected_hover_color",
        "segmented_button_unselected_color",
        "segmented_button_unselected_hover_color",
        "text_color",
        "text_color_disabled",
        "command",
        "anchor",
        "state",
    )
    command_properties = ("command",)


register_widget(
    nsctk.CTkTabview,
    CTkTabviewBO,
    "CTkTabview",
    _designer_tabs,
    group=GCONTAINER,
)


class CTkTabviewTabBO(BuilderObject):
    class_ = None
    container = True
    container_layout = True
    layout_required = False
    allow_bindings = False
    allowed_parents = (nsctk.CTkTabview,)
    properties = ("label",)

    def _get_tab_name(self):
        return self.wmeta.properties.get("label", self.wmeta.identifier)

    def realize(self, parent, extra_init_args: dict = None):
        view = parent.get_child_master()
        self.widget = view.add(self._get_tab_name())
        return self.widget

    def configure(self, target=None):
        pass

    #
    # Code generation methods
    #
    def code_realize(self, boparent, code_identifier=None):
        view = boparent.code_child_master()
        tabid = self.code_identifier()
        tab_name = self._get_tab_name()
        lines = [f'{tabid} = {view}.add("{tab_name}")']
        return lines

    def code_configure(self, targetid=None):
        return tuple()


CTkTabviewBO.add_allowed_child(nsctk.CTkTabviewTab)
register_widget(
    nsctk.CTkTabviewTab,
    CTkTabviewTabBO,
    "CTkTabview.Tab",
    _designer_tabs,
    group=GCONTAINER,
)

# I'm renaming Tab UID from
# customtkinter.CTkTabview.Tab to customtkinter.CTkTabviewTab
# so, maintain backward compatibility:

CTkTabviewBO.add_allowed_child(nsctk.OldCTkTabview.Tab)
register_widget(
    nsctk.OldCTkTabview.Tab,
    CTkTabviewTabBO,
    "CTkTabview.Tab",
    _designer_tabs,
    group=GCONTAINER,
    public=False,
)
