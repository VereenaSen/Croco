"""Прыг-Крок — браузерная игра, встроенная в Streamlit.

Сама игра написана на HTML5 Canvas + JavaScript (static/game.html)
и работает целиком в браузере игрока. Streamlit отдаёт страницу
и встраивает игру через HTML-компонент.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

GAME_FILE = Path(__file__).parent / "static" / "game.html"
GAME_HEIGHT = 600  # высота окна игры в пикселях (на телефоне включает панель кнопок)

st.set_page_config(
    page_title="Прыг-Крок",
    page_icon="🐊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Убираем лишние отступы Streamlit, чтобы игра занимала больше места,
# особенно на узких экранах телефонов
st.markdown(
    """
    <style>
      .block-container { padding-top: 1.2rem; padding-bottom: 1rem; }
      iframe { border-radius: 14px; display: block; }
      @media (max-width: 640px) {
        .block-container { padding-left: 0.5rem; padding-right: 0.5rem; padding-top: 0.6rem; }
        h1 { font-size: 1.6rem !important; }
        iframe { border-radius: 10px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🐊 Прыг-Крок")
st.caption(
    "Компьютер: кликни по игре, затем ← → — бег, Пробел / ↑ — прыжок. "
    "Телефон: кнопки под игрой или тап по экрану. В горизонтальной ориентации видно больше уровня."
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
