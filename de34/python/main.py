from openai import OpenAI

print("いまのあなたにおすすめのアニメを診断するサイトです")

#APIを使うkeyを入力します。これは絶対にwebページなどで公開してはいけません。
client = OpenAI(api_key="キー入力")

#ユーザーにする質問
a=input("今の気分を入力")
b=input("今なりたい気分")
c=input("今見たいジャンルを入力")
d=input("最近ハマっていること、ものを入力")
e=input("興味のあること、ものを入力")
f=input("どのくらいの時間で見終えたいか（何分、何クール）入力")
g=input("一番アニメに求めている要素を入力")


#AIにする質問（prompt）
question = f"""
今の気分：{a}
なりたい気分：{b}
見たいジャンル：{c}
最近ハマっていること：{d}
興味のあること：{e}
希望の視聴時間：{f}
アニメに求めている要素：{g}

これらに合うアニメをおすすめしてください。
それぞれに簡単な理由も書いてください。
"""


response = client.chat.completions.create(
    model="gpt-4o-mini",
    #AIに与える役割
    messages=[ {"role": "system", "content": "あなたはアニメに詳しいユーザー嗜好分析AIです。ユーザーの気分や好みからアニメを提案してください"},
        {"role": "user", "content": question}]
)
#---------------------------------------

print("AIの答え：", response.choices[0].message.content)#AIの診断結果でおすすめアニメ表示
