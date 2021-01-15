import os
import json
from cudatext import *
from cudax_lib import html_color_to_int

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_tab_colors.json')

colormap = {}
if os.path.isfile(fn_config):
    with open(fn_config, 'r') as f:
        colormap = json.load(f)


class Command:

    def on_open(self, ed_self):
        color_tab(ed_self)

    def on_lexer(self, ed_self):
        color_tab(ed_self)

    def config(self):

        if not os.path.isfile(fn_config):
            with open(fn_config, 'w') as f:
                f.write('{}\n')
        file_open(fn_config)


def color_tab(ed_self):
    filename = ed_self.get_filename()
    lexer = ed_self.get_prop(PROP_LEXER_FILE)
    val = None

    global colormap
    for key in colormap:
        if key[0] == '.':
            if filename.endswith(key):
                val = colormap[key]
                break
        elif key.lower() == lexer.lower():
            val = colormap[key]
            break

    if val is not None:
        try:
            n = html_color_to_int(val)
            ed_self.set_prop(PROP_TAB_COLOR, n)
        except:
            print('NOTE: Tab Colors: bad color string in config "%s"' % val)
            pass
