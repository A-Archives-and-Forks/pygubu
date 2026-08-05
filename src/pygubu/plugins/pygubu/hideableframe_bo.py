from pygubu.api.v1 import register_widget
from pygubu.plugins.ttk.ttkstdwidgets import TTKFrame
from pygubu.widgets.hideableframe import HideableFrame
from ._config import nspygubu, _section_containers, GCONTAINER


class HideableFrameBO(TTKFrame):
    class_ = HideableFrame


register_widget(
    nspygubu.widgets.hideableframe,
    HideableFrameBO,
    "HideableFrame",
    _section_containers,
    group=GCONTAINER,
)
