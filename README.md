# システム開発プロジェクト基礎　1Q レポート課題


## このサーバーはCoroutineに基づいて作った


### 環境：
- python 3.7.3
- mysql 8.0.16

### File
- server.py server file
- orm.py orm file
- models.py todo model config file
- coroweb.py framework of server
- config.py convert config_default.py into dict
- config_default.py you can set dbuser and dbpassword here
- apis.py one APIError include here
- handles.py handle url, you can add url here
- create_database.py create database and file, dbuser:todotest, dbpassword:todotest

### server:
- eventの登録ができる
- 全てのeventを取得できる
- 一つのeventを取得できる
- あるeventを消去できる

### 実行方法:
```
1.requirements.txt 中のライブラリをインストールする
2.create_database.pyを実行して、データベースと表を作成する(dbuser:todotest, dbpsword:todotest)
3.server.pyを実行する
```

## API
### イベントの登録 request
```
POST /api/v1/todo  
{"deadline": "2019-06-11T14:00:00+09:00", "title": "report", "memo": ""}
```

コマンドライン  

```  
curl -X POST -H "Content-Type: application/json" -d '{"deadline": "2019-06-11T14:00:00+09:00", "title": "report", "memo": ""}' http://localhost:8080/api/v1/todo

```

### イベントの登録 response
```
200 OK
{"status": "success", "message": "registered", "id": 1}
###時間フォーマットが違い場合
400 Bad Request
{"status": "failure", "message": "invalid date format"}
###データフォーマットが違い場合
400 Bad Request
{"status": "failure", "message": "JSON body must be object"}
###headが違い場合
400 Bad Request
{"status": "failure", "message": "Unsupported Content-Type"}
```
### 全てのイベントの取得 request
```
GET /api/v1/todo
```
コマンドライン

```
curl -X GET http://localhost:8080/api/v1/todo
```
### 全てのイベントの取得 response
```
200 OK
{"events": [
    {"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "report", "memo": ""},
    ...
]}
```
### id(1)のイベントの取得 request
```
GET /api/v1/todo/id
```
コマンドライン  
```
curl -X GET http://localhost:8080/api/v1/todo/1
```
### id(=1)のイベントの取得 response
```
200 OK
{"id": 1, "deadline": "2019-06-11T14:00:00+09:00", "title": "レreport", "memo": ""}

404 Not Found
{'status': 'failure', 'message': 'Event not found', 'id': 1}
```

### id(=1)のイベントの消去 request
```
DELETE /api/v1/todo/1
```
コマンドライン  
```
curl -X DELETE http://localhost:8080/api/v1/todo/1
```
### id(=1)のイベントの消去 response
```
200 OK
{'status': 'success', 'message': 'deleted', 'id': 1}

404 Not Found
{'status': 'failure', 'message': 'Event not found', 'id': 1}
```
