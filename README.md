# Biggest Loser App

## Dev Notes

Run this to sync db changes with Heroku:

```
heroku run python manage.py syncdb
```

Add to venv/bin/activate file to use SQLite for dev

```
DATABASE_URL="sqlite:////Users/thall/Projects/BigLoser/db.sqlite3"
export DATABASE_URL
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
