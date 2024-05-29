import streamlit as st
import pandas as pd
import random
 
background_images = [
    'https://arknights.wikiru.jp/attach2/E3839FE383A5E383ABE382B8E382B9_6D75656C737973655F322E706E67.png',
    'https://arknights.wikiru.jp/attach2/E382B7E383ABE38390E383BCE382A2E38383E382B7E383A5_E382B7E383ABE38390E383BCE382A2E38383E382B7E383A52E706E67.png',
    'https://arknights.wikiru.jp/attach2/E38381E383A7E383B3E383A6E382A8_43686F6E677975655F456C6974655F322E6A7067.jpg',
]

# ランダムに画像を選択
selected_image = random.choice(background_images)

# CSSを使って背景画像を設定
page_bg_img = f"""
<style>
body {{
    background-image: url("{selected_image}");
    background-size: cover;
}}
</style>
"""

# CSSをStreamlitに適用
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('アークナイツオペレーター検索')
 
# エクセルデータを読み込む
df = pd.read_excel('arknights - 完成.xlsx', sheet_name="キャラクター一覧")
 
# 名前の選択肢を作成
names = df['名前'].unique().tolist()
selected_name = st.selectbox("名前を選択してください", names)
 
# テキスト入力による名前検索
name = st.text_input("名前を入力してください")
 
# 選択された名前で DataFrame をフィルタリング
if name:
    filtered_df = df[df['名前'] == name]
elif selected_name:
    filtered_df = df[df['名前'] == selected_name]
else:
    filtered_df = pd.DataFrame()
 
# 表示するカラムを選択
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]
filtered_df = filtered_df[columns_to_display]
 
# DataFrame が空でない場合にのみ結果を表示
if not filtered_df.empty:
    st.write(filtered_df)
 
    # 各カラムの値を個別に表示
    for column in columns_to_display:
        st.write(f"{column}: {filtered_df[column].values[0]}")
else:
    st.write("選択された名前に一致するデータがありません。")