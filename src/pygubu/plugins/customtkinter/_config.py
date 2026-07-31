from pygubu.utils.namespace import walkns, SN
from pygubu.i18n import _

_tab_label = _("CustomTkinter")
_designer_tabs = ("ttk", _tab_label)

# used for group ordering in designer.
GROOT: int = 100
GCONTAINER: int = 200
GDISPLAY: int = 300
GINPUT: int = 400

namespace = "customtkinter"

# Namespace configuration
ns_ctk = SN(
    _name=namespace,
    CTk=1,
    CTkToplevel=1,
    CTkFrame=1,
    CTkLabel=1,
    CTkProgressBar=1,
    CTkButton=1,
    CTkSlider=1,
    CTkEntry=1,
    CTkOptionMenu=1,
    CTkComboBox=1,
    CTkCheckBox=1,
    CTkRadioButton=1,
    CTkSwitch=1,
    CTkTextbox=1,
    CTkCanvas=1,
    CTkScrollbar=1,
    CTkScrollableFrame=1,
    CTkSegmentedButton=1,
    CTkTabview=1,
    CTkTabviewTab=1,
    OldCTkTabview=SN(_name="CTkTabview", Tab=1),
)

# Namespace walker
nsctk = walkns(ns_ctk)
