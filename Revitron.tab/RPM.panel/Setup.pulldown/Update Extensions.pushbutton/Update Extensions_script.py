import revitron
import rpm

if not revitron.Document().isFamily():
	
	rpm.Update.extensions()
	
	# Call pyRevit reload command to reload pyRevit
	# The reason to call the command instead of using sessionmgr module
	# to realod is that the repo has been just updatedm so all
	# modules need to be re-imported again in a clean engine.
	from pyrevit.loader.sessionmgr import execute_command
	execute_command('pyrevitcore-pyrevit-pyrevit-tools-reload')