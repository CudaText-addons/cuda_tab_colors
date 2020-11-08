import os
import json
from cudatext import *
from cudax_lib import html_color_to_int

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_tab_colors.json')

colormap = {}
if os.path.isfile(fn_config):
    with open(fn_config, 'r') as f:
        colormap = json.load(f)
print('colormap', colormap)

class Command:

    def on_open(self, ed_self):

        global colormap
        filename = ed_self.get_filename()
        lexer = ed_self.get_prop(PROP_LEXER_FILE)

        val = None

        for key in colormap:
            if key[0] == '.' and filename.endswith(key):
                val = colormap[key]
                break
            elif key == lexer:
                val = colormap[key]
                break

        if val is not None:
            ed_self.set_prop(PROP_TAB_COLOR, html_color_to_int(val))

    def config(self):

        if not os.path.isfile(fn_config):
            with open(fn_config, 'w') as f:
                f.write('{}\n')
        file_open(fn_config)
