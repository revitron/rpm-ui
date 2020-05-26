# -*- coding: utf-8 -*-
import revitron
import jarvis
import subprocess
import os
from revitron import _

if not revitron.Document.isFamily():

    info = _(revitron.DOC.ProjectInformation)
    lines = info.get('Extensions').split('\r\n')
             
    for line in lines:
        
        items = line.split('\t')
        
        try:
            extType = items[0].strip()
            extRepo = items[1].strip()
            extName = os.path.basename(extRepo).replace('.git', '')
            cmd = '{} extend {} {} {} --dest="{}"'.format(jarvis.JRVS_PYREVIT_BIN, extType, extName, extRepo, jarvis.JRVS_EXTENSIONS_DIR)
            print('Installing {} "{}" from {} ...'.format(extType, extName, extRepo))
        except:
            pass
        
        
        
