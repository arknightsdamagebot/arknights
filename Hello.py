import streamlit as st
import pandas as pd
import random

st.title('アークナイツオペレーター検索')
 
df = pd.read_excel('arknights - 完成 (2).xlsx', sheet_name="キャラクター一覧")
 
names = df['名前'].unique().tolist()
selected_name = st.selectbox("名前を選択してください", names)
filtered_df = df[df['名前'] == selected_name]
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]
filtered_df = filtered_df[columns_to_display]