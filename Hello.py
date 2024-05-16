import streamlit as st
import pandas as pd
import openpyxl

st.title('アークナイツキャラクター検索サイト')



# エクセルデータを読み込む
df = pd.read_excel('arknights.xlsx',sheet_name="キャラクター一覧")


# 名前に対応する情報を取得して表示
uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

name = st.text_input("名前を入力してください")


# 名前に一致するデータを抽出
filtered_df = df[df['名前'] == name]

# 必要な列のみを選択
columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
filtered_df = filtered_df[columns_to_display]

# 抽出したデータを表示
st.write(filtered_df)
