"""URL slugs."""
from __future__ import annotations

import re
import unicodedata
from typing import Container

__all__ = ["slugify", "unique_slug"]

_SPECIAL = {"ß": "ss", "æ": "ae", "Æ": "AE", "ø": "o", "Ø": "O", "œ": "oe", "Œ": "OE", "đ": "d", "Đ": "D", "ł": "l", "Ł": "L"}


def slugify(text: str, separator: str = "-", max_length: int = 0) -> str:
    text = "".join(_SPECIAL.get(c, c) for c in text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", separator, text.lower()).strip(separator)
    if max_length and len(text) > max_length:
        text = text[:max_length]
        cut = text.rfind(separator)
        text = (text[:cut] if cut > 0 else text).strip(separator)
    return text


def unique_slug(base: str, taken: Container[str], separator: str = "-") -> str:
    if base not in taken:
        return base
    n = 2
    while f"{base}{separator}{n}" in taken:
        n += 1
    return f"{base}{separator}{n}"
