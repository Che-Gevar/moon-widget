import json
from datetime import datetime
from zoneinfo import ZoneInfo

today = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%Y-%m-%d")

forecast = {
    "2026-10-09": {
        "date": "9 октября",
        "title": "ДОГОВАРИВАЙСЯ",
        "widget_text": "☾ ДОГОВАРИВАЙСЯ\nУтром — хвосты. После обеда — люди.\n₽ Фиксируй, не форсируй.\n♡ Не руби с плеча."
    },

    "2026-10-10": {
        "date": "10 октября",
        "title": "ЗАДАЙ ВЕКТОР",
        "widget_text": "☾ ЗАДАЙ ВЕКТОР\nДо вечера — заверши старое.\nПосле 18:50 — сформулируй новое.\n₽ Не форсируй.\n♡ Ищи баланс."
    }
}

data = forecast.get(today, {
    "date": today,
    "title": "НАБЛЮДАЙ",
    "widget_text": "☾ НАБЛЮДАЙ\nНа этот день прогноз пока не задан."
})

with open("today.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)