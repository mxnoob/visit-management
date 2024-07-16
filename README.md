# Visit management

## Простое API для мобильного приложения, в котором полевой сотрудник заказчика будет выполнять визиты в магазины.

## Запуск приложения

```shell
# Склонировать репозиторий
git clone git@github.com:mxnoob/visit-management.git
```

> [!IMPORTANT]
> Необходимо создать файл `.env` с переменными окружения.</br>
> Пример файла [.env.example](.env.example)

```shell
# Запустить докер композ
docker compose up -d --build
```

```shell
# добавить моковых данных
# опциональные параметры `add_visits --workers 10 --shops 25 --visits 100`
docker compose exec backend python manage.py add_visits
```

## Пример запроса

```shell
curl -H "Authorization: Phone <phone_number>" http://127.0.0.1:8000/api/shops/
```

```shell
curl -X POST -H "Authorization: Phone <phone_number>" -H "Content-Type: application/json" -d '{"latitude": 55.7558, "longitude": 37.6176}' http://127.0.0.1:8000/api/visit/14/
```
