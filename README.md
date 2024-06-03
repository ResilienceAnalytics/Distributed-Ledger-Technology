# Distributed-Ledger-Technology

## Deployment and Execution Instructions

1. Create a folder named `dlt_project` and place the files `dlt.py`, `node.py`, `app.py`, and `models.py` inside it.

2. Ensure you have Flask, Requests, and SQLAlchemy installed:

    ```bash
    pip install Flask requests SQLAlchemy
    ```

3. Run the server by launching `app.py`:

    ```bash
    python app.py
    ```

This will start a Flask server at `http://localhost:5000`, where you can interact with your DLT via the defined endpoints.

## Endpoint Usage

- **Mine a new block**: `GET /mine`
  
  Example:
  ```bash
  curl http://localhost:5000/mine
  ```

- **Create a new transaction**: `POST /transactions/new`
  
  Example:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{
    "users": "user1",
    "data": [],
    "dh_parameters": "param",
    "server_public_key": "server_key",
    "receiver_public_key": "receiver_key",
    "sender_public_key": "sender_key"
  }' http://localhost:5000/transactions/new
  ```

- **Return the full blockchain**: `GET /chain`
  
  Example:
  ```bash
  curl http://localhost:5000/chain
  ```

- **Register new nodes**: `POST /nodes/register`
  
  Example:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{
    "nodes": ["http://localhost:5001"]
  }' http://localhost:5000/nodes/register
  ```

- **Resolve conflicts**: `GET /nodes/resolve`
  
  Example:
  ```bash
  curl http://localhost:5000/nodes/resolve
  ```

You can use tools like Postman or curl to interact with your DLT via the provided APIs. This modular structure and the use of a database make the code more flexible, maintainable, and robust.

## Utility

1. **Persistence of Data**:
   - **Durable Storage**: The data is stored persistently, ensuring that it is not lost when the server restarts or shuts down.
   - **Recovery**: Blocks and other information can be easily retrieved even after system downtime.

2. **Efficient Data Management**:
   - **Efficient Queries**: Databases are optimized for performing complex queries efficiently, allowing for fast search and retrieval of stored information.
   - **Indexing**: Databases can index data to speed up searches.

3. **Data Integrity**:
   - **Transactions**: Relational databases like SQLite use transactions to ensure data integrity, allowing complex operations to be performed atomically.
   - **Constraints**: Databases can enforce constraints on data, such as primary and foreign keys, to ensure data consistency and validity.

4. **Scalability**:
   - **Handling Large Data Volumes**: Databases are designed to handle large amounts of data efficiently.
   - **Easy Extension**: It is easier to add new features and tables to extend the system without refactoring the entire codebase.

5. **Security**:
   - **Access Control**: Databases can provide access control mechanisms to ensure that only authorized users can access or modify the data.
   - **Backup and Restore**: Databases offer backup and restore mechanisms to protect data from loss.



