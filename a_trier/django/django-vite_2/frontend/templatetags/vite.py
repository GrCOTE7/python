import json
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def vite_asset(filename):
    if settings.DEBUG:
        return f"{settings.VITE_DEV_SERVER_URL}/{filename}"

    manifest_path = settings.BASE_DIR / "static" / "dist" / "manifest.json"
    try:
        with open(manifest_path, "r") as manifest_file:
            manifest = json.load(manifest_file)
    except:
        raise Exception(f"Vite manifest file not found at {manifest_path}")

    if filename not in manifest:
        raise Exception(f"File {filename} not found in Vite manifest")

    return f"/static/dist/{manifest[filename]['file']}"


@register.simple_tag
def vite_hmr_client():
    if settings.DEBUG:
        return mark_safe(
            f'<script type="module" src="{settings.VITE_DEV_SERVER_URL}/@vite/client"></script>'
        )
    return ""
