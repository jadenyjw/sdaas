##############################################################################
#
#    file                 : Makefile
#    created              : Sat Jan 28 09:53:03 EST 2017
#    copyright            : (C) 2002 Jaden
#
##############################################################################

ROBOT       = sdaas
MODULE      = ${ROBOT}.so
MODULEDIR   = drivers/${ROBOT}
SOURCES     = ${ROBOT}.cpp

SHIPDIR     = drivers/${ROBOT}
SHIP        = ${ROBOT}.xml acura-nsx-sz.rgb logo.rgb
SHIPSUBDIRS = 

PKGSUBDIRS  = ${SHIPSUBDIRS}
src-robots-sdaas_PKGFILES = $(shell find * -maxdepth 0 -type f -print)
src-robots-sdaas_PKGDIR   = ${PACKAGE}-${VERSION}/$(subst ${TORCS_BASE},,$(shell pwd))

include ${MAKE_DEFAULT}
