import streamlit as st
import pandas as pd

# Excelファイルからデータを読み込む
excel_file = 'https://oitast-my.sharepoint.com/personal/omzh220247_st_oita-ed_jp/Documents/[アークナイツ表　キャラ.xlsx]Sheet1'  # Excelファイルのパス
df = pd.read_excel(excel_file)

# Streamlitアプリケーションのタイトル
st.title('アークナイツキャラクター検索サイト')

# ユーザーから名前を入力
name = st.text_input('名前を入力してください')

# 名前に対応する情報を取得して表示
if name:
    # 名前がExcelファイルに存在するかチェック
    if name in df['名前'].values:
        info = df[df['名前'] == name]  # 名前に対応する行を取得
        st.write(f'**{name}** さんの情報:')
        st.write(f"所属: {info['所属'].values[0]}")
        st.write(f"職業: {info['職業'].values[0]}")
        st.write(f"職分: {info['職分'].values[0]}")
        st.write(f"レアリティ: {info['レアリティ'].values[0]}")
        st.write(f"公開求人: {info['公開求人'].values[0]}")
        st.write(f"素質1: {info['素質1'].values[0]}")
        st.write(f"素質2: {info['素質2'].values[0]}")
        st.write(f"スキル1: {info['スキル1'].values[0]}")
        st.write(f"スキル2: {info['スキル2'].values[0]}")
        st.write(f"スキル3: {info['スキル3'].values[0]}")
    else:
        st.write('その名前の情報は見つかりませんでした')
