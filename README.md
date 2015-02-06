# Long Word

## Installation

    pip install -r requirements.txt

if enchant library cannot be found, should be packaged with the install, but that didn't work on my OS-X system.

    OSX : brew install enchant 
    Linux ( Debian ) : apt-get install enchant
    Amamzon Linux:
    - yum install enchant
    - yum install enchant-aspell
    - yum install aspell-en 

### Minimal tasks to setup the server

Setup initialize the DB

    python manage.py migrate

Run unittests

    python manage.py test

Setup Admin user

    python manage.py createsuperuser 

Run server

    python manage.py runserver

Create sample users

    1. Goto http://127.0.0.1:8000/admin
    2. Login as superuser and create sample users via admin interface

Test site by logging in as one of the sample users at the root: http://127.0.0.1:8000

## Pro's and Con's 

### Database Selection

The default database was chosen. It works out of the box and is simple to setup because it doesn't require it's own service.

Most other databases (Postgres, Mysql, MongoDB, Redis, ... ) would also be potential candidates if the business case would have been more complex and the scaling 

or performance requirements stronger.

### UI

The default template engine was chosen for speed purpose and the minimization of unknown gotchas. The tutorials for the default template engine are pretty good.

## Scaling

Since I know that the user base is currently limited and I only have limited time, 
I didn't investigate scaling issues. However, if the business case requires it i would start doing the following: 

Load testing simulating the common use cases at scale should be setup to identify the bottle necks of the application.

Parameters currently to look at scale would be:

1. Number of users
2. Number of valid submissions per user.

The work to make the product scale should be focused on the identified bottle necks.

### Potential bottleneck if number of users grows

The html is dynamically generated, this can be a concern at scale. 

Potential partial solutions that could play part in a solution are:

1. Move html to cdn
2. Dynamic updates via minimal API
3. Cache leaderboard only update in regular intervals ( potentially modify it client side if the client notices that submitted score would be in the leaderboard )

## Exploitation / Security

I should also think more carefully about potential exploits and security concerns.

Request forgery is already prevented via Django's standard mechanism.

Spamming the database with duplicate words is another concern. Preventing the storage of duplicates might be a good option.

## Acceptance Testing

Only parts of the application are tested via unit testing.

At this complexity automatated end to end test would be still good to have; but didn't have the time setup them up. 

Technologies that could play a role: Cucumber , Selenium, etc.

## Algorithm Choices

### Word scoring

Implemented as suggested. Length of characters. Easy to understand for the user and easy to implement

### Word validation

Normalization is first applied so that the scoring and the underlying dictionary gets reasonable strings (without superfluous whitespaces).
The enchant dictionary to check if a word is valid english was found via the google search. It was the one of the first hits.
It seems to fit the requirements. The dependency issues are a bit worrying. In a real production environment I would probably look for alternatives,
that are more predictable during the installation process.

### Highscoring

Currently, highscores are also displayed when the score is equal the highest score. Depending on the user experience one might want to change that. 

