## 🐍 Python Integration

- MongoDB uses **BSON** (Binary JSON) for communication.
- Python interacts with MongoDB using the **`pymongo`** library.
- BSON supports additional data types and is more efficient than plain JSON.

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]
collection.insert_one({"name": "Hari", "age": 25})
```

---

## ✅ TIPS

| Topic            | Key Concept                                |
|------------------|---------------------------------------------|
| Data Format      | BSON (Binary JSON)                          |
| Structure        | DB → Collection → Document                  |
| CLI Tool         | `mongosh`                                   |
| GUI Tool         | MongoDB Compass                             |
| Insert Methods   | `insertOne`, `insertMany`                   |
| Query Filter     | `find({})`, `findOne({})`, `$eq`, `$in`     |
| Update           | `$set`, `$push`, `upsert`, `replaceOne()`   |
| Delete           | `deleteOne`, `deleteMany`                   |
| Array Query      | `$in`, used for filtering list fields       |
| Sort & Limit     | `sort({field: 1/-1})`, `limit(n)`           |
