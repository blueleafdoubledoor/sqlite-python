# -*- coding: utf-8 -*-
import os
from sys import argv
import sqlite3

class BaseClass:
    def __init__(self, db_name, table_name, path=None):
        """コンストラクタ
        db_name  -- データベース名
        table_name -- データベースのテーブル名

        引数に取ったdb ファイル名とテーブル名をメンバ変数にセットし
        SQLite を操作するためのコネクターとカーソルを取得する
        """
        self.db_name = db_name
        self.table_name = table_name
        # パスの指定がなければカレントディレクトリを取得
        database_path = path if path is not None else os.path.dirname(os.path.abspath(__file__))
        self.connector = sqlite3.connect(database_path + '/' + self.db_name)
        self.cursor = self.connector.cursor()


    def create_table(self):
        """テーブルの作成
        table_name -- 操作するデータベースのテーブル名
        """
        sql = "CREATE TABLE IF NOT EXISTS {0}(data1 text, data2 text, data3 text, data4 real);"
        self.cursor.execute(sql.format(self.table_name))
        self.connector.commit()
        self.connector.close()


    def is_created_table(self):
        """作成済みのテーブルかどうかをチェックする
        table_name -- 操作するデータベースのテーブル名
        """
        sql = "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='{0}';"
        return self.cursor.execute(sql.format(self.table_name)) is not None


    def d_insert(self):
        insert_list = [
            ("おはよう", "こんにちわ", "こんばんわ", 1.0),
            ("オハヨウ", "コンニチワ", "コンバンワ", 1.1),
            ("Good morning", "Hello", "Good evening", 1.2),
        ]
        sql = "INSERT INTO '{0}' VALUES(?,?,?,?);"
        self.cursor.executemany(sql.format(self.table_name), insert_list)
        self.connector.commit()
        self.connector.close()


    def d_order_by(self, sort_key):
        """情報を並べ替えて出力する
        sort_key -- 並べ替えの判断材料とするフィールド名
        """
        if sort_key is None:
            sql = "SELECT * FROM {0};"
            for row in self.cursor.execute(sql.format(self.table_name)):
                print(row)
        else:
            sql = "SELECT * FROM {0} ORDER BY {1};"
            for row in self.cursor.execute(sql.format(self.table_name, sort_key)):
                print(row)
        self.connector.close()


if __name__ == "__main__":
    # コマンドライン引数を取得
    order = None
    option_1 = None
    argv_num = len(argv)
    if argv_num == 2:
        order = argv[1]
        print(order)
    elif argv_num == 3:
        order = argv[1]
        option_1 = argv[2]
    else:
        print("引数に問題があります")

    base = BaseClass("example.db", "example")
    if order == "create" or order == "c":
        # データベースにテーブルを作成する
        base.create_table()
    elif order == "insert" or order == "i":
        # データベースにデータを格納する
        base.d_insert()
    elif order == "read" or order == "r":
        # データベースの情報を取得する
        base.d_order_by(option_1)
    else:
        # ポート外の命令が来た場合
        print("Order missing.")

