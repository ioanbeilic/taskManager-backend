# FastAPI + SQLAlchemy + Alembic

### Building the Project
- We can start building our projects by running `docker-compose build`
- One build is done, run `docker-compose up` to start the services. Leave this terminal open to check the logs.
- To stop the services you can press `Ctrl + C` - (Control + C)

### Export requirements txt
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Commands
- To Generate the Migration From Model
```
docker-compose run fastapi-service /bin/sh -c "alembic revision --autogenerate -m "create my table table""
```
- To Apply the Migration to Database
```
docker-compose run fastapi-service /bin/sh -c "alembic upgrade head"
# for database error run query CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```
 
- To Revert last applied migration
```
docker-compose run fastapi-srvice /bin/sh -c "alembic downgrade -1"
```

# Accessing the Applications
- FastAPI Application Status [http://localhost:8000](http://localhost:8000)
- API Documentation [http://localhost:8000/docs](http://localhost:8000/docs)
- Database Access [http://localhost:8080](http://localhost:8080) - use the above detail to login.
- Mailpit [http://localhost:8025](http://localhost:8025)
