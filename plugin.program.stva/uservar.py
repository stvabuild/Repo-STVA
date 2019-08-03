import os, xbmc, xbmcaddon

#########################################################
### Global Variables ####################################
#########################################################
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'STVA [COLOR orange][B]WIZARD[/B][/COLOR]'
BUILDERNAME    = 'WHIZ'
EXCLUDES       = [ADDON_ID, 'plugin.program.stva', 'plugin.video.balandro']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it.
BUILDFILE      = 'https://stva.zriel.ga/wizard/txt/autobuilds.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'https://stva.zriel.ga/wizard/txt/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = ''
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://stva.zriel.ga/wizard/txt/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://stva.zriel.ga/wizard/txt/Advanced.txt'
#########################################################

#########################################################
### Theming Menu Items ##################################
#########################################################

ICONBUILDS     = 'https://stva.zriel.ga/wizard/imagenes/builds.png'
ICONMAINT      = 'https://stva.zriel.ga/wizard/imagenes/mantenimiento.png'
ICONAPK        = 'https://stva.zriel.ga/wizard/imagenes/apk.png'
ICONADDONS     = 'https://stva.zriel.ga/wizard/imagenes/i-addons.png'
ICONYOUTUBE    = 'https://stva.zriel.ga/wizard/imagenes/youtube.png'
ICONSAVE       = 'https://stva.zriel.ga/wizard/imagenes/data.png'
ICONCONTACT    = 'https://stva.zriel.ga/wizard/imagenes/contacto.png'
ICONSETTINGS   = 'https://stva.zriel.ga/wizard/imagenes/ajustes.png'
ICONSPEED      = 'https://stva.zriel.ga/wizard/imagenes/test.png'
ICONTRAKT      = 'https://stva.zriel.ga/wizard/imagenes/trakt.png'
ICONREAL       = 'https://stva.zriel.ga/wizard/imagenes/real.png'
ICONLOGIN      = 'https://stva.zriel.ga/wizard/imagenes/login.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'darkorange'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][COLOR '+COLOR2+'][/COLOR][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Version STVA Instalada:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME6         = '[COLOR '+COLOR1+']Version STVA a instalar:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Gracias por utilizar STVA Build\r\n\r\nSi quieres ponerte en contacto utiliza el formulario de la web www.stva.ml'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://stva.zriel.ga/wizard/imagenes/qrstva.jpg'
CONTACTFANART  = 'https://stva.zriel.ga/wizard/imagenes/cfanart.jpg'
#########################################################

#########################################################
### Auto Update                   #######################
###        For Those With No Repo #######################
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://stva.zriel.ga/wizard/txt/autobuilds.txt'
#########################################################

#########################################################
### Auto Install                 ########################
###        Repo If Not Installed ########################
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.repostva'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/stvabuild/Repo-STVA/master/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/stvabuild/Repo-STVA/master/repository.repostva/'
#########################################################

#########################################################
### Notification Window #################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://stva.zriel.ga/wizard/txt/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = 'STVA WIZARD'
# url to image if using Image 424x180
HEADERIMAGE    = 'http://'
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'https://stva.zriel.ga/wizard/imagenes/cfanart.jpg'
#########################################################
