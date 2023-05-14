# spreadsheet_to_csv

Google スプレッドシートからデータを読み込み、それを CSV ファイルに出力する Python スクリプトです。

## 機能

Google スプレッドシートからデータを読み込む
読み込んだデータを CSV ファイルに出力する
スプレッドシートの最初の行（ヘッダー行）を無視する
出力した CSV ファイル名を環境変数から設定する
スクリプトの実行ログを表示する

## 必要条件

- Python 3.6 以上
- Google スプレッドシート API の有効化とサービスアカウントキーの生成
  以下の Python パッケージのインストール
- gspread
- oauth2client
- python-dotenv

## インストール

- このリポジトリをクローンまたはダウンロードします。
- 必要な Python パッケージをインストールします：pip install -r requirements.txt
- Google スプレッドシート API を有効にし、サービスアカウントキー（JSON ファイル）を生成します。
- 生成したサービスアカウントキーを credentials.json としてプロジェクトのルートディレクトリに保存します。
- .env ファイルを作成し、以下の環境変数を設定します：

```
SPREADSHEET_ID=your_spreadsheet_id_here
RANGE_NAME=your_range_here
OUTPUT_FILE_NAME=auth.csv
```

- スクリプトを実行します：`python main.py`

## 注意事項

- Google スプレッドシートの ID は、スプレッドシートの URL から取得できます。
- 範囲は、スプレッドシート内の特定の範囲を指定するための文字列です（例：'Sheet1!A1:B10'）。
- OUTPUT_FILE_NAME は出力する CSV ファイルの名前を指定します。
- スクリプトを実行する前に、スプレッドシートにサービスアカウントがアクセスできるように設定する必要があります。スプレッドシートを開き、サービスアカウントのメールアドレスを共有設定に追加してください。
