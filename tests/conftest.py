# tests/conftest.py
import re
from types import ModuleType, SimpleNamespace
from pathlib import Path
import pytest

BOT_FILE = Path(__file__).resolve().parent.parent / "Percents_Per_Day_Bank.py"

def load_bot_module():
    """
    Загружает исходник бота как модуль, устраняя любые вечные циклы polling.
    Исходный файл НЕ меняется на диске.
    """
    src = BOT_FILE.read_text(encoding="utf-8")

    # 1) На всякий случай выключим бесконечные циклы
    src = src.replace("while True:", "if False:")

    # 2) И глушим любые прямые вызовы polling/infinity_polling
    src = re.sub(r"bot\.infinity_polling\([^)]*\)", "pass  # patched in tests", src)
    src = re.sub(r"bot\.polling\([^)]*\)", "pass  # patched in tests", src)

    mod = ModuleType("ppd_bank_bot_under_test")
    code = compile(src, str(BOT_FILE), "exec")
    exec(code, mod.__dict__)
    return mod

@pytest.fixture(scope="function")
def bot_mod(monkeypatch):
    """
    Возвращает загруженный модуль с замоканными методами бота.
    """
    mod = load_bot_module()

    sent_messages = []
    next_handlers = []

    # Простейшая заглушка get_me()
    monkeypatch.setattr(mod.bot, "get_me", lambda: {"username": "test_bot"})

    # Заглушки отправки сообщений
    def fake_send_message(chat_id, text, **kwargs):
        sent_messages.append((chat_id, text, kwargs))

    # Иногда в коде могут вызывать reply_to — обрабатываем одинаково
    def fake_reply_to(message, text, **kwargs):
        chat_id = getattr(getattr(message, "chat", None), "id", None)
        sent_messages.append((chat_id, text, kwargs))

    monkeypatch.setattr(mod.bot, "send_message", fake_send_message)
    if hasattr(mod.bot, "reply_to"):
        monkeypatch.setattr(mod.bot, "reply_to", fake_reply_to)

    # Регистрируем «следующий шаг» — просто запоминаем функцию
    def fake_register_next_step_handler(message, func):
        next_handlers.append(func)

    monkeypatch.setattr(mod.bot, "register_next_step_handler", fake_register_next_step_handler)

    # Утилита для создания «сообщения» (достаточно нужных полей)
    def make_msg(text, user_id=12345):
        return SimpleNamespace(
            text=text,
            from_user=SimpleNamespace(id=user_id),
            chat=SimpleNamespace(id=user_id),
        )

    return SimpleNamespace(
        mod=mod,
        sent=sent_messages,
        next_handlers=next_handlers,
        make_msg=make_msg
    )
