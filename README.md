# さらぱんぷれぜんすちぇんじゃー

## つかいかた
1 . Discord Developer Portal [(Discord Developer Portal)](https://discord.com/developers/applications)でApplicationを作成する(この時につけた名前が○○をプレイ中の○○になります)

2 . CLIENT IDをコピーする

3 . config.jsonを開く

4 . CLIENT IDを書く

とりあえずそれで起動すると思います。
起動するのを確認したら細かい設定をしていきます。

# config.jsonの設定

__client_id__ Client idを入れる  
__details__   今行っていることを表示する(残り100人 とかのあれ)  
__state__     detailsとの違いがわからない  
__start__     `True` か `False`と入力する Trueにするとプレイ時間が表示される  
__large_image__ Developer Portalで設定した Rich Presence Assetsの名前を書く  
__large_text__ large_imageにカーソルを合わせたときに表示する文字を書く  
__button__ ボタンを表示したいときに使う 好きな文字を入れる __作者の力不足でボタンをTrueにしないと起動できません pythonもうちょい出来るようになってから直します__  
__buttonURL__ ボタンを押したときに飛ぶサイトを決める  

わからないことがあったらDiscord てぃーすぴん#3939 または Twitter @BrightNoahBにDMしてください