Plugin for CudaText.
Allows to colorize ui-tabs headers: per lexer, and per file extension.
Plugin has config file in JSON format, to open it, call
"Options / Settings-plugins / Tab Colors / Config" menu item.
Config has pairs "key":"value".

- "key": Lexer name, or just file extension with leading dot (it can be double extension too).
  Lexer name is compared case-insensitive here.
- "value": String with HTML color like "#rrggbb" or "#rgb".
  In the case of bad color string, plugin prints error to Console panel.

Authors:
  Alexey (CudaText)
  Shovel (CudaText forum user)
License: MIT
