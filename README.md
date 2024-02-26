# Conventional commit messages
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

commit type:
fix: -> fixes bug in codebase
feat: -> new feature to the codebase
refactor: -> a code changes that neither fixes bug neither creates new feature
perf: -> increases performances
style: -> code changes that do not affect meaning of code (white-space, formatting, missing semi-colons, etc)
build: -> changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)

## Steps to deploy flask app to the render

- Create an Procfile
```web: gunicorn app_file_name:app```
- example: ```web: gunicorn main:app ```
- Put all dependencies in ```requirements.txt``` file
```
  Bootstrap_Flask==2.2.0
  Flask_CKEditor==0.4.6
  Flask_Login==0.6.3
  Flask-Gravatar==0.5.0
  Flask_WTF==1.2.1
  WTForms==3.0.1
  Werkzeug==3.0.0
  Flask==2.3.2
  flask_sqlalchemy==3.1.1
  SQLAlchemy==2.0.25
```

- Create a web service on render
- Create a postgres db on render with same origin
- In environment variable of web service ```SQLALCHEMY_DATABASE_URI```
- replace ```postgres``` to ```postgresql```