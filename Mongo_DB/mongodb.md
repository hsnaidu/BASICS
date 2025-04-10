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
