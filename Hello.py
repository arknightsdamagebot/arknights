import streamlit as st
import pandas as pd
import openpyxl
import random

image_urls = [
    "https://arknights.wikiru.jp/index.php?plugin=attach&refer=%E3%83%A0%E3%83%AA%E3%83%8A%E3%83%BC%E3%83%AB&openfile=mlynar_e2.png",
    "https://arknights.wikiru.jp/attach2/E3839FE383A5E383ABE382B8E382B9_6D75656C737973655F322E706E67.png",
    "https://arknights.wikiru.jp/attach2/E383B4E382A3E382B8E382A7E383AB_766967696C5F65706F7175652E706E67.png",
]

def main():
    # Streamlitアプリケーションのタイトル
    st.title('アークナイツオペレーター検索サイト')

    # ランダムに画像を選択
    random_image_url = random.choice(image_urls)

    # CSSを使用して背景画像を設定
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url("{random_image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )




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
