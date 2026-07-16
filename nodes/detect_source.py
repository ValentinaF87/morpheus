"""
Detect Source

Determina la sorgente della mail.

Output possibili:
- linkedin
- welcome_to_the_jungle
- fullremote
"""


def to_lower_string(value):
    """
    Converte un valore in stringa minuscola.

    Se il valore è None, restituisce una stringa vuota.
    """
    if value is None:
        return ""

    return str(value).lower()


# In n8n, i dati reali dell'item sono dentro _item["json"].
current = _item["json"].copy()

# Recuperiamo gli header.
# Se non esistono o valgono None, usiamo un dizionario vuoto.
headers = current.get("headers") or {}

# Mittente della mail.
sender = to_lower_string(
    current.get("sender")
    or current.get("from")
    or headers.get("from")
)

# Oggetto della mail.
subject = to_lower_string(
    current.get("subject")
    or headers.get("subject")
)

# Contenuto HTML.
html = to_lower_string(
    current.get("html")
    or current.get("textHtml")
)

# Contenuto testuale.
text = to_lower_string(
    current.get("text")
    or current.get("textPlain")
)

# Uniamo tutti i contenuti in una sola stringa ricercabile.
content = " ".join(
    [
        sender,
        subject,
        html,
        text,
    ]
)

source = None

# Welcome to the Jungle viene controllato per primo.
if (
    "welcome to the jungle" in content
    or "welcometothejungle" in content
    or "wttj.co" in content
):
    source = "welcome_to_the_jungle"

elif (
    "fullremote" in content
    or "fullremote.it" in content
):
    source = "fullremote"

elif (
    "linkedin" in content
    or "linkedin.com" in content
):
    source = "linkedin"

# Aggiungiamo i nuovi campi al JSON originale.
current["source"] = source

current["source_detection_debug"] = {
    "sender": sender,
    "subject": subject,
    "detected_source": source,
}

# n8n si aspetta un item con la chiave "json".
return {
    "json": current
}