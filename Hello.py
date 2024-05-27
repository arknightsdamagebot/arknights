import streamlit as st
import pandas as pd
import openpyxl

st.title('アークナイツオペレーター検索')

# エクセルデータを読み込む
df = pd.read_excel('arknights - 完成.xlsx',sheet_name="キャラクター一覧")

names = df['名前'].unique().tolist()
selected_name = st.selectbox("名前を選択してください", names)

name = st.text_input("名前を入力してください")

filtered_df = df[df['名前'] == selected_name]

columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
filtered_df = filtered_df[columns_to_display]

st.write(filtered_df)
st.write("名前:"+ filtered_df['名前'].values[0])
st.write("所属:"+ filtered_df['所属'].values[0])
st.write("職業:"+ filtered_df['職業'].values[0])
st.write("職分:"+ filtered_df['職分'].values[0])
st.write("レアリティ:"+ filtered_df['レアリティ'].values[0])
st.write("公開求人:"+ filtered_df['公開求人'].values[0])
st.write("素質1:"+ filtered_df['素質1'].values[0])
st.write("素質2:"+ filtered_df['素質2'].values[0])
st.write("スキル1:"+ filtered_df['スキル1'].values[0])
st.write("スキル2:"+ filtered_df['スキル2'].values[0])
st.write("スキル3:"+ filtered_df['スキル3'].values[0])

filtered_df = df[df['名前'] == name]

columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
filtered_df = filtered_df[columns_to_display]

if not name.strip():
    st.error("オペレーターの名前を入力してください")
elif filtered_df.empty:
    st.error("一致する名前のオペレーターは存在しません")
else :
    st.write(filtered_df)
    st.write("名前:"+ filtered_df['名前'].values[0])
    st.write("所属:"+ filtered_df['所属'].values[0])
    st.write("職業:"+ filtered_df['職業'].values[0])
    st.write("職分:"+ filtered_df['職分'].values[0])
    st.write("レアリティ:"+ filtered_df['レアリティ'].values[0])
    st.write("公開求人:"+ filtered_df['公開求人'].values[0])
    st.write("素質1:"+ filtered_df['素質1'].values[0])
    st.write("素質2:"+ filtered_df['素質2'].values[0])
    st.write("スキル1:"+ filtered_df['スキル1'].values[0])
    st.write("スキル2:"+ filtered_df['スキル2'].values[0])
    st.write("スキル3:"+ filtered_df['スキル3'].values[0])

