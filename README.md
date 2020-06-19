# VAV-BE
Visa 2020 Hackathon Project (BE Repository)

## Create a Virtual Environment
### Mac OS

```
virtualenv env
```
or 
```
python3 -m venv env
```

### Windows
```
py -m venv env
```
You will have a new python virtual environment in your directory called **env**

## Activating a Virtual Environment
### Mac OS
```
source env/bin/activate
```
### Windows
```
.\env\Scripts\activate
```

## Check which virtual environment you have activated
### Mac OS
```
which python
```

### Windows
```
where python
```

## Install Requirements
```
pip install -r requirements.txt
```
## Run Django Server

```
python manage.py runserver
```

## Setting up your own local DB
Go to settings.py and change the 'DATABASE' settings with this format:
```
DATABASES = {
    'default': {
        'NAME': 'xxx',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx',
        'PORT': 'xxx',  
        'OPTIONS': {
          'autocommit': True,
        },
    }
}
```


## Making Migrations
Run the make migration command after making changes to the model (since we only have one app called mockplatform):
```
	python manage.py makemigrations mockplatform
```
Run the latest migrations by running this command in your terminal:
```
	python manage.py migrate
```
You should see the migrated model in your database

## Check if your server is running properly
Go to `/store`, you will see "Hello, world. Welcome to the Mock Platform"
