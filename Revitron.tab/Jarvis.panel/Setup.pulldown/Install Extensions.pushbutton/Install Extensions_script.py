# -*- coding: utf-8 -*-
import revitron
import jarvis
import os
import glob
from revitron import _

if not revitron.Document.isFamily():

    extManager = jarvis.ExtensionsManager()
    extManager.removeAll()

    info = _(revitron.DOC.ProjectInformation)
    lines = info.get('Jarvis Extensions').split('\r\n')
     
    for line in lines:
        
        items = line.split('\t')
        
        try:
            extType = items[0].strip()
            extRepo = items[1].strip()
            extName = os.path.basename(extRepo).replace('.git', '')
            print('Installing {}'.format(extName))
            extManager.install(extName, extRepo, extType)
        except:
            pass
        
    # Call pyRevit reload command to reload pyRevit
    # The reason to call the command instead of using sessionmgr module
    # to realod is that the repo has been just updatedm so all
    # modules need to be re-imported again in a clean engine.
    from pyrevit.loader.sessionmgr import execute_command
    execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')
