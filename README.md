## create a virtual env

```commandline
python -m venv venv
```

## switch to virtual env

```commandline
. venv/bin/activate
```

## install dependencies

```commandline
pip install fastapi uvicorn
```

## run development server

```commandline
uvicorn <FILE_NAME>:app --reload
```

