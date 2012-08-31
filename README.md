# InviteMe #

InviteMe is a simple Python Flask app that accepts POST requests to store to 
a sqlite3(or MySQL/Postgres) database. This was used to collect emails to send out
invitation codes, hence the name. 

The app itself renders a validated form and waits for POST requests. You can embed
the form into your webpage with an iframe. Json responses for jQuery forms coming soon.

## Install ##

1. Clone:

        git clone git://github.com/alfg/inviteme.git

2. Setup virtualenv:

        cd inviteme
        virtualenv env
        . env/bin/activate

3. PIP Install Deps:

        pip install -r requirements.txt

4. Configure DB URI in inviteme.py:

        DB_URI = 'sqlite:////path/to/file.db'
        
    or for mysql:
    
        DB_URI = 'mysql://username:password@server/db'

5. Run Dev Server:
        
        python inviteme.py

6. View in browser:

        http://localhost:5000

7. Embed into your webpage:

        <iframe src="http://url" frameborder=0 width="100%" scrolling="no" allowtransparency="true"></iframe>

8. Customize template HTML and CSS:
        
        vim templates/form.html

You can use the builtin server during development, but you should use a full wsgi deployment option
for production applications. Refer below for a basic Gunicorn and Nginx configuration.


## Deploying with Gunicorn and Nginx ##

Coming soon!


## TODO ##

- Add support for Ajax JSON requests
