import streamlit as st

st.set_page_config(page_title="アークナイツオペレーター検索", layout="wide")

st.title("アークナイツオペレーター検索")

st.write("アークナイツに登場するオペレーターを検索することができます。")

st.write("**名前検索**では、オペレーターの名前を入力または選択することによって詳細を確認できます。")

st.write("**所属検索**では、所属陣営を入力または選択することによってフィルタリングをすることができます。")

st.write("**職分検索**では、職分を入力または選択することによってフィルタリングをすることができます。")

st.subheader("バフ・デバフ一覧表  \n**攻撃速度UP**:基礎値は全キャラクター100。加速は速度上昇なので、+10でDPSが1.1倍、攻撃間隔が100/110=0.91倍になる。上限は600。  \n**回復力UP**:基礎値に対して%で上昇。医療オペレーターの回復からスキルによる自己回復まで、緑文字で表示される効果が対象。  \n**リジェネ**:フレーム毎にHPを回復し、1秒での合計量が秒間回復量と等しくなる。回復時に回復量の表記が表示されない。味方の治療効果を受けないユニットおよび召喚ユニットも回復可能。回復率上昇効果を受けない。  \n**最大HPUP**:基礎値に対して%で上昇。なおバフした際の現在HPは最大HPに対する割合が同じになるように計算される。**バフ後の現在HP = (バフ前の現在HP÷バフ前の最大HP) × バフ後の最大HP**  \n**加護**:加護が付与された味方の被ダメージを、物理術問わず%で軽減する。確定ダメージは軽減できない。複数の効果は重複せず、効果の高いものが優先される。  \n**バリア**:一定量のダメージを吸収する。  \n**元素損傷バリア**:一定量の元素損傷を吸収する。  \n**シールド**:一定回数のダメージを無効化する。  \n**レジスト**:「スタン、寒冷、凍結状態の継続時間が50%短縮」を付与。  \n**迷彩**:未ブロック時敵の攻撃の対象にならない。但し、範囲攻撃に巻き込まれた場合はダメージを受ける。  \n**脆弱**:付与された敵が受けるダメージを増加させる。複数の効果は重複せず、効果の高いものが優先される。物理・術・確定ダメージに対して有効であり、確定ダメージに影響する唯一のデバフである。  \n**対術脆弱**:付与された敵が受ける術ダメージを増加させる。複数の効果は重複せず、効果の高いものが優先される。【脆弱】とは別枠扱いのため重複可能。  \n**攻撃力DOWN(虚弱)**:敵の攻撃力を下降させることで味方の被ダメージを軽減する。虚弱も同様。直接乗算下降と最終乗算下降の2種類がある。  \n**攻撃速度DOWN**:敵攻撃速度を下げる。基礎値は100で、下がった数値%の速度で攻撃する。-50で半分の速度になる。下限は10。ただしステータスとして参照される下限は20なので実質的には下限20。  \n**移動速度DOWN**:敵の移動速度を%で低下させる。足止めも含め複数重ねると効果は補数の乗算で重複するが、0.05[マス/秒]以下にはならない。  \n**足止め**:実態は「移動速度80%DOWN」。補助オペレーターの緩速師、術師オペレーターの連鎖術師が特性で所持するデバフであり、緩速師の場合は持続0.8秒。1.9秒の攻撃間隔を元に平均化すると約34%の減速に相当する。  \n**バインド**:敵の移動のみを停止させる。攻撃は停止しない。  \n**スタン**:敵の移動を停止させ、攻撃およびスキル使用も同時に停止させる。  \n**睡眠**:敵の移動、攻撃、スキル使用を停止させるが、同時に無敵とブロック不可も付与する。無敵なので攻撃対象にできないだけでなく、持続ダメージ、環境ダメージ、ダメージタイプの自傷ダメージなども受けなくなる。  \n**寒冷・凍結**:寒冷は敵の攻撃速度-30。凍結は移動、攻撃、スキル使用を停止させ、術耐性-15。  \n**浮遊**:浮遊が付与された敵は、その場で浮き上がり行動不能となったうえで、飛行ユニットとみなされる。ただし重量が3を超えている敵に対しては効果時間が半減する。浮遊中の敵は移動不能、攻撃不能、スキル使用不能となる代わりに、ブロック不可となり、強制移動耐性も付与される。  \n**反重力**:付与された敵の重量ランクが1減少する。複数の反重力効果は重複しない。  \n**ステルス無効化**:敵のステルス能力(非ブロック中は攻撃対象にならず、ダメージを受けない)を無効化する。  \n**戦慄**:戦慄状態の敵がブロックされると、通常近接攻撃を行えなくなる。  \n**コスト軽減**:初期所持コストの増加や、特定のオペレーターの配置コスト軽減。")

