# downloads_statistics

<h3>How to run:</h3>
<ol>
  <li>cd into the root directory.</li>
  <li>run the command <code>make app</code> to build the app. This will build the containers and execute the first database seeding.</li>
  <li>the application is exposed at <code>http://localhost:8081</code> by default.</li>
</ol>

<h3>Additional info:</h3>
<ul>
  <li>you can run automatic tests with the command <code>make test</code><strong>*</strong></li>
  <li>if you want to seed the database run the command <code>make seed</code><strong>*</strong></li>
  <li>the application features a first implementation of websocket in order to load new data in realtime, this can be tested with the button at the botton of the page, that simulates a download.</li>
  <li>in order to obtain the country where a download has happened, an reverse geocoding API is consumed and the response data is saved to the database not to consume the API everytime the application is used and data is loaded on the map.</li>
</ul>

<strong>*</strong><em>containers must be up and running for this, if they are not run the command <code><strong>docker-compose up -d</strong></code> in the project directory.</em>
