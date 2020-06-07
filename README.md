# letterboxd-watch-progress

My goal is to average watching one film a day for the entire year. The purpose of this small project is to track the progress of watched films for the current year to date. 

Use React + Chart.js for the frontend and a Flask server to scrape my Letterboxd diary page to get my logged entries. Using this I plot a chart with two lines: an average line for watching one film a day, and a line for the number of films I have actually watched. 

Above the chart are three status boxes stating:

1. The current day of the year
2. The number of films I have watched so far
3. Whether I'm ahead or behind and by how much

I use a cronjob to fetch my diary entries at 5am every morning, the cronjob is not included within this repository but can easily be added using `crontab -e` on Mac/Linux with the following line `00 05 * * * <python_path> <path_to_project>/letterbox/api/letterboxd.py`.

## Personalising the data
In `letterboxd/api/letterboxd.py` change the value of `username` to your Letterboxd username.

## Running the app
First build the React project using `yarn build`. Then start the Flask api with `yarn run start-api` and run the React app with `serve -s build`. To view the project navigate to `localhost:3000` or whichever URL the `serve` tells you the app is available at.
