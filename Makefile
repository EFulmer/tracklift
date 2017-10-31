DATABASE := "tracklift"
DB_DIR := "$(HOME)/pgsql/data/"
ENV_NAME := "tracklift"
INIT_SCRIPT := "schema.sql"
MAIN_FILE := "main.py"
TEST_SCRIPT := "test.sql"

.PHONY: start-db create-db populate-db start-app
start-db:
	pg_ctl -D $(DB_DIR) start

create-db:
	psql --file=$(INIT_SCRIPT) $(DATABASE)

populate-db:
	psql --file=$(TEST_SCRIPT) $(DATABASE)

start-app:
	source activate $(ENV_NAME)
	python $(MAIN_FILE)
