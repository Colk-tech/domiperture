# domiperture
茨城高専生の寮生のための検温サポートDiscord BOTです。 なお製作者は通生です。



## About	

このプログラムは、Python上で動作する検温をサポートするためのDiscord BOTです。	

`!url` と発言するか、決まった時間（デフォルトでは20時）になると、適当な平熱を生成して、エントリーを埋めた状態のGoogleFormsのURLが送信されます。	



### Futures	

#### 要望があれば実装します	

- [ ] 茨城高専以外のGoogleFormsにも対応する	
- [ ] 複数人サーバーでの利用を可能にする	



### 環境構築	

Pythonが動く環境であれば、動作するようになっています。	

まず、`requirements.txt` をインストールした後に、次の環境変数を設定することで使用可能になります。	

（`main.py`がエントリーポイントです）	



- `DISCORD_TOKEN` DiscordBOTのTOKEN。	

- `URL_TEMPLATE` 自動生成させたいURLのテンプレート。	

  例: `https://colk.dev/{building}/{room_number}/{name}/{body_temperature}`	

- `USER_BUILDING` 自動入力する棟の名前。	

- `USER_NAME` 自動入力する氏名。	

- `USER_ROOM_NUMBER` 自動入力する部屋番号。	