st.subheader("装置一覧表  \n**障害物**:ブロックされた敵および溶岩噴出孔によるダメージのみ受ける。配置により敵出現地点と防衛ラインを繋ぐ経路が塞がれる場合配置できない。敵ユニットの経路が全て封鎖された場合、障害物を無視して最も近い経路を探す。  \n**妨害装置**:範囲内の敵ドローンは攻撃不能、特殊能力が無効化、更に移動速度-50%。敵はこの装置を優先して攻撃する  \n**簡易補給所**:4秒ごとに味方のSPを3回復。  \n**妨害地雷**:起動後、敵がこのマスに侵入時に爆発し、一定範囲内の敵全員に2000確定ダメージを与え、15秒間被ダメージ+50%の状態を付与。  \n**伐採作業員**:おばけ茸を伐採し、遠距離ユニットを配置可能な切り株にする。  \n**ミスターランブル**:隣接4マス範囲以内の敵全員を12秒間スタンさせる。  \n**ミェシュココイル**:攻撃範囲に他のミェシュココイルがいる場合、通電状態になる。2.3秒ごとに電流が発生し、経路上の敵に250の術ダメージを与え、1.5秒足止めする。  \n**改良型爆竹**:配置後爆発し、隣接4マス内にいる敵全員に500の術ダメージを与え、さらに範囲内にいる敵全員と晦明の印の属性変化を与える。  \n**補強装置**:土石構造を補強して砂嵐の影響を受けなくなる。  \n**スノーズントの安全クレーン**:直ちにオペレーターを撤退させ、再配置までの時間を80%減少させる。  \n**耐水蝕コーティング装置**:前方1マスの味方に「水蝕」無効化状態を付与する（「水蝕」：攻撃速度低下、1秒ごとに侵蝕損傷を受け、攻撃を受けた時に被ダメージと比例する侵蝕損傷を受ける）。  \n**爆破装置**:配置後即座に爆発し、正面1マスにいる敵にダメージを与え、普通の力で突き飛ばす。効果範囲内の<脆い石柱>を倒壊させる。  \n**主なき財宝**:敵に接触されると消滅する。戦闘終了時、宝箱が場に存在する場合、報酬に源石錐が1個追加される。  \n**壊れたスモークマシン**:周囲一定範囲内の敵全員の移動速度-60%。  \n**ガスボンベ**:周囲の敵全員をかなりの力で突き飛ばす。  \n**聖徒の御手**:配置方向に「聖徒の御手」を放ち、触れた敵にダメージとスタンを与える。  \n**聖徒の御手・清掃モード**:配置方向に「聖徒の御手」を放ち、触れた敵にダメージとスタンを与え、経路上の「溟痕」を取り除く。  \n**聖徒の御手・巡回モード**:配置方向に「聖徒の御手」を放ち、触れた敵にダメージとスタンを与える。壁にぶつかると跳ね返り、繰り返し命中した敵のスタン時間が延長される。  \n**アラデルの衛護**:配置後、対象と周囲にいる味方全員に1000までの被ダメージを吸収可能なバリアを付与する。  \n**掩体**:敵を4体までブロック。  \n**救急バッグ**:攻撃範囲内の味方ユニット1体のHPを1000回復。  \n**ダイス**:配置時、ダイスロールの回数を1消費し、ダイスの出目に応じて敵の移動速度と攻撃速度を15秒間低下させる。出目が大きいほど効果も高くなる。  \n**8面ダイス**:配置時、ダイスロールの回数を1消費し、ダイスの出目に応じて敵の移動速度と攻撃速度を15秒間低下させ、さらに出目によっては再配置待ちの味方の再配置時間を減少させる。出目が大きいほど効果も高くなる。  \n**12面ダイス**:配置時、ダイスロールの回数を1消費し、ダイスの出目に応じて敵の移動速度と攻撃速度を15秒間低下させ、さらに出目によっては再配置待ちの味方の再配置時間を0にする。出目が大きいほど効果も高くなる。  \n**特設ボート**:水上に任意のユニットが配置可能なボードを設置  \n**騎士の紋章**:配置後、配置マスの視野を確保する  \n**EMP発生装置**:コスト10で使用可能、使用後周囲の敵全員にダメージを与え、7秒間スタンさせる  \n**探知機**:起動後周囲一定範囲内の敵全員のステルス状態を無効化する  \n**コマンドシステム**:所持コストを20消費して次の効果を発動させる：防御力+200%、術耐性+20、1秒ごとHPが10回復、配置可能数+1。破壊された場合耐久値-1  \n**源石気流発生装置**:前方3マスに気流を排出し、気流範囲内、気流と同方向/逆方向に配置する味方の攻撃力上昇/低下、気流と同方向/逆方向に移動する敵の移動速度上昇/低下  \n**おばけ茸**:隣接4マスにいる味方ユニットの防御力上昇。<伐採作業員>の伐採後、オペレーター配置可能な遠距離マスになる  \n**フロストノヴァの源石氷晶**:一定時間ごとに、周囲一定範囲内の敵全員に10秒間寒冷状態を付与する衝撃波を発生させる  \n**パトリオットの源石祭壇**:衝撃波を発生させ、周囲一定範囲内の敵全員に2000の確定ダメージを与える")
