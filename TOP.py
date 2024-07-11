import streamlit as st

st.set_page_config(page_title="アークナイツオペレーター検索", layout="wide")

st.title("アークナイツオペレーター検索")

st.write("アークナイツに登場するオペレーターを検索することができます。")

st.write("**名前検索**では、オペレーターの名前を入力または選択することによって詳細を確認できます。")

st.write("**所属検索**では、所属陣営を入力または選択することによってフィルタリングをすることができます。")

st.write("**職分検索**では、職分を入力または選択することによってフィルタリングをすることができます。")

st.subheader("バフ・デバフ一覧表  \n**攻撃速度UP**:基礎値は全キャラクター100。加速は速度上昇なので、+10でDPSが1.1倍、攻撃間隔が100/110=0.91倍になる。上限は600。  \n**回復力UP**:基礎値に対して%で上昇。医療オペレーターの回復からスキルによる自己回復まで、緑文字で表示される効果が対象。  \n**リジェネ**:フレーム毎にHPを回復し、1秒での合計量が秒間回復量と等しくなる。回復時に回復量の表記が表示されない。味方の治療効果を受けないユニットおよび召喚ユニットも回復可能。回復率上昇効果を受けない。  \n**最大HPUP**:基礎値に対して%で上昇。なおバフした際の現在HPは最大HPに対する割合が同じになるように計算される。**バフ後の現在HP = (バフ前の現在HP÷バフ前の最大HP) × バフ後の最大HP**  \n**加護**:加護が付与された味方の被ダメージを、物理術問わず%で軽減する。確定ダメージは軽減できない。複数の効果は重複せず、効果の高いものが優先される。  \n**バリア**:一定量のダメージを吸収する。  \n**元素損傷バリア**:一定量の元素損傷を吸収する。  \n**シールド**:一定回数のダメージを無効化する。  \n**レジスト**:「スタン、寒冷、凍結状態の継続時間が50%短縮」を付与。  \n**迷彩**:未ブロック時敵の攻撃の対象にならない。但し、範囲攻撃に巻き込まれた場合はダメージを受ける。  \n**脆弱**:付与された敵が受けるダメージを増加させる。複数の効果は重複せず、効果の高いものが優先される。物理・術・確定ダメージに対して有効であり、確定ダメージに影響する唯一のデバフである。  \n**対術脆弱**:付与された敵が受ける術ダメージを増加させる。複数の効果は重複せず、効果の高いものが優先される。【脆弱】とは別枠扱いのため重複可能。  \n**攻撃力DOWN(虚弱)**:敵の攻撃力を下降させることで味方の被ダメージを軽減する。虚弱も同様。直接乗算下降と最終乗算下降の2種類がある。  \n**攻撃速度DOWN**:敵攻撃速度を下げる。基礎値は100で、下がった数値%の速度で攻撃する。-50で半分の速度になる。下限は10。ただしステータスとして参照される下限は20なので実質的には下限20。  \n**移動速度DOWN**:敵の移動速度を%で低下させる。足止めも含め複数重ねると効果は補数の乗算で重複するが、0.05[マス/秒]以下にはならない。  \n**足止め**:実態は「移動速度80%DOWN」。補助オペレーターの緩速師、術師オペレーターの連鎖術師が特性で所持するデバフであり、緩速師の場合は持続0.8秒。1.9秒の攻撃間隔を元に平均化すると約34%の減速に相当する。  \n**バインド**:敵の移動のみを停止させる。攻撃は停止しない。  \n**スタン**:敵の移動を停止させ、攻撃およびスキル使用も同時に停止させる。  \n**睡眠**:敵の移動、攻撃、スキル使用を停止させるが、同時に無敵とブロック不可も付与する。無敵なので攻撃対象にできないだけでなく、持続ダメージ、環境ダメージ、ダメージタイプの自傷ダメージなども受けなくなる。  \n**寒冷・凍結**:寒冷は敵の攻撃速度-30。凍結は移動、攻撃、スキル使用を停止させ、術耐性-15。  \n**浮遊**:浮遊が付与された敵は、その場で浮き上がり行動不能となったうえで、飛行ユニットとみなされる。ただし重量が3を超えている敵に対しては効果時間が半減する。浮遊中の敵は移動不能、攻撃不能、スキル使用不能となる代わりに、ブロック不可となり、強制移動耐性も付与される。  \n**反重力**:付与された敵の重量ランクが1減少する。複数の反重力効果は重複しない。  \n**ステルス無効化**:敵のステルス能力(非ブロック中は攻撃対象にならず、ダメージを受けない)を無効化する。  \n**戦慄**:戦慄状態の敵がブロックされると、通常近接攻撃を行えなくなる。  \n**コスト軽減**:初期所持コストの増加や、特定のオペレーターの配置コスト軽減。")


