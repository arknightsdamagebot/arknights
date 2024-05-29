import streamlit as st
import pandas as pd
import random

st.title('アークナイツオペレーター検索')
 
df = pd.read_excel('arknights - 完成.xlsx', sheet_name="キャラクター一覧")
 
names = df['名前'].unique().tolist()
selected_name = st.selectbox("名前を選択してください", names)
 
name = st.text_input("名前を入力してください")
 
if name:
    filtered_df = df[df['名前'] == name]
elif selected_name:
    filtered_df = df[df['名前'] == selected_name]
else:
    filtered_df = pd.DataFrame()
 
columns_to_display = [
    '名前', '所属', '職業', '職分', 'レアリティ',
    '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3'
]
filtered_df = filtered_df[columns_to_display]
 
if not filtered_df.empty:
    st.write(filtered_df)
 
    for column in columns_to_display:
        st.write(f"{column}: {filtered_df[column].values[0]}")
else:
    st.write("選択された名前に一致するデータがありません。")

    def main():
    st.title("画像表示アプリ")
    
    # 画像ファイルのパス
    image_path = "https://arknights.wikiru.jp/attach2/417368_E382A2E38383E382B7E383A52E706E67.png"  # 画像ファイルのパスを指定してください
    
    # 画像を表示
    st.image(image_path, caption="事前に準備した画像", use_column_width=True)

if __name__ == "__main__":
    main()