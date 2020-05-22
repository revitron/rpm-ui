import revitron
from revitron import _ 
from pyrevit import script

transaction = revitron.Transaction()
_(revitron.DOC.ProjectInformation).set('Extensions', '', 'MultilineText')
transaction.commit()
