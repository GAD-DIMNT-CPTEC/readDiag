#-----------------------------------------------------------------------------#
#           Group on Data Assimilation Development - GDAD/CPTEC/INPE          #
#-----------------------------------------------------------------------------#
#BOP
#
# !SCRIPT:
#
# !DESCRIPTION:
#
# !CALLING SEQUENCE:
#
# !REVISION HISTORY: 
# 13 Apr 2018 - J. G. de Mattos - Initial Version
#
# !REMARKS:
#
#EOP
#-----------------------------------------------------------------------------#
#BOC
"""
This package defines some functions to read and plot gsi diagnostic files.\
For help please use help() function.
"""
from .__main__ import (help,read_diag, getColor)
from .datasources import getVarInfo

__name__    = 'gsiDiag'
__version__ = '2.0'


#EOC
#-----------------------------------------------------------------------------#

