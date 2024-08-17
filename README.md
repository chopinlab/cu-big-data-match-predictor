# 콜로라도 볼더 대학원 수업
## Software Architecture Patterns for Big Data
### 설치 과정
파이썬의 경우에는 마이너 버전을 꼭 맞추어야 한다. 파일 패키지 자체가 바뀌는 경우가 많기 때문에, 
상위 버전으로 설치시 호환이 안된다.


```bash
pyenv install 3.10.13
pyenv local 3.10.13

make install test

python3 -m venv env
cp ./backend/.env.example ./backend/.env
```


# Match predictor

The Match Predictor codebase contains an app with several predictors for football results.

## Local development

Follow the instructions below to get the app up and running on your machine.

1.  Install Python 3.10 and a recent version of NPM.
1.  Install dependencies and run tests.
    ```shell
    make install test
    ```
1.  View the list of available tasks
    ```shell
    make
    ```

## Backend

Here are a few tasks that are useful when running the backend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    make backend/test

1.  Run model measurement tests
    ```shell
    make backend/measure
    ```

1.  Run server
    ```shell
    make backend/run
    ```

1.  Run an accuracy report
    ```shell
    make backend/report
    ```

## Frontend

Here are a few tasks that are useful when running the frontend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    make frontend/test
    ```

1.  Run server
    ```shell
    make frontend/run
    ```

## Integration tests

If it's helpful, you may want to run integration tests during development.
Do so with the tasks below.

1.  Run tests
    ```shell
    make integration/test
    ```

1.  Interactive mode
    ```shell
    make integration/run
    ```
