import streamlit as st
import pandas as pd
import openpyxl

st.title('アークナイツオペレーター検索')

@st.cache
def load_data():
    return pd.read_excel('arknights - 完成.xlsx', sheet_name="キャラクター一覧")

df = load_data()

name = st.text_input("名前を入力してください")

# 名前に一致するデータを抽出
filtered_row = df[df['名前'] == name]

# 抽出した行があるかどうかをチェック
if not filtered_row.empty:
    # 名前に対応する文章を取得
    selected_text = filtered_row.iloc[0]['文章']
    st.write(selected_text)
else:
    st.warning("該当する名前の文章が見つかりませんでした。")

filtered_df = df[df['名前'] == name]

columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
filtered_df = filtered_df[columns_to_display]

st.write(filtered_df)
st.write(filtered_df['名前'].values[0])
