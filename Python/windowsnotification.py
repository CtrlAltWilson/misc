"""
Send Windows Notifications
"""

from plyer import notification
import os

# Notification title and message
app_name = os.path.basename(__file__)
title = "My Notification"
message = "This is a Windows notification sent using Python."

# Send the notification
notification.notify(
    title=title,
    message=message,
    app_name=app_name,  # Optional, set the application name
    timeout=10  # Optional, set the duration the notification is displayed in seconds
)
