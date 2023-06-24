# Subjects

Subject is an area of knowledge that is studied in school.

Model: ``backend.apps.core.models.Subject``

## Fields

| Field      | Type    | Description                |
| ---------- | ------- | -------------------------- |
| id         | integer | Unique identifier          |
| name       | string  | Name of the subject        |
| icon       | string  | Icon of the subject        |
| descrition | string  | Description of the subject |

## Example

```json
{
    "id": 2,
    "name": "Astronomy",
    "icon": "http://127.0.0.1:8000/media/subjects/astronomy.png",
    "description": "Astronomy is a natural science that studies celestial objects and phenomena."
}
```

## API endpoints

| Endpoint                     | Methods                 | Desciption                      |
| ---------------------------- | ----------------------- | ------------------------------- |
| `/api/subjects/`     | GET, POST               | List subjects / Create subject  |
| `/api/subjects/<id>` | GET, PATCH, PUT, DELETE | Get, update or delete a subject |
