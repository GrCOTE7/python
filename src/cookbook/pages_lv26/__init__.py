from .page_root import build_root_view
from .page_settings import build_settings_view
from .page_mail_settings import build_mail_settings_view
from .template import build_lv26_et_plus_view


def get_page_builders(lesson: int = 26):
    def _build_root_view(open_setting):
        return build_root_view(open_setting, lesson=lesson)

    def _build_settings_view(open_mail_setting):
        return build_settings_view(open_mail_setting, lesson=lesson)

    def _build_mail_settings_view():
        return build_mail_settings_view(lesson=lesson)

    return _build_root_view, _build_settings_view, _build_mail_settings_view


__all__ = [
    "build_root_view",
    "build_settings_view",
    "build_mail_settings_view",
    "build_lv26_et_plus_view",
    "get_page_builders",
]
