# Distributed-Ledger-Technology


## Code Explanation

**dlt.py**: This file contains the `DLT` class, which handles all the logic for the distributed ledger technology, including block creation, adding new data, the proof of authority (PoA) mechanism, and consensus to resolve conflicts.

**node.py**: This file sets up the Flask server and defines the endpoints to interact with the DLT. It includes routes for mining new blocks, adding new transactions, retrieving the full chain, registering new nodes, and resolving conflicts.

**app.py**: This file runs the Flask application defined in `node.py`. It is designed to start the server when executed.

## Deployment and Execution

To run this project, follow the steps below:

1. Create a folder named `dlt_project` and place the files `dlt.py`, `node.py`, and `app.py` in it.

2. Ensure you have Flask and Requests installed:

    ```bash
    pip install Flask requests
    ```

3. Run the server by launching `app.py`:

    ```bash
    python app.py
    ```

This will start a Flask server at `http://localhost:5000`, where you can interact with your DLT via the defined endpoints.

## Endpoint Usage

- **Mine a new block**: `GET /mine`
- **Create a new transaction**: `POST /transactions/new`
- **Return the full blockchain**: `GET /chain`
- **Register new nodes**: `POST /nodes/register`
- **Resolve conflicts**: `GET /nodes/resolve`

Use tools like Postman or curl to interact with your DLT via the provided APIs. This modular structure makes the code more flexible and maintainable.
