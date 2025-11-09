import streamlit as st
import streamlit.components.v1 as components
import os
import base64

st.set_page_config(page_title="Daggerheart Story", page_icon="🗡️", layout="wide")

st.markdown(
    """
    <style>
    .title {
        font-family: 'Cinzel', serif;
        font-size: 48px;
        color: #a0522d;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px #000000;
    }
    .banner-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .banner-img {
        width: 33.33%;
        max-width: 500px;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Daggerheart Story</div>', unsafe_allow_html=True)

# Функция для конвертации изображения в base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

#изображение в base64
lith_img_base64 = ""
if os.path.exists("img/lith.jpg"):
    lith_img_base64 = f"data:image/jpeg;base64,{image_to_base64('img/lith.jpg')}"

characters = [
    {"name": "Скерек", "img": "https://via.placeholder.com/140x140.png?text=Скерек"},
    {"name": "Зора", "img": "https://via.placeholder.com/140x140.png?text=Зора"},
    {"name": "Трескун", "img": "https://via.placeholder.com/140x140.png?text=Трескун"},
    {"name": "Элара", "img": "https://via.placeholder.com/140x140.png?text=Элара"},
    {"name": "Литмуатар", "img": lith_img_base64},
    {"name": "Бард", "img": "https://via.placeholder.com/140x140.png?text=Бард"},
]

chars_html = """
<!DOCTYPE html>
<html>
<head>
<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    width: 100%;
    overflow: hidden;
}
.char-row {
    display: flex;
    flex-direction: row;
    gap: 30px;
    justify-content: center;
    align-items: flex-start;
    padding: 20px;
    flex-wrap: nowrap;
    width: 100%;
}
.char-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 140px;
    min-width: 140px;
    flex-shrink: 0;
}
.char-img {
    border-radius: 12px;
    width: 140px;
    height: 140px;
    object-fit: cover;
    border: 2px solid #8b5e3c;
    box-shadow: 3px 3px 8px #1a1515;
    background: #75604c;
    display: block;
}
.char-label {
    margin-top: 10px;
    font-size: 18px;
    color: #f0e6d2;
    font-family: 'Georgia', serif;
    text-align: center;
    width: 100%;
}
</style>
</head>
<body>
<div class="char-row">
"""

for char in characters:
    chars_html += f'''
    <div class="char-block">
        <img src="{char["img"]}" alt="{char["name"]}" class="char-img"/>
        <div class="char-label">{char["name"]}</div>
    </div>
    '''

chars_html += """
</div>
</body>
</html>
"""

components.html(chars_html, height=240)


if os.path.exists("img/Burachstandard.png"):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("img/Burachstandard.png", use_container_width=True)
else:
    st.info("img/Burachstandard.png не найден")
