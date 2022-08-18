-- Deployment required steps ---
-- gilbert tanner written article step wise deploy the file on server

link of the article--
https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku/


step1 - - - Needed files
pip install pipreqs 
pipreqs ./  (cmd after file location)

requirements.txt   
		streamlit==0.79.0
		pandas==1.2.3
		numpy==1.18.5
		matplotlib==3.3.2
		seaborn==0.11.0
		scikit_learn==0.24.1

setup.sh
Procfile


step2- - - initialize
git init (for tracking the our file)


step-3---Create a Heroku Account
Installing the Heroku Command Line Interface (CLI)

https://www.geeksforgeeks.org/introduction-and-installation-of-heroku-cli-on-windows-machine/

step-4---heroku login
heroku login (cmd prompt)


step-5--- Deploy the Application 
heroku create projectName (cmd Prompt)
git add .
git commit -m "some message"
git push heroku master


step-6---Check if it is running
after deployed open url 
heroku ps:scale web=1 (cmd Prompt)
heroku open


