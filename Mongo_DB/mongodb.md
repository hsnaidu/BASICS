# 📘 MongoDB Cheat Sheet – Quick Guide

---

## 📌 What is MongoDB?

- MongoDB is a **NoSQL, unstructured database**.
- It stores data in **JSON-like documents (BSON)**, making it schema-less and flexible.
- Ideal for handling **unstructured / semi-structured data** in modern applications.

---

## 🧭 Ways to Access MongoDB

| Interface        |Description                    |
|------------------|-------------------------------|
| `mongosh`        | MongoDB Shell (CLI interface) |
| `MongoDB Compass`| Official GUI for MongoDB      |

---

## 🏗️ Basic Concepts

- **Database** = Collection of Tables (aka *Collections*)
- **Collection** = Equivalent to a Table
- **Document** = Equivalent to a Row (stored in JSON-like format)

---

## 📂 Database & Collection Commands

### 🔍 View

``` bash
show dbs                 # List all databases
use <db-name>           # Switch to a database
show collections        # List collections in current DB
```
### 🗑️ Delete

```javascript
use <db-name>
db.dropDatabase()                             // Drop current database
db.<collection-name>.drop()                   // Drop specific collection
```
### ➕ Create

```javascript
db.createCollection("collection-name")        // Explicit creation
db.<collection-name>.insertOne({...})         // Implicitly creates collection
```

---

## 📥 Insert Documents

```javascript
db.<collection>.insertOne({ key: value })          // Insert single doc
db.<collection>.insertMany([{...}, {...}, {...}])  // Insert multiple docs
```

---

## 🔍 Query Documents

### 📃 Basic Find

```javascript
db.<collection>.find({})                          // Get all documents
db.<collection>.find({name: "Alice"})             // Filter by field
db.<collection>.findOne({name: "Alice"})          // Return only one document
```

### 🔎 Filters and Projections

```javascript
db.users.find({name: {$eq: "Hari"}}, {password: 1})   // Filter + project only password
```

---

## 🔢 Comparison Operators

| Operator | Use                          |
|----------|------------------------------|
| `$eq`    | Equal                        |
| `$gt`    | Greater than                 |
| `$lt`    | Less than                    |
| `$gte`   | Greater than or equal        |
| `$lte`   | Less than or equal           |

```javascript
db.users.find({salary: {$gt: 5000}})
```

---

## ⚙️ Logical Operators

```javascript
db.users.find({$and: [{name: "Hari"}, {age: 20}]})
db.users.find({$or: [{name: "Hari"}, {name: "Hemanth"}]})
```

---

## 📚 Arrays & `$in` Operator

```javascript
db.users.find({tags: {$in: ["developer", "designer"]}})
```

Example:

```json
{
  "_id": 1,
  "name": "Alice",
  "tags": ["developer", "designer"]
}
```

---
## 🔄 Update & Replace

### 🧾 Replace Entire Document (⚠️ Must Include All Fields!)

```javascript
db.<collection>.replaceOne({_id: ObjectId()}, {name: "New Name"})
```

### ✏️ Update Fields

```javascript
// Replace or add field
db.<collection>.updateOne({_id: ObjectId()}, {$set: {field: "value"}})

// Push to an array
db.<collection>.updateOne({_id: ObjectId()}, {$push: {skills: "MongoDB"}})

---

## 🗑️ Delete Documents

```javascript
db.<collection>.deleteOne({_id: ObjectId()})                   // Delete single
db.<collection>.deleteMany({category: "crime"})                // Delete multiple
```

---

## 📊 Sorting & Limiting

```javascript
// Sort by name (1 = asc, -1 = desc)
db.users.find().sort({name: 1})

// Limit results to 3
db.users.find().limit(3)

// Sort + limit + project specific fields
db.users.find({}, {name: 1}).sort({name: -1}).limit(3)
```

---
## 🔁 Recovery Notes

- MongoDB standalone instances **do not have replica sets**, so recovery is limited.
- To restore data:
  [Restore Guide](https://www.mongodb.com/docs/ops-manager/current/tutorial/restore-single-database/)

---