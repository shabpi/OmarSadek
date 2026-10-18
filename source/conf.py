project = "Omar Sadek"
author = "Omar Sadek"
copyright = "2026, Omar Sadek"

extensions = ["sphinx_design"]

html_theme = "furo"
html_title = "Omar Sadek"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sphinx = False
html_copy_source = False

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-brand-primary": "#b0003a",
        "color-brand-content": "#b0003a",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ff5c8a",
        "color-brand-content": "#ff5c8a",
    },
}

exclude_patterns = ["_build", "README.md"]
