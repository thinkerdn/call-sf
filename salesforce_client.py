"""
Salesforce API クライアント
Salesforceへの接続とデータ操作を行うクラス
"""

import os
from simple_salesforce import Salesforce
from dotenv import load_dotenv


class SalesforceClient:
    """Salesforce APIとの接続を管理するクライアントクラス"""
    
    def __init__(self):
        """環境変数から認証情報を読み込み、Salesforceに接続"""
        load_dotenv()
        
        self.username = os.getenv('SF_USERNAME')
        self.password = os.getenv('SF_PASSWORD')
        self.security_token = os.getenv('SF_SECURITY_TOKEN')
        self.domain = os.getenv('SF_DOMAIN', 'login')
        
        if not all([self.username, self.password, self.security_token]):
            raise ValueError("環境変数が設定されていません。.envファイルを確認してください。")
        
        self.sf = None
        self.connect()
    
    def connect(self):
        """Salesforceに接続"""
        try:
            self.sf = Salesforce(
                username=self.username,
                password=self.password,
                security_token=self.security_token,
                domain=self.domain
            )
            print(f"✓ Salesforceに正常に接続しました (ユーザー: {self.username})")
            return True
        except Exception as e:
            print(f"✗ Salesforce接続エラー: {e}")
            return False
    
    def query(self, soql):
        """
        SOQLクエリを実行
        
        Args:
            soql (str): 実行するSOQLクエリ
            
        Returns:
            dict: クエリ結果
        """
        try:
            result = self.sf.query(soql)
            print(f"✓ クエリ実行成功: {result['totalSize']}件のレコードを取得")
            return result
        except Exception as e:
            print(f"✗ クエリ実行エラー: {e}")
            return None
    
    def get_account(self, account_id):
        """
        特定のAccountレコードを取得
        
        Args:
            account_id (str): AccountのID
            
        Returns:
            dict: Accountレコード
        """
        try:
            account = self.sf.Account.get(account_id)
            print(f"✓ Account取得成功: {account.get('Name', 'N/A')}")
            return account
        except Exception as e:
            print(f"✗ Account取得エラー: {e}")
            return None
    
    def create_account(self, name, **kwargs):
        """
        新しいAccountレコードを作成
        
        Args:
            name (str): Account名
            **kwargs: その他のフィールド
            
        Returns:
            str: 作成されたレコードのID
        """
        try:
            data = {'Name': name, **kwargs}
            result = self.sf.Account.create(data)
            if result.get('success'):
                print(f"✓ Account作成成功: ID={result['id']}")
                return result['id']
            else:
                print(f"✗ Account作成失敗: {result}")
                return None
        except Exception as e:
            print(f"✗ Account作成エラー: {e}")
            return None
    
    def update_account(self, account_id, **kwargs):
        """
        Accountレコードを更新
        
        Args:
            account_id (str): AccountのID
            **kwargs: 更新するフィールド
            
        Returns:
            bool: 更新成功の可否
        """
        try:
            result = self.sf.Account.update(account_id, kwargs)
            print(f"✓ Account更新成功: ID={account_id}")
            return True
        except Exception as e:
            print(f"✗ Account更新エラー: {e}")
            return False
    
    def delete_account(self, account_id):
        """
        Accountレコードを削除
        
        Args:
            account_id (str): AccountのID
            
        Returns:
            bool: 削除成功の可否
        """
        try:
            result = self.sf.Account.delete(account_id)
            print(f"✓ Account削除成功: ID={account_id}")
            return True
        except Exception as e:
            print(f"✗ Account削除エラー: {e}")
            return False
    
    def describe_object(self, object_name):
        """
        オブジェクトのメタデータを取得
        
        Args:
            object_name (str): オブジェクト名（例: 'Account', 'Contact'）
            
        Returns:
            dict: オブジェクトのメタデータ
        """
        try:
            metadata = getattr(self.sf, object_name).describe()
            print(f"✓ {object_name}のメタデータ取得成功")
            return metadata
        except Exception as e:
            print(f"✗ メタデータ取得エラー: {e}")
            return None