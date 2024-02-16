# 0x0E - SQL More Queries
## Features covered
### 1. Creating new users and granting them priviledges
**Syntax:**
```bash
-- To create a new user:
CREATE USER '<new-user-name>'@'<host>' IDENTIFIED BY '<password>';
```
```bash
-- To grant new user priviledges to define and control data structures:
GRANT <priviledge[s]> TO <user>@<host> [WITH GRANT OPTION];
```
### 2. Connect two or more tables using `JOIN` clauses. There are different types of **JOIN** clauses:
- `NATURAL JOIN`
- `INNER JOIN`
- `FULL OUTER JOIN`
- `LEFT OUTER JOIN`
- `RIGHT OUTER JOIN`
- `CROSS JOIN` - Cumbersome output
**EX:**
```bash
SELECT cFirstName, cLastName, OrderDate
FROM Customers NATURAL JOIN Orders;
```
### 3. Using SQL Constraints when creating tables such as `NOT NULL`, `UNIQUE`, etc.
 SQL constraint are used to restrict or limit the type of data to be entered at a column during table creation
```bash
CREATE TABLE 'new_table' (
`Id` INTEGER NOT NULL,
`FirstName` VARCHAR(33) NOT NULL UNIQUE,
`LastName` VARCHAR(33)
);
```
### 4. Learning about Subqueries
Subqueries are queries used to get an additional information needed by the main query. For example we are told to get all customers that live in the same **town** as **'Olivia Olsen'**.
- First we don't know what **town** is **Olivia** located. And we cannot look it up from the table
- So to do this, we need to make more than one query
First we need to know what town is Olivia located and use that information to find others, so to do this, we need:
```bash
SELECT cFirstName, cLastName
FROM Customers
WHERE Town = ??? -- Because we don't know Olivia's town
```
AND
```bash
SELECT Town
FROM Customers
WHERE cFirstName = 'Olivia' AND cLastName = 'Olsen'
```
SO to do this, we make the second query a subquery
LIKE THIS:
```bash
SELECT cFirstName, cLastName
FROM Customers
WHERE Town = (
SELECT Town
FROM Customers
WHERE cFirstName = 'Olivia' AND cLastName = 'Olsen'
);
```
