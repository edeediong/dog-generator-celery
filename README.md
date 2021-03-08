# GenDog™
An application that utilizes a task scheduler and a message broker for fetching dog pictures.

## PREREQUISITES
- virtualenv
- rabbitmq-server

*Install virtualenv*


    sudo pip install virtualenv

*Install and set up rabbitmq-server*


    sudo apt-get install rabbitmq-server
    sudo rabbitmq-server -detached
    
    sudo rabbitmqctl add_user myuser mypassword 
    sudo rabbitmqctl add_vhost myvhost 
    sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

*Here’s the structure of our project*


    .
    ├── app.py
    ├── routes.py
    ├── static
    │   └── css
    │       └── main.css
    ├── templates
    │   └── template.html
    ├── test.db
    ├── .env
    ├── requirements.txt
    └── url.txt

*Activate virtual env and install requirements*


    virtualenv gen_dog
    source gen_dog/bin/activate
    
    pip install -r requirements.txt 

*Create a `.env` file and within our .env file, we write important environmental variables*


    CELERY_BROKER_URL=amqp://myuser:mypassword@localhost/myvhost
    CELERY_BACKEND_URL=db+sqlite:///test.db


## Starting the App

*Within the virtual environment, type this into your terminal*


    celery -A app worker -l info

*Then, open a new terminal, activate the virtual env and start flask*


    source gen_dog/bin/activate
    flask run
