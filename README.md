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

## Check if your server is running properly
Go to `/store`, you will see "Hello, world. Welcome to the Mock Platform"
