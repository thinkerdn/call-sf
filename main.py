"""
Salesforce API サンプルアプリケーション
使用例を示すメインスクリプト
"""

from salesforce_client import SalesforceClient


def main():
    """メイン処理"""
    print("=" * 60)
    print("Salesforce API サンプルアプリケーション")
    print("=" * 60)
    print()
    
    try:
        # Salesforceクライアントの初期化
        client = SalesforceClient()
        print()
        
        # 1. SOQLクエリの実行例
        print("-" * 60)
        print("1. Accountレコードの検索（最新5件）")
        print("-" * 60)
        query_result = client.query("SELECT Id, Name, Type, Industry FROM Account ORDER BY CreatedDate DESC LIMIT 5")
        if query_result and query_result['totalSize'] > 0:
            for record in query_result['records']:
                print(f"  - {record['Name']} (ID: {record['Id']})")
                if record.get('Type'):
                    print(f"    Type: {record['Type']}")
                if record.get('Industry'):
                    print(f"    Industry: {record['Industry']}")
        else:
            print("  レコードが見つかりませんでした")
        print()
        
        # 2. Accountの作成例
        print("-" * 60)
        print("2. 新しいAccountの作成")
        print("-" * 60)
        new_account_id = client.create_account(
            name="テスト株式会社",
            Type="Customer",
            Industry="Technology",
            Phone="03-1234-5678",
            Website="https://example.com"
        )
        print()
        
        if new_account_id:
            # 3. 作成したAccountの取得
            print("-" * 60)
            print("3. 作成したAccountの詳細取得")
            print("-" * 60)
            account = client.get_account(new_account_id)
            if account:
                print(f"  Name: {account.get('Name')}")
                print(f"  Type: {account.get('Type')}")
                print(f"  Industry: {account.get('Industry')}")
                print(f"  Phone: {account.get('Phone')}")
                print(f"  Website: {account.get('Website')}")
            print()
            
            # 4. Accountの更新
            print("-" * 60)
            print("4. Accountの更新")
            print("-" * 60)
            client.update_account(
                new_account_id,
                Phone="03-9876-5432",
                Description="更新されたテストアカウント"
            )
            print()
            
            # 5. 更新後のAccountの確認
            print("-" * 60)
            print("5. 更新後のAccountの確認")
            print("-" * 60)
            updated_account = client.get_account(new_account_id)
            if updated_account:
                print(f"  Phone: {updated_account.get('Phone')}")
                print(f"  Description: {updated_account.get('Description')}")
            print()
            
            # 6. Accountの削除（オプション）
            print("-" * 60)
            print("6. テストAccountの削除")
            print("-" * 60)
            delete_confirm = input("作成したテストAccountを削除しますか？ (y/n): ")
            if delete_confirm.lower() == 'y':
                client.delete_account(new_account_id)
            else:
                print(f"  テストAccountは削除されませんでした (ID: {new_account_id})")
            print()
        
        # 7. オブジェクトメタデータの取得例
        print("-" * 60)
        print("7. Accountオブジェクトのメタデータ取得")
        print("-" * 60)
        metadata = client.describe_object('Account')
        if metadata:
            print(f"  Label: {metadata.get('label')}")
            print(f"  API Name: {metadata.get('name')}")
            print(f"  フィールド数: {len(metadata.get('fields', []))}")
            print(f"  作成可能: {metadata.get('createable')}")
            print(f"  更新可能: {metadata.get('updateable')}")
            print(f"  削除可能: {metadata.get('deletable')}")
        print()
        
        print("=" * 60)
        print("処理が完了しました")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\n設定エラー: {e}")
        print("\n.envファイルを作成し、Salesforceの認証情報を設定してください。")
        print("詳細はREADME.mdを参照してください。")
    except Exception as e:
        print(f"\nエラーが発生しました: {e}")


if __name__ == "__main__":
    main()