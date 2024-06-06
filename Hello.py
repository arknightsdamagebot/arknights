import streamlit as st
import pandas as pd
import random
from PIL import Image

st.title('アークナイツオペレーター検索')
 
df = pd.read_excel('arknights - 完成 (4).xlsx', sheet_name="キャラクター一覧")
 
names = df['名前'].unique().tolist()
syozokus = df['所属'].unique().tolist()
syokubuns = df['職分'].unique().tolist()
selected_name = st.selectbox("名前を選択してください", names)
selected_syozoku = st.selectbox("所属を選択してください", syozokus)
selected_syokubun = st.selectbox("職分を選択してください", syokubuns)
filtered_df = df[df['名前'] == selected_name]
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]
filtered_df = filtered_df[columns_to_display]
if not filtered_df.empty:
    st.write(filtered_df)

    for column in columns_to_display:
        st.write(f"{column}: {filtered_df[column].values[0]}")
    
    image_path = f"{selected_name}.png"  # 画像のファイルパス
    try:
        image = Image.open(image_path)
        st.image(image_path, caption=f'{selected_name}', width=350)
    except FileNotFoundError:
        st.write("画像が見つかりませんでした。")
else:
    st.write("名前に一致するデータがありません。")
    filtered_df = df[df['所属'] == selected_syozoku]
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]
filtered_df = df[df['職分'] == selected_syokubun]
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]