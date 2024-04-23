```shell
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To connect via psql to local postgres:
```shell
psql -U local-db -d local-db -h localhost
```


todo:
- кнопка возврата из формы регистрации
- хеширование паролей
- ..