# tests/test_bot_flow.py
import re

def test_start_prompts_for_amount_and_sets_next_handler(bot_mod):
    m = bot_mod
    # Вызов /start
    m.mod.start(m.make_msg("/start"))

    # Было отправлено хотя бы одно сообщение
    assert m.sent, "Ожидалось приглашение ввести сумму"
    # Зарегистрирован следующий шаг -> ввод суммы
    assert m.next_handlers, "Ожидалась регистрация next_step_handler после /start"
    assert m.next_handlers[-1].__name__ in {"get_Deposit_Amount", "get_deposit_amount"}

def test_amount_then_rate_happy_path(bot_mod):
    m = bot_mod

    # Шаг 1: сумма
    m.mod.get_Deposit_Amount(m.make_msg("100000"))
    assert m.next_handlers, "После суммы должен быть зарегистрирован обработчик ставки"
    assert m.next_handlers[-1].__name__ in {"get_Deposit_Percent", "get_deposit_percent"}

    # Проверим, что пользователю что-то подсказали про ставку
    # (не завязываемся на точный текст)
    assert any("ставк" in (txt.lower() or "") for _, txt, _ in m.sent), \
        "Ожидалась подсказка про ввод процентной ставки"

    # Шаг 2: ставка
    m.sent.clear()
    m.mod.get_Deposit_Percent(m.make_msg("12"))

    # Должен быть выслан «итог» с числами (проверим, что в тексте есть цифры)
    assert m.sent, "Ожидалось итоговое сообщение с расчётами"
    final_text = " ".join(txt for _, txt, _ in m.sent if isinstance(txt, str))
    assert re.search(r"\d", final_text), "Итоговое сообщение должно содержать числа"

def test_invalid_amount_is_reasked(bot_mod):
    m = bot_mod
    m.sent.clear()
    m.next_handlers.clear()

    # Невалидная сумма
    m.mod.get_Deposit_Amount(m.make_msg("abc"))

    # Ожидаем, что бот попросит повторить ввод суммы
    # (проверяем по цепочке — next handler снова get_Deposit_Amount)
    assert m.next_handlers, "После невалидной суммы должен быть следующий шаг"
    assert m.next_handlers[-1].__name__ in {"get_Deposit_Amount", "get_deposit_amount"}
    # И было отправлено хотя бы одно сообщение об ошибке/повторном вводе
    assert m.sent, "Ожидалось сообщение о повторном вводе суммы"
