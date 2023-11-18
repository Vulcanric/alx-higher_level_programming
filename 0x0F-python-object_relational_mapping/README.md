## Python - Object Relational Mapping
This project was done to get familiar with **Object Relational Mapping** uses these libraries:

| **Library used** | **Functionalities** |
| ---------------- | ------------------- |
| MySQLdb | Allows one to write SQL queries within a Python file to communicate to a database |
| SQLAlchemy | Allows one to communicates with the database within a Python file, but ***NO MORE QUERIES!*** |

### Use case of both Libraries
Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
