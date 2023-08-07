# rest-MySQL
(即興)RestAPIでMySQLの読み書き消しをできるようにしたもの
## 事前準備
```bash
docker network create --subnet=172.18.0.0/24 external-api
```
上記実行後、
```bash
docker-compose up -d
```

### (POST) /create-item
Bodyを下記のように表記
```JSON
{
  "key": "record1234",
  "body": "プログラム作成 Aug 6 2023"
}
```
**key** がプライマリキーとなる。

### (GET) /get-item/<key>
例えば、/get-item/record1234にアクセスすると
```
プログラム作成 Aug 6 2023
```
が帰ってくる。


### (DELTE) /delete-item/<key>
/delete-item/record1234
でAPIコールすると、
keyとbodyの値が削除される。
