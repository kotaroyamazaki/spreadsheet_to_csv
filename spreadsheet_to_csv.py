import csv
import datetime
import gspread
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials


def main():
    # .envファイルの読み込み
    load_dotenv()

    # スプレッドシートのIDと範囲
    SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
    RANGE_NAME = os.getenv('RANGE_NAME')
    OUTPUT_FILE_NAME = os.getenv('OUTPUT_FILE_NAME')

    # 認証情報ファイルへのパス
    credential_file = 'credentials.json'

    # APIのスコープ
    scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credential_file, scope)
    gc = gspread.authorize(credentials)

    # スプレッドシートを開く
    workbook = gc.open_by_key(SPREADSHEET_ID)
    print(workbook)
    worksheet = workbook.get_worksheet(0)  # 最初のワークシートを開く

    # スプレッドシートのデータを読み込む
    rows = worksheet.get(RANGE_NAME)
    print(rows)

    del rows[0]  # 最初の行（ヘッダー行）を削除

    # CSVファイルに出力する
    with open(OUTPUT_FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # ログを出力する
    print(f'{datetime.datetime.now()} : CSVに出力しました。')


if __name__ == '__main__':
    main()
