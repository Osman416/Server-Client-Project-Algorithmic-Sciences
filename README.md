# Server-Client String Search Project

## Overview

This project consists of a server that searches for strings in a specified file and a client that queries the server for string existence. The server supports SSL connections and is configurable through a configuration file.

## Project Structure

- `Server/` - Contains the server code and tests.
- `Client/` - Contains the client code and tests.
- `data/` - Contains the sample data file.
- `logs/` - Contains the server log file.
- `config/` - Contains the server configuration file.
- `docs/` - Contains project documentation.

## Requirements

- Python 3.8+
- configparser
- pytest
- unittest

## Installation

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the server by editing `config/server_config.ini`.

2. Start the server:

    ```bash
    python Server/server.py
    ```

3. Run the client:

    ```bash
    python Client/client.py
    ```

## Testing

Run the tests using `unittest` and `pytest`:

```bash
pytest tests/