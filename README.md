# Salesforce API Python アプリケーション

PythonでSalesforce APIを呼び出すサンプルアプリケーションです。

## 機能

- Salesforceへの認証と接続
- SOQLクエリの実行
- Accountレコードの作成・取得・更新・削除（CRUD操作）
- オブジェクトメタデータの取得

## 必要な環境

- Python 3.7以上
- Salesforceアカウント（本番環境またはサンドボックス）
- Salesforceセキュリティトークン

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env.example`ファイルを`.env`にコピーして、Salesforceの認証情報を設定します。

```bash
copy .env.example .env
```

`.env`ファイルを編集して、以下の情報を入力してください：

```env
SF_USERNAME=your_username@example.com
SF_PASSWORD=your_password
SF_SECURITY_TOKEN=your_security_token
SF_DOMAIN=login  # サンドボックスの場合は 'test'
```

### 3. Salesforceセキュリティトークンの取得方法

1. Salesforceにログイン
2. 右上のユーザーアイコンをクリック → **設定**
3. 左メニューから **私の個人情報** → **私のセキュリティトークンのリセット**
4. メールで送られてくるセキュリティトークンをコピー

## 使い方

### サンプルアプリケーションの実行

```bash
python main.py
```

このコマンドで以下の操作が実行されます：

1. Accountレコードの検索（最新5件）
2. 新しいAccountの作成
3. 作成したAccountの詳細取得
4. Accountの更新
5. 更新後のAccountの確認
6. テストAccountの削除（確認あり）
7. Accountオブジェクトのメタデータ取得

### カスタムスクリプトの作成

`salesforce_client.py`の`SalesforceClient`クラスを使用して、独自のスクリプトを作成できます。

```python
from salesforce_client import SalesforceClient

# クライアントの初期化
client = SalesforceClient()

# SOQLクエリの実行
result = client.query("SELECT Id, Name FROM Account LIMIT 10")
for record in result['records']:
    print(record['Name'])

# Accountの作成
account_id = client.create_account(
    name="新規会社",
    Type="Customer",
    Industry="Technology"
)

# Accountの取得
account = client.get_account(account_id)
print(account['Name'])

# Accountの更新
client.update_account(account_id, Phone="03-1234-5678")

# Accountの削除
client.delete_account(account_id)
```

## SalesforceClientクラスのメソッド

### `query(soql)`
SOQLクエリを実行します。

**パラメータ:**
- `soql` (str): 実行するSOQLクエリ

**戻り値:**
- dict: クエリ結果

### `get_account(account_id)`
特定のAccountレコードを取得します。

**パラメータ:**
- `account_id` (str): AccountのID

**戻り値:**
- dict: Accountレコード

### `create_account(name, **kwargs)`
新しいAccountレコードを作成します。

**パラメータ:**
- `name` (str): Account名
- `**kwargs`: その他のフィールド（Type, Industry, Phone, Websiteなど）

**戻り値:**
- str: 作成されたレコードのID

### `update_account(account_id, **kwargs)`
Accountレコードを更新します。

**パラメータ:**
- `account_id` (str): AccountのID
- `**kwargs`: 更新するフィールド

**戻り値:**
- bool: 更新成功の可否

### `delete_account(account_id)`
Accountレコードを削除します。

**パラメータ:**
- `account_id` (str): AccountのID

**戻り値:**
- bool: 削除成功の可否

### `describe_object(object_name)`
オブジェクトのメタデータを取得します。

**パラメータ:**
- `object_name` (str): オブジェクト名（例: 'Account', 'Contact', 'Opportunity'）

**戻り値:**
- dict: オブジェクトのメタデータ

## プロジェクト構成

```
call-sf/
├── .env.example          # 環境変数のサンプルファイル
├── .gitignore           # Gitで無視するファイルの設定
├── README.md            # このファイル
├── requirements.txt     # 依存パッケージのリスト
├── salesforce_client.py # Salesforce APIクライアントクラス
└── main.py             # サンプル実行スクリプト
```

## トラブルシューティング

### 認証エラーが発生する場合

- ユーザー名、パスワード、セキュリティトークンが正しいか確認
- セキュリティトークンは、パスワード変更時にリセットされます
- サンドボックス環境の場合、`SF_DOMAIN=test`に設定されているか確認

### API制限について

Salesforceには1日あたりのAPI呼び出し制限があります。制限を超えた場合はエラーが発生します。

## 参考リンク

- [Salesforce REST API ドキュメント](https://developer.salesforce.com/docs/atlas.ja-jp.api_rest.meta/api_rest/)
- [Simple Salesforce ライブラリ](https://github.com/simple-salesforce/simple-salesforce)
- [SOQL リファレンス](https://developer.salesforce.com/docs/atlas.ja-jp.soql_sosl.meta/soql_sosl/)

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。