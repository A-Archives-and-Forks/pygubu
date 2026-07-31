import os
import tkinter as tk
import customtkinter
from pathlib import Path
from pygubu.i18n import _
from pygubu.plugins.tk.tkstdwidgets import TKFrame as TKFrameBO
from pygubu.utils.font import tkfontstr_to_dict
from pygubu.stockimage import StockImage
from customtkinter.windows.widgets.core_widget_classes import CTkBaseClass
from customtkinter import CTkFont, CTkImage
from ._config import namespace, GCONTAINER, GDISPLAY, GINPUT
from PIL import Image, ImageTk


_use_fixed_image_class = False

if os.getenv("PYGUBU_DESIGNER_RUNNING"):
    _use_fixed_image_class = True

    class CTKImageFix(CTkImage):
        "Fix loader for pygubu designer toplevel preview"

        def __init__(
            self,
            light_image: "Image.Image" = None,
            dark_image: "Image.Image" = None,
            size=(20, 20),
            tk_master=None,
        ):
            super().__init__(light_image, dark_image, size)
            self._tk_master = tk_master

        def _get_scaled_light_photo_image(
            self, scaled_size
        ) -> "ImageTk.PhotoImage":
            if scaled_size in self._scaled_light_photo_images:
                return self._scaled_light_photo_images[scaled_size]
            else:
                self._scaled_light_photo_images[scaled_size] = (
                    ImageTk.PhotoImage(
                        self._light_image.resize(scaled_size),
                        master=self._tk_master,
                    )
                )
                return self._scaled_light_photo_images[scaled_size]

        def _get_scaled_dark_photo_image(
            self, scaled_size
        ) -> "ImageTk.PhotoImage":
            if scaled_size in self._scaled_dark_photo_images:
                return self._scaled_dark_photo_images[scaled_size]
            else:
                self._scaled_dark_photo_images[scaled_size] = (
                    ImageTk.PhotoImage(
                        self._dark_image.resize(scaled_size),
                        master=self._tk_master,
                    )
                )
                return self._scaled_dark_photo_images[scaled_size]


def ctk_image_loader(source_type, source, tk_master):
    if _use_fixed_image_class:
        return CTKImageFix(Image.open(source), tk_master=tk_master)
    return CTkImage(Image.open(source))


int_properties = {
    "border_width",
    "border_spacing",
    "button_corner_radius",
    "button_length",
    "corner_radius",
    "height",
    "from_",
    "to",
    "number_of_steps",
    "width",
    "checkbox_width",
    "checkbox_height",
    "radiobutton_width",
    "radiobutton_height",
    "border_width_unchecked",
    "border_width_checked",
    "switch_width",
    "switch_height",
    "minimum_pixel_length",
    "determinate_speed",
    "indeterminate_speed",
}

bool_properties = {
    "dynamic_resizing",
    "hover",
    "activate_scrollbars",
    "round_width_to_even_numbers",
    "round_height_to_even_numbers",
}

font_properties = {
    "font",
    "dropdown_text_font",
    "dropdown_font",
    "label_font",
}


class CTkBaseMixin:

    def _can_set_tcl_widget_name(self) -> bool:
        """Returns True if widget accepts the tcl "name" init argument."""
        return False

    def _process_property_value(self, pname, value):
        if pname in bool_properties:
            return tk.getboolean(value)
        if pname in int_properties:
            return float(value)
        if pname in font_properties:
            fdesc = tkfontstr_to_dict(value)
            _modifiers = (
                [] if fdesc["modifiers"] is None else fdesc["modifiers"]
            )
            family = fdesc["family"]
            size = None if fdesc["size"] is None else int(fdesc["size"])
            weight = "bold" if "bold" in _modifiers else None
            slant = "italic" if "italic" in _modifiers else "roman"
            underline = True if "underline" in _modifiers else False
            overstrike = True if "overstrike" in _modifiers else False
            _font = CTkFont(family, size, weight, slant, underline, overstrike)
            return _font
        if pname == "image":
            name = Path(value).name
            if not StockImage.is_registered(name):
                StockImage.find_and_register(name)
            img = StockImage.get(value, ctk_image_loader)
            return img
        return super()._process_property_value(pname, value)

    #
    # Code generation methods
    #

    def _code_process_property_value(self, targetid, pname, value: str):
        if (
            pname in int_properties
            or pname in bool_properties
            or pname in font_properties
        ):
            return super()._process_property_value(pname, value)
        return super()._code_process_property_value(targetid, pname, value)

    def _code_set_property(self, targetid, pname, value, code_bag):
        if pname in font_properties:
            fdesc = tkfontstr_to_dict(value)
            _modifiers = (
                [] if fdesc["modifiers"] is None else fdesc["modifiers"]
            )
            family = f'"{fdesc["family"]}"'
            size = None if fdesc["size"] is None else int(fdesc["size"])
            weight = '"bold"' if "bold" in _modifiers else None
            slant = '"italic"' if "italic" in _modifiers else '"roman"'
            underline = True if "underline" in _modifiers else False
            overstrike = True if "overstrike" in _modifiers else False

            fvalue = f"CTkFont({family}, {size}, {weight}, {slant}, {underline}, {overstrike})"
            code_bag[pname] = fvalue
        elif pname == "image":
            lines = [
                f'_img = Image.open("{value}")',
                f"{targetid}.configure(image=CTkImage(_img))",
            ]
            code_bag[pname] = lines
        else:
            super()._code_set_property(targetid, pname, value, code_bag)

    def code_imports(self):
        # Shoud return an iterable of (module, classname/function) to import
        # or None
        imports = [
            ("customtkinter", self.class_.__name__),
        ]
        extra_imports = self.code_extra_imports()
        imports.extend(extra_imports)
        return imports

    def code_extra_imports(self) -> list:
        """Return extra imports required."""
        extra_imports = []
        uses_ctk_font = False
        uses_ctk_image = False
        for pname in self.properties:
            if pname in self.wmeta.properties:
                if pname in font_properties:
                    uses_ctk_font = True
                if pname == "image":
                    uses_ctk_image = True
        if uses_ctk_font:
            extra_imports.append(("customtkinter", "CTkFont"))
        if uses_ctk_image:
            extra_imports.append(("customtkinter", "CTkImage"))
            extra_imports.append(("PIL", "Image"))
        return extra_imports
