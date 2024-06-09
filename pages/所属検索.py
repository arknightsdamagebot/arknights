import streamlit as st
import pandas as pd
import random
from PIL import Image

st.title('所属検索')

df = pd.read_excel('arknights - 完成 (4).xlsx', sheet_name="キャラクター一覧")

# キャラクターの所属を一意にリストアップ
affiliations = df['所属'].unique().tolist()

# ユーザーが所属を選択
selected_affiliation = st.selectbox("所属を選択してください", affiliations)

# 所属に基づいてキャラクターをフィルタリング
filtered_df = df[(df['所属'] == selected_affiliation)]

# 選択された所属のキャラクター名を一意にリストアップ
characters_in_affiliation = filtered_df['名前'].unique().tolist()

# ユーザーがキャラクターを選択
selected_character = st.selectbox("オペレーターを選択してください", characters_in_affiliation)

# 選択されたキャラクターの情報を表示
selected_character_info = filtered_df[filtered_df['名前'] == selected_character]

columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3', 'モジュール-X', 'モジュール-Y', 'モジュール-Δ'
]

if not selected_character_info.empty:
    st.write(selected_character_info)

    # 選択されたキャラクターの情報を表示
    for column in columns_to_display:
        st.write(f"{column}: {selected_character_info[column].values[0]}")

    # キャラクターの画像を表示
    selected_image_path = f"{selected_character}.png"
    try:
        image = Image.open(selected_image_path)
        st.image(selected_image_path, caption=f'{selected_character}', width=350)
    except FileNotFoundError:
        st.write("画像が見つかりませんでした。")
