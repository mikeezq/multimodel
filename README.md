## Настройка окружения
```shell
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Локальный запуск postgresql
```shell
./postgres-run.sh
```

To connect via psql to local postgres:
```shell
psql -U local-db -d local-db -h localhost
```

## MongoDB

Для запуска и подключения к монго
```shell
brew install mongodb-community@7.0
brew services start mongodb-community@7.0
mongosh # консоль для работы с базой
```

Для отключения сервера
```shell
brew services stop mongodb-community@7.0
```

## Localstack
Localstack - локальный s3
Для запуска:
```shell
brew install pkg-config libvirt
pip install localstack[runtime]
localstack start --host
```



## TODO:
- кнопочка logout
- typing
- сделать актеров с их ролью
- описание для добавления фильма
- сделать возможность загрузки картинки профиля