# -*- coding: utf-8 -*-

from resources.lib import kodiutils
from resources.lib import kodilogging
import io
import os
import sys
import time
import zipfile
import urllib
import logging
import xbmcaddon
import xbmcgui
import xbmc


ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))


class Canceled(Exception):
    pass


class MyProgressDialog():
    def __init__(self, process):
        self.dp = xbmcgui.DialogProgress()
        self.dp.create("Instalador Pack Ajustes", process, '', 'Espere...')

    def __call__(self, block_num, block_size, total_size):
        if self.dp.iscanceled():
            self.dp.close()
            raise Canceled
        percent = (block_num * block_size * 100) / total_size
        if percent < total_size:
            self.dp.update(percent)
        else:
            self.dp.close()


def read(response, progress_dialog):
    data = b""
    total_size = response.info().getheader('Content-Length').strip()
    total_size = int(total_size)
    bytes_so_far = 0
    chunk_size = 1024 * 1024
    reader = lambda: response.read(chunk_size)
    for index, chunk in enumerate(iter(reader, b"")):
        data += chunk
        progress_dialog(index, chunk_size, total_size)
    return data


def extract(zip_file, output_directory, progress_dialog):
    zin = zipfile.ZipFile(zip_file)
    files_number = len(zin.infolist())
    for index, item in enumerate(zin.infolist()):
        try:
            progress_dialog(index, 1, files_number)
        except Canceled:
            return False
        else:
            zin.extract(item, output_directory)
    return True


def stva():
    addon_name = ADDON.getAddonInfo('name')
    url = 'https://stvabuild.github.io/pack.zip'
    response = urllib.urlopen(url)
    try:
        data = read(response, MyProgressDialog("Descargando..."))
    except Canceled:
        message = "Descarga cancelada"
    else:
        addon_folder = xbmc.translatePath(os.path.join('special://', 'home'))
        if extract(io.BytesIO(data), addon_folder, MyProgressDialog("Extrayendo...")):
            message = "Instalación finalizada con éxito. "
        else:
            message = "Extraccion cancelada"
    dialog = xbmcgui.Dialog()
    dialog.ok(addon_name, "%s, Por favor, cierra la aplicación para completar el proceso" % message)
    os._exit(0)
