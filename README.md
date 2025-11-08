# bird tracker mobile app

Author: Bryan Cromabach

Purpose: track the activity of birds

# running the backend
1. open a terminal and open bird_tracker_server
2. start virtual environment:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate
3. run "pip install -r requirements.txt"
4. run "python -m src"
5. when asked if you want to populate the database press "y" then enter but you only need to do this once on every other time you are prompted to populate database pres "n" then enter. You will automatically start the api afterwards.

# running the frontend

1. open a terminal and open bird_tracker_client
2. run "npm install"
3. Find your local IPv4:
   - Windows: ipconfig
   - Mac/Linux: ifconfig | grep inet
4. Add it to .env:
   API_URL=http://(your-ip):3000
5. download expo go on your phone and log in
6. Run Expo from pc terminal:
   "npm run start"
7. scan QR code in terminal to get directed to the expo app

# demo
once both frontend and backend are working simply play around with the demo on the expo go app. The speaker icon is the only location currently and once you click on the icon it will take you to the statistics page where you can chose the different graphs you want to view or go back to the map.

# testing
I have tests for the indetifier and the database in the backend which are the core features that make the app run. Because I have to populate the database manually the test for the database should be run before populating the database because the population function randomises the data in the database.

How to run the tests:

1. open a terminal and open bird_tracker_server
2. start virtual environment:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate
3. run "pip install -r requirements.txt"
4. run "pytest tests/test_identifier.py" and "pytest tests/test_database.py"
