import os
import sys
from pyrevit import script
from pyrevit import output
from pyrevit.loader import sessionmgr

pwd = os.path.dirname(__file__)
sys.path.append('{}\\..\\jarvis-core.lib'.format(pwd))

import jarvis

out = script.get_output()
js = jarvis.system
fileTempUpdated = 'C:\\temp\\jarvis.update'

output.set_stylesheet(pwd + '\\outputstyles.css')

if os.path.isfile(fileTempUpdated):
    os.remove(fileTempUpdated)
else:
    open(fileTempUpdated, 'a').close()
    out.set_height(800)
    out.set_width(1000)
    out.print_image('{}/svg/jarvis-light.svg'.format(js.constants.JRVS_DIR))
    out.center()
    js.Update.jarvis(js.constants.JRVS_DIR)
    js.Update.extensions(js.constants.JRVS_EXTENSIONS_DIR)
    out.print_html('<br>')
    out.print_html('<em>Starting session ...</em>')
    sessionmgr.load_session()