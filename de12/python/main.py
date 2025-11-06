from openai import OpenAI

#APIを使うkeyを入力します。これは絶対にwebページなどで公開してはいけません。
client = OpenAI(api_key=)

question = input("AIに聞きたいことを入れてね：")

#ここがAPIです----------------------------
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": question}]
)
#---------------------------------------

print("AIの答え：", response.choices[0].message.content)
