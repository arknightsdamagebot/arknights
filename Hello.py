import streamlit as st
import pandas as pd

# Excelファイルからデータを読み込む
excel_file = 'https://d.docs.live.net/b47bda82cedbc7ec/ドキュメント/arknights.xlsx'  # Excelファイルのパス

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


# Streamlitアプリケーションのタイトル
st.title('アークナイツキャラクター検索サイト')

# ユーザーから名前を入力
name = st.text_input('名前を入力してください')

# 名前に対応する情報を取得して表示
if name:
    # 名前がExcelファイルに存在するかチェック
    if name in df['名前'].values:
        info = df[df['名前'] == name]  # 名前に対応する行を取得
        st.write(f'**{name}** の情報:')
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
