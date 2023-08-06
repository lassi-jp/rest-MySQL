# rest-MySQL
(即興)RestAPIでMySQLの読み書き消しをできるようにしたもの

## (POST) /create-item
Bodyを下記のように表記
```JSON
{
  "key": "record1234",
  "body": "プログラム作成 Aug 6 2023"
}
```
**key** がプライマリキーとなる。

## (GET) /get-item/<key>
例えば、/get-item/record1234にアクセスすると
```
プログラム作成 Aug 6 2023
```
が帰ってくる。


## (DELTE) /delete-item/<key>
/delete-item/record1234
でAPIコールすると、
keyとbodyの値が削除される。
