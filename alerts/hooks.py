# Alerts © 2022
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


from . import __version__ as app_version
from frappe import __version__ as frappe_version


app_name = "alerts"
app_title = "Alerts"
app_publisher = "Ameen Ahmed (Level Up)"
app_description = "Frappe module that displays custom alerts to specific recipients after login."
app_icon = "octicon octicon-bell"
app_color = "blue"
app_email = "kid1194@gmail.com"
app_license = "MIT"


is_frappe_above_v13 = int(frappe_version.split('.')[0]) > 13


app_include_js = [
    'alerts.bundle.js'
] if is_frappe_above_v13 else [
    '/assets/alerts/js/alerts.js'
]


after_install = "alerts.setup.install.after_install"


on_login = ["alerts.utils.access.on_login"]
on_logout = ["alerts.utils.access.on_logout"]


extend_bootinfo = "alerts.utils.boot.extend"