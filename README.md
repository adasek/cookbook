### Sample Cookbook Python API

This API uses poetry to manage dependencies.
Alternatively, you can use pip to install the dependencies using requirements.txt.

## Installation
```bash
poetry install
```

## Run
```bash
poetry run python3 run.py
```

## Testing
After running the server, you can test the API using curl.

```bash
curl -X GET http://10.0.1.40:5000/recipe
```
