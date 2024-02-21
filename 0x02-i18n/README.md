# Description

This folder has code on how to write i18n.
Basically a way to auto translate one language into another.
Although its for Flask.

### Packages

Run this: `pip3 install flask_babel flask`

### Running pybabel

1. Create the following in `babel.cfg`
```txt
[python: **.py]
[jinja2: **templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

2. Init the translations with:
`pybabel extract -F babel.cfg -o messages.pot .`

3. Init dictionaries:
`pybabel init -i messages.pot -d translations -l en`
`pybabel init -i messages.pot -d translations -l fr`

4. Then manually edit the `messages.po` file with the correct value:

|msgid | English | French|
|---|---|---|
|home_title | "Welcome to Holberton" | "Bienvenue chez Holberton"|
|home_header | "Hello world!" | "Bonjour monde!"|

5. Then compile translation files:
`pybabel compile -d translations`

### Testing the app

#### You can force the locale with the URL parameter
`http://localhost:5000/?locale=fr|en`

