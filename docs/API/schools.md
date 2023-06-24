# Schools

School is a place where students study.

Model: ``backend.apps.core.models.School``

## Fields

| Field       | Type            | Description                              |
| ----------- | --------------- | ---------------------------------------- |
| id          | integer         | Unique identifier                        |
| name        | string          | Name of the school                       |
| description | string          | Description                              |
| plugins     | ManyToManyField | Plugins that are enabled for this school |

## Example

### Detailed

```json
{
  "id": 1,
  "plugins": [
    {
      "id": 3,
      "name": "homework",
      "description": "Дает возможность ученикам просматривать домашнее задание, которое может быть добавлено учителями.",
      "icon": "http://127.0.0.1:8000/media/plugins/homework.png",
      "month_price": 0
    },
    {
      "id": 1,
      "name": "timetable",
      "description": "Позволяет ученикам просматривать свое расписание, которое задается администраторами для каждого класса.",
      "icon": "http://127.0.0.1:8000/media/plugins/timetable.png",
      "month_price": 0
    }
  ],
  "name": "ГБОУ Академическая гимназия №56",
  "description": ""
}
```

### Compact

```json
{
    "id": 1,
    "name": "Академическая гимназия №56",
    "plugins": [
        3,
        1
    ]
}
```

## API endpoints

| Endpoint             | Methods         | Desciption             |
| -------------------- | --------------- | ---------------------- |
| `/api/subjects/`     | GET             | List schools           |
| `/api/subjects/<id>` | GET, PATCH, PUT | Get or update a school |

## Parameters

### `/api/subjects/`

| Parameter | Type    | Description                                            |
| --------- | ------- | ------------------------------------------------------ |
| `compact` | boolean | If true, don't show detailed information about plugins |
