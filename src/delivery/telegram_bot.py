"""Minimal Telegram delivery (same pattern as macro-pulse-bot).

Only needs TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID (both free from @BotFather
and @userinfobot). If those aren't set, the caller is expected to skip Telegram
and rely on the markdown archive / console output instead.
"""

from __future__ import annotations

import os
from typing import List, Optional

import requests


class TelegramBot:
    """Thin wrapper over the Telegram Bot HTTP API."""

    BASE_URL = "https://api.telegram.org/bot{token}"

    def __init__(self, token: Optional[str] = None, chat_id: Optional[str] = None):
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID")
        if not self.token:
            raise ValueError("TELEGRAM_BOT_TOKEN not found")
        if not self.chat_id:
            raise ValueError("TELEGRAM_CHAT_ID not found")
        self.base_url = self.BASE_URL.format(token=self.token)

    @staticmethod
    def is_configured() -> bool:
        return bool(os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_CHAT_ID"))

    def send_message(
        self,
        text: str,
        parse_mode: str = "Markdown",
        disable_preview: bool = True,
    ) -> dict:
        data = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_preview,
        }
        try:
            resp = requests.post(f"{self.base_url}/sendMessage", json=data, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as exc:
            print(f"  [warn] Telegram send failed: {exc}")
            return {"ok": False, "error": str(exc)}

    def send_messages(self, messages: List[str], parse_mode: str = "Markdown") -> bool:
        ok = True
        for msg in messages:
            result = self.send_message(msg, parse_mode=parse_mode)
            if not result.get("ok"):
                ok = False
        return ok
