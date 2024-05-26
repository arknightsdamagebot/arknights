import streamlit as st
import pandas as pd
import openpyxl

html_code = """
<style>
body {
    background-color: #f0f0f0; /* 任意の色を指定 */
}
</style>
"""

st.title('アークナイツキャラクター検索サイト')



st.markdown(html_code, unsafe_allow_html=True)

# エクセルデータを読み込む
df = pd.read_excel('arknights - 完成.xlsx',sheet_name="キャラクター一覧")


name = st.text_input("名前を入力してください")


# 名前に一致するデータを抽出
filtered_df = df[df['名前'] == name]

# 必要な列のみを選択
columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
filtered_df = filtered_df[columns_to_display]

# 抽出したデータを表示
st.write(filtered_df)
