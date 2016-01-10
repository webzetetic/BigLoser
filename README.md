# Biggest Loser App

### Getting Started

1. Clone the repository.
2. `createdb bigloser`
3. In virtual environment `bin/activate` script, add `export DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/bigloser"`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`

## Production Notes

Run this to sync db changes with Heroku:

```
heroku run python manage.py syncdb
```

App homepage on Heroku:
```
https://vast-mesa-4779.herokuapp.com/bigLoser/login/
```

## Requirements

* Administrator Interface
* Contestant Interface

As an Administrator, I want to be able to:

  * View list of registered contestants
  * View contestant personal data*
  * View contestant weight loss target
  * Add/Modify/Delete contestant personal data*
  * Record weigh-ins
  * Send messages to contestants
  * Add/Modify contest rules
  * Upload images/descriptions of available prizes
  * Acknowledge receipt of payments

As a Contestant, I want to be able to:

  * Register to compete
  * Review weight loss target
  * Add/Modify/Delete my personal data*
  * View my registered weigh-ins/progress toward goal
  * Compare my progress against others
  * Send messages to admins/fellow contestants
  * Review contest rules
  * View images/descriptions of available prizes

*height, frame size

## Architecture Diagrams

### mysite

We introduced `mysite` as the "master" Django application to rule them all.
This way `mysite` knows about `register`, `admin`, and `bigLoser`,
but each doesn't need to know about the other.
(That said, some dependencies do currently linger 
until we move some of the `index()` logic up into `mysite`.)

![mysite knows all apps](http://yuml.me/diagram/scruffy/class/%5Bmysite%5D%2B%2B-%3E%5BbigLoser%5D%2C%20%5Bmysite%5D%2B%2B-%3E%5Bregister%5D%2C%20%5Bmysite%5D%2B%2B-%3E%5Badmin%5D)

```
[mysite]++->[bigLoser]
[mysite]++->[register]
[mysite]++->[admin]
```

### Registration

![Registration](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgQmlnTG9zZXIgUmVnaXN0cmF0aW9uCgpVc2VyLT4-dXJscy5weTogL3IAGgVlci8KAA0HLT4-dmlld3M6IAATCF91c2VyCgAQBS0-PnRlbXBsYXRlABYKLmh0bWwKABAILT4-VXNlcjogaHRtbA&s=napkin)

### Index

![Registration](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgQmlnTG9zZXIgSW5kZXgKClVzZXItPj51cmxzLnB5OiAvYgAaBy8KAA0HLT4-dmlld3M6IGkALgVhbHQgYWRtaW4KICAgIAAWBQAZCgAUBV9ob21lcGFnZQAVDXRlbXBsYXRlABURLmh0bWwKZWxzZSB1c2VyAEMUdXNlcgA1IQAYDQBKC25vYm9keQCBGhQAgWQIX2xvZwCBQQ8AgSMLABgFAIEeB25kCgCBPwktPj5Vc2VyOiAAgTsF&s=napkin)

### Admin Creates Contest

![Admin](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgQmlnTG9zZXIgQWRtaW4KClVzZXItPj51cmxzLnB5OiAvYgAaBy9jb250ZXN0L2FkZAoAGActPj52aWV3czogQwAXBkNyZWF0ZS5hc192aWV3KCkKABoFLT4-ABMNOiAAFwoALA0tPj5Vc2VyOiBodG1sCg&s=napkin)
