# FastapiFormTemplates
## Task summary    
App database stores form templates like:    
```python
{     
    "name": "Form template name",    
    "field_name_1": "email",    
    "field_name_2": "phone"    
}    
```
Where _email, phone, date, text_ are available datatypes of fields    
Task requires ___POST endpoint /get_form___ receiving parametrized requests such as: ___?f_name1=value1&f_name2=value2___     
where f_name1 is a field name.     
Then it should validate by value one of specified fields' datatype       
There are only 2 types of answer:
- Case 1. Match:     
For our earlier example  __Form template name__ matching input would be:
    - ?field_name_1=hello@mail.ru1&field_name_2=+7 999 999 99 99
    - ?field_name_1=hello@mail.ru1&field_name_2=+79999999999&field_name_3=hi   
- Case 2. No match:     
    - ?field_name_1=username1&field_name_2=28.12.2012     
    - ?field_name_1=hello@mail.ru
    
#### ___Requirements for match are:___
1. Inputed fields names are equal to db template field names and inputed values datatypes (identified by validation) are equal to template datatypes     
2. Input may contain more fields than template in db, but not in reverse way(second example)     
#### ___Endpoint returns:___
- _Template name_ if there is at least one matching. For the first template it would be 'Form template name'     
- dict with _field_name:datatype_ of param value pairs, for ther first No match example it would look like:    
```python
{        
    "field_name_1": "text",    
    "field_name_2": "date"    
}    
```
#### ___Validation:___ ####
Task specifications for data type are:
1. values +7 xxx xxx xx xx is a phone. (for example: +7 999 999 99 99)    
2. values DD.MM.YYYY или YYYY-MM-DD (for example: 12.04.2021, 2020-02-11)    
3. email validation is default     
4. All other values are text    

## Stack
- Fastapi
- Mongodb
- Docker
- Pytest

## Project Setup     
reminder: don't forger to configure your interpreter and activate venv.   
- activate venv    
- pip install docker    
This part you should run from the root directory of the project    
- docker-compose up -d --build    
Filling mongodb with testing data
- docker-compose exec form_app python utils/fill_test_db.py    
Run Tests    
- docker-compose exec form_app pytest     
   
