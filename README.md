# W2V Service

此份是根據 https://github.com/jyhsu2000/CKIPService 進行修改

所輸入之單字必須為在資料庫中之單詞，單詞資料可查看 vol.txt

W2V 使用 搜狐實驗室 所提供之資料，進行訓練後之模型，拿來做為預測使用
- [資料網址](http://www.sogou.com/labs/resource/cs.php)

## Start service
1. Start the service using `docker-compose`
    ```
    docker-compose up -d
    ```
    If you want to rebuild the image, add `--build` flag when startup
    ```
    docker-compose up --build -d
    ```
2. Service is now on port `4088`

## Stop service
1. Stop the service using `docker-compose`
    ```
    docker-compose down
    ```

## Endpoint
- Main
    - method: `POST`
    - route: `/`
    - parameter
        - `sentence_list`: sentence list for CKIP tagging, split multiple sentences by linebreak(`\n`)

## Test W2V
1. Send request using curl
    ``` bash
    curl -X POST localhost:4088 -F $'sentence_list=閱讀'
