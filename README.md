# Rick & Morty API

# Build and run api
```bash
docker-compose up -d
```

# Init db
```bash
docker exec -it rickmorty-api poetry run rick_morty/scripts/db.py
```

# Run test
```bash
docker exec -it rickmorty-api poetry run pytest tests
```

# Openapi docs
http://<your_ip_address>:8000/docs

# Remove app 
docker-compose down
docker volume rm rick-morty_pgdata