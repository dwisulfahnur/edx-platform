"""
Message types used for ACE communication by the course_duration_limits app.
"""
import logging

from openedx.core.djangoapps.ace_common.message import BaseMessageType
from openedx.core.djangoapps.schedules.config import DEBUG_MESSAGE_WAFFLE_FLAG


class ExpiryReminder(BaseMessageType):
    def __init__(self, *args, **kwargs):
        super(ExpiryReminder, self).__init__(*args, **kwargs)
        self.log_level = logging.DEBUG if DEBUG_MESSAGE_WAFFLE_FLAG.is_enabled() else None
