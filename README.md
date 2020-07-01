# downloads_statistics

guide to run:
1) cd into the root directory
2) run the command <code>make app</code> to build the app. This will build the containers and execute the first database seeding.
3) the application is exposed at <code>http://localhost:8081</code> by default

- you can run automatic tests with the command <code>make test</code><strong>*</strong>
- if you want to seed the database run the command <code>make seed</code><strong>*</strong>
- the application features a first implementation of websocket in order to load new data in realtime, this can be tested with the button at the botton of the page, that simulates a download
- in order to obtain the country where a download has happened, an reverse geocoding API is consumed and the response data is saved to the database not to consume the API everytime the application is used and data is loaded on the map.

<strong>*</strong><em>containers must be up and running for this, if they are not run the command <code>docker-compose up -d</code> in the project directory</em>
