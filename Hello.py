import streamlit as st
import pandas as pd

st.title('アークナイツキャラクター検索サイト')

uploaded_file = st.file_uploader("https://d.docs.live.net/b47bda82cedbc7ec/ドキュメント/arknights.xlsx", type="xlsx")

if uploaded_file:
    # エクセルデータを読み込む
    df = pd.read_excel(uploaded_file)

    
    string_cols = df.select_dtypes(include=['名前']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)

    string_cols2 = df.select_dtypes(include=['所属']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols2:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols3 = df.select_dtypes(include=['職業']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols3:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols4 = df.select_dtypes(include=['職分']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols4:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols5 = df.select_dtypes(include=['レアリティ']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols5:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols6 = df.select_dtypes(include=['公開求人']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols6:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols7 = df.select_dtypes(include=['素質1']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols7:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols8 = df.select_dtypes(include=['素質2']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols8:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols9 = df.select_dtypes(include=['スキル1']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols9:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols11 = df.select_dtypes(include=['スキル2']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols11:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)
    
    string_cols12 = df.select_dtypes(include=['スキル3']).columns

    # 文字列列をUnicodeに変換する
    for col in string_cols12:
        df[col] = df[col].apply(lambda x: str(x).encode('utf-8').decode('utf-8') if pd.notnull(x) else x)


# 名前に対応する情報を取得して表示
uploaded_file = st.file_uploader("Upload an Excel file", type="xlsx")

name = st.text_input("名前を入力してください")

if uploaded_file:
    # Excelデータを読み込む
    df = pd.read_excel(uploaded_file)


    # 名前に一致するデータを抽出
    filtered_df = df[df['名前'] == name]

    # 必要な列のみを選択
    columns_to_display = ['名前', '所属', '職業', '職分', 'レアリティ', '公開求人', '素質1', '素質2', 'スキル1', 'スキル2', 'スキル3']
    filtered_df = filtered_df[columns_to_display]

    # 抽出したデータを表示
    st.write(filtered_df)
