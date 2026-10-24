"""Small shared HTTP helper with sane defaults and graceful failure."""

from __future__ import annotations

from typing import Optional

import requests

from .. import config


_session: Optional[requests.Session] = None


def get_session() -> requests.Session:
    global _session
    if _session is None:
        s = requests.Session()
        s.headers.update({"User-Agent": config.USER_AGENT})
        _session = s
    return _session


def get(url: str, **kwargs) -> Optional[requests.Response]:
    """GET a URL, returning None on any error instead of raising.

    Keeping the pipeline resilient matters more than any single feed; a dead
    source should never take down the whole digest.
    """
    try:
        resp = get_session().get(url, timeout=config.HTTP_TIMEOUT, **kwargs)
        resp.raise_for_status()
        return resp
    except requests.RequestException as exc:
        print(f"  [warn] fetch failed for {url}: {exc}")
        return None
