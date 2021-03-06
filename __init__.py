# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QgisServerChecker
                                 A QGIS plugin
 QGIS Server Checker
                             -------------------
        begin                : 2015-12-16
        copyright            : (C) 2015 by 3Liz
        email                : info@3Liz.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QgisServerChecker class from file QgisServerChecker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_server_checker import QgisServerChecker
    return QgisServerChecker(iface)
