# politician-recommender-system

## Overview

This is a prototype for a politician recommender system. It was created using Flask with SQLite.

The `backup.db` is the database before the system was tested by users. To preserve user's information, `storage.db` will not be updated with theirs ratings for now.

This is the tree structure:

```
app
├── controllers
├── models
├── scripts
│   ├── datasets
│   ├── inserts
│   └── recommenders
├── static
│   └── styles
└── templates
```

The scripts' folder is to insert data into the database if is necessary to reset all the information, all the implementation of information filtering is in `recommenders` folder

The final version will be created in another repo featuring a backend (in Flask as an API) and frontend(using a javascript framework).

## Installation

You need to install the libraries first:

```python
pip3 install -r requirements.txt
```

Then you can initialize the application:

```python
python3 run.py runserver
```