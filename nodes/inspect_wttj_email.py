"""
Inspect WTTJ Email

Estrae i campi principali della mail:
- subject
- sender
- text
- html
"""

current = _item["json"]
headers = current.get("headers") or {}

return {
    "json": {
        "subject": (
            current.get("subject")
            or headers.get("subject")
            or None
        ),
        "sender": (
            current.get("from")
            or current.get("sender")
            or headers.get("from")
            or None
        ),
        "text": (
            current.get("text")
            or current.get("textPlain")
            or None
        ),
        "html": (
            current.get("html")
            or current.get("textHtml")
            or None
        ),
    }
}