import streamlit as st

st.set_page_config(page_title="アークナイツオペレーター検索", layout="wide")

# App title and creator
st.title("アークナイツオペレーター検索")

st.write("アークナイツに登場するオペレーターを検索することができます。")

st.write("名前検索では、オペレーターの名前を入力または選択することによって詳細を確認できます。")

st.write("所属検索では、所属陣営を入力または選択することによってフィルタリングをすることができます。")

st.write("職分検索では、職分を入力または選択することによってフィルタリングをすることができます。")

st.markdown("バフ・デバフ一覧表  \n加護:加護が付与された味方の被ダメージを、物理術問わず%で軽減する。確定ダメージは軽減できない。複数の効果は重複せず、効果の高いものが優先される。  \nバリア:一定量のダメージを吸収する。  \n元素損傷バリア:一定量の元素損傷を吸収する。  \nシールド:一定回数のダメージを無効化する。  \nレジスト:「スタン、寒冷、凍結状態の継続時間が50%短縮」を付与。  \n迷彩:未ブロック時敵の攻撃の対象にならない。但し、範囲攻撃に巻き込まれた場合はダメージを受ける。  \n脆弱:付与された敵が受けるダメージを増加させる。複数の効果は重複せず、効果の高いものが優先される。物理・術・確定ダメージに対して有効であり、確定ダメージに影響する唯一のデバフである。  \n足止め:実態は「移動速度80%DOWN」。補助オペレーターの緩速師、術師オペレーターの連鎖術師が特性で所持するデバフであり、緩速師の場合は持続0.8秒。1.9秒の攻撃間隔を元に平均化すると約34%の減速に相当する。  \nバインド:敵の移動のみを停止させる。攻撃は停止しない。  \nスタン:敵の移動を停止させ、攻撃およびスキル使用も同時に停止させる。  \n睡眠:敵の移動、攻撃、スキル使用を停止させるが、同時に無敵とブロック不可も付与する。無敵なので攻撃対象にできないだけでなく、持続ダメージ、環境ダメージ、ダメージタイプの自傷ダメージなども受けなくなる。  \n寒冷・凍結:寒冷は敵の攻撃速度-30。凍結は移動、攻撃、スキル使用を停止させ、術耐性-15。  \n浮遊:浮遊が付与された敵は、その場で浮き上がり行動不能となったうえで、飛行ユニットとみなされる。ただし重量が3を超えている敵に対しては効果時間が半減する。浮遊中の敵は移動不能、攻撃不能、スキル使用不能となる代わりに、ブロック不可となり、強制移動耐性も付与される。  \n反重力:付与された敵の重量ランクが1減少する。複数の反重力効果は重複しない。  \n")