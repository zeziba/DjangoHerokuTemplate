# Introdcution
This project supplies a django template that uses serveral differnt technologies to allow for ease of deployment to heroku.

This template is designed with django 4+, python 3.8+ and npm in mind.

- Development environment with Docker-Compose
- Production environment with Heroku
- Static file compulation with django-sass-processor and django-compressor
- Static file serving with whitenoise
- CI with github actions
- VSCode remote container config with several helful tools including black and linting
- A custom user model that uses the email and the username
- Use of npm for these technologies
  - bootstrap5
  - bootstrap-sass
  - sass
  - webpack for compulation of css and js files


## Before use
Install the following onto your dev machine
- Python3.8+
- npm v8+
- git v2+

Navigate to the directory where the project will be stored and create a folder for the project

After creating the folder where the project will be located, create a python virtual environment with the following command

- `python -m venv .env`

Next activate the virtual environment

- `.env/Scripts/activate`

Once the virtual environment is activated then install django and get the template

- `python -m pip install django -y`
- `python -m django --template=https://github.com/zeziba/DjangoHerokuTemplate/zipball/main --extension=py,md <project_name>`

Next using npm install the nessisary files with the following command

Change directory to the correct path
- `cd .\project\static\vendor`

Then install using npm
- `npm install`

## Usage
Once the template is installed by django it is time to set eveything to a running state.

There is a script included in the ./project/scripts file called finalize.dev.sh which will attempt the following

- Flush any databases which currently exists
  - If no database exists it will throw a error that can be ignored as this is just using the built-in manage.py flush command
- Run all makemigrations
  - If during development some migrations do not work properly from a specific app just run the following command
    - `python manage.py makemigrations <app_name>`
- Run migrations
  - As above, if there is an issue with migrations then follow the above with this command
    - `python manage.py migrate <app_name>`
- Create the cache that django will use
- Run the custom initadmin command
  - This command will use the .env file to set up the admin
    - It is possible to refactor this command to setup a group of admin/users but I elave that to the user to figure out

To start the dev container/environment
#### VSCode
Right click the docker-compose.yml and click compose up
- Same for production after the .env.prod file has been created and populated correctly

#### From the command line
Open a commandline and navigate the cwd to the project root folder

Run the following command
- `docker-compose -f docker-compose.yml build`
- `docker-compose -f docker-compose.yml up`

Or just the following one liner
- `docker-compose -f docker-compose.yml up --build`


## Installation is now complete and the template is ready to be used.
