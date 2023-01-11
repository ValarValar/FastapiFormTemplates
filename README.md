# FastapiFormTemplates
## Project Setup     
docker-compose up -d --build    
Filling mongodb with testing data
docker-compose exec form_app python utils/fill_test_db.py    
Run Tests    
docker-compose exec form_app pytest     

todo: update readme    
