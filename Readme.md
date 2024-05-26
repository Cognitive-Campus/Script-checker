Ai model for checking scripts, takes an image file for containing a single question, and an image file containing its answer, and gives rating. BOTH IMAGES SHOULD BE OF 1 PAGE ONLY.


## How to run

1. Create .env file and fill the environment variables as shown in the .env.example file
2. Also create virtual environment :)
3. Install the requirements defined in requirements.txt file
4. Run the server by `uvicorn main:app --reload --port=8002 --host=0.0.0.0`
5. Hit POST request on "http://localhost:8000/process_images/" with question_img and answer_img as request body



## To make Django api

1. Check.py file is unnecessary, you can ignore it. It is for my use
2. Pipeline.py file contains the full script checker code but it is not made into an API, it runs on terminal.
3. Main.py is the FULL API IN FAST API
4. Config.py is configuration

So, use config and pipeline if you want to create django api
