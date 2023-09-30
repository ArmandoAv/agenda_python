# agenda_python

This project creates an agenda in a json file with an ID, first name, last name and cell phone number. The ID is a number from 1 onwards.

In the project folder create a virtual environment whit the following command:

    python - n venv vnev

Once the virtual environment is created, execute the commands:

    cd vnev\Scripts\
    activate

Install the following libraries:

    pip install click
    pip install -U autopep8

## Execution agenda

Because this agenda is created through the command line, when executing the main program you must be given some option.

For example:

    python cli.py --help

Shows the commands that can be used.

usuarios:

    python cli.py -- usuarios

Shows users saved in the agenda.

actualiza-usuario:

    python cli.py -- actualiza-usuario <id> --nombre <update_first_name>
    python cli.py -- actualiza-usuario <id> --apellido <update_last_name>
    python cli.py -- actualiza-usuario <id> --numero_celular <update_cell_phone_number>
    
You can update one o more data:

    python cli.py -- actualiza-usuario <id> --nombre <update_first_name> --apellido <update_last_name>
    python cli.py -- actualiza-usuario <id> --nombre <update_first_name> --numero_celular <update_cell_phone_number>
    python cli.py -- actualiza-usuario <id> --apellido <update_last_name> --numero_celular <update_cell_phone_number>
    python cli.py -- actualiza-usuario <id> --nombre <update_first_name> --apellido <update_last_name> --numero_celular <update_cell_phone_number>

nuevo-usuario:

    python cli.py -- nuevo-usuario --nombre <new_first_name> --apellido <new_last_name> --numero_celular <new_cell_phone_number>
    
Create a new user, the ID is created automatically.

busca-usuario:

    python cli.py -- actualiza-usuario <id>

Find a user with the ID.

borra-usuario:

    python cli.py -- borra-usuario <id>

Delete a user with the ID.

