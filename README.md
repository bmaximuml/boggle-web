# Letter Shuffle Game

This is a web based game created using Flask and Bulma.

4x4 boards of letters are generated and players can try to find as many words as possible in a set time. 

Users can play together remotely by entering the same key. 

### Management

This template uses SASS. After making changes to `static/sass/sass_styles.scss`,
run the command `sass --no-source-map sass/sass_styles.scss:sass_styles.css` to
regenerate the `static/sass_styles.css` file, which is looked at by the
application.

Make sure to specify the `FLASK_SECRET_KEY` environment variable
