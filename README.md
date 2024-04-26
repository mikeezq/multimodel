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
brew services start mongodb-community@7.0
mongosh
```

Для отключения сервера
```shell
brew services stop mongodb-community@7.0
```

## TODO:
- кнопочка logout
- хеширование паролей
- полноценное кэширование запросов
- валидация пользовательских данных (например одинаковые username / email и тп)
- typing
- вынести админку из run.py