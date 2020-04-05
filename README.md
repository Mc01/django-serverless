# Django-Serverless
Django, Docker and Serverless on Lambda.

## Requirements
To work with this repo you should have preinstalled:
* Docker Desktop
* Serverless Framework
* Node Package Manager
* Make

## Setup
Change `service`, `app` and `org` values in:
```
nano serverless.yml
```

Fill in secrets
```
cp .env.sample .env && nano .env
```

Set the same secrets in Serverless Dashboard
```
make db
```

Install deployment deps
```
make install-deps
```

## Development

For local development
```
make rebuild
```

For Django shell
```
make shell
```

For running migrations
```
make migrate
```

## Deployment

For remote deployment
```
make deploy
```

For remote migrations
```
make remote-migrate
make remote-migrate-logs
```
