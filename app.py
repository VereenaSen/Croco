"""Прыг-Крок — браузерная игра, встроенная в Streamlit.

Сама игра написана на HTML5 Canvas + JavaScript (static/game.html)
и работает целиком в браузере игрока. Streamlit отдаёт страницу
и встраивает игру через HTML-компонент.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

GAME_FILE = Path(__file__).parent / "static" / "game.html"
GAME_HEIGHT = 560  # высота окна игры в пикселях

st.set_page_config(page_title="Прыг-Крок", page_icon="🐊", layout="wide")

# Убираем лишние отступы Streamlit, чтобы игра занимала больше места
st.markdown(
    """
    <style>
      .block-container { padding-top: 1.5rem; padding-bottom: 1rem; }
      iframe { border-radius: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🐊 Прыг-Крок")
st.caption(
    "Кликни по игре, чтобы она получила фокус клавиатуры. "
    "← → — бег, Пробел / ↑ — прыжок. На телефоне — экранные кнопки."
)


@st.cache_data
def load_game() -> str:
    return GAME_FILE.read_text(encoding="utf-8")


components.html(load_game(), height=GAME_HEIGHT, scrolling=False)

with st.expander("Как считаются очки"):
    st.markdown(
        """
| Штучка | Базовые очки |
|---|---|
| 🪰 Муха | 5 |
| 🫐 Ягода | 10 |
| 🪙 Монета | 20 |
| 💎 Кристалл | 40 |

Базовые очки умножаются на высоту блока (×1 … ×5, множитель написан на блоке).
Упал в болото — игра окончена, жми «Начать заново».
"""
    )
