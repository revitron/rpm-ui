# -*- coding: utf-8 -*-
import revitron
import System.Windows
from rpw.ui.forms import FlexForm, TextBox, Button, Label
from revitron import _

if not revitron.Document.isFamily():

    info = _(revitron.DOC.ProjectInformation)
    
    components = [
            Label('Enter one extension per line like this:'),   
            Label('"ui→https://repository.git" for UI extensions or "lib→https://repository.git" for libraries', Width=600),
            TextBox('extensions', Text=info.get('Extensions'), TextWrapping=System.Windows.TextWrapping.Wrap, AcceptsTab=True, AcceptsReturn=True, Multiline=True, Height=200, Width=600),
            Button('Save', Width=100, HorizontalAlignment=System.Windows.HorizontalAlignment.Right)
    ]
    
    form = FlexForm('Jarvis Extensions', components)
    form.show()
        
    if 'extensions' in form.values:
        extensions = form.values['extensions']
        transaction = revitron.Transaction()
        info.set('Jarvis Extensions', extensions , 'MultilineText')
        transaction.commit()
