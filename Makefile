install-deps:
	npm i

rebuild:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d --force-recreate

mm:
	docker-compose exec app ./manage.py makemigrations

migrate:
	docker-compose exec app ./manage.py migrate

shell:
	docker-compose exec app ./manage.py shell_plus

deploy:
	sls deploy

db:
	sls dashboard

test:
	sls invoke -f app -p headers.json

remote-migrate:
	sls invoke -f migrate

remote-migrate-logs:
	sls logs -f migrate
