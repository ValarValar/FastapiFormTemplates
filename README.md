# FastapiFormTemplates
todo: update readme
## Project Setup     
reminder: don't forger to configure your interpreter and activate venv.   
- activate venv    
- pip install docker    
- 
This part you should run from the root directory of the project    
- docker-compose up -d --build    
Filling mongodb with testing data
- docker-compose exec form_app python utils/fill_test_db.py    
Run Tests    
- docker-compose exec form_app pytest     

todo: update readme    
