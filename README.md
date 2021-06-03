# W2V Service

此份是根據 https://github.com/jyhsu2000/CKIPService 進行修改

所輸入之單字必須為在資料庫中之單詞，單詞資料可查看 vol.txt

W2V 使用 搜狐實驗室 所提供之資料，進行訓練後之模型，拿來做為預測使用
- [資料網址](http://www.sogou.com/labs/resource/cs.php)

## 啟動伺服器
1. 使用 `docker-compose` 開啟伺服器
    ```
    docker-compose up -d
    ```
    如果需要重新編譯 image , 在啟動時加上 `--build`
    ```
    docker-compose up --build -d
    ```
2. 服務所在的 port `4088`

## 關閉伺服器
1. 關閉伺服器使用  `docker-compose`
    ```
    docker-compose down
    ```

## Endpoint
- Main
    - method: `POST`
    - route: `/`
    - parameter
        - `sentence_list`: word string for W2V

## Test W2V
1. Send request using curl
    ``` bash
    curl -X POST localhost:4088 -F $'sentence_list=閱讀'
