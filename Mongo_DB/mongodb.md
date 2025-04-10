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