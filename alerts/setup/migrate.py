# Expenses © 2024
# Author:  Ameen Ahmed
# Company: Level Up Marketing & Software Development Services
# Licence: Please refer to LICENSE file


# [Hooks]
def after_migrate():
    from frappe.utils import now
    
    from alerts import __version__
    
    from alerts.utils.settings import settings
    
    doc = settings()
    if doc.current_version != __version__:
        
        if doc.update_notification_receivers:
            for v in doc.update_notification_receivers:
                if v.user == doc.update_notification_sender:
                    doc.update_notification_receivers.remove(v)
        
        doc.current_version = __version__
        doc.latest_version = __version__
        doc.latest_check = now()
        doc.has_update = 0
        
        doc.save(ignore_permissions=True)