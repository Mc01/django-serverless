test:
	sls invoke -f app -p headers.json

migrate:
	sls invoke -f migrate
