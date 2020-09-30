# Querytube
Integration of Youtube API with fetching results with updated intervals supporting multiple search queries

How it works:-
1. User registers the search queries. For eg 'football'.
2. The registerd queries are fetched from Youtube Api at regular inteval and update the database.
3. User can view the queries with the order of published video date with support of pagination and also videos related to a particular search-query registered.

How to use:-
1. Make python virtualenv
2. git clone https://github.com/savish28/Querytube.git
3. cd Querytube
4. pip install r - requirements.txt
5. python manage.py runserver
6. python manage.py process_tasks
6. To view the queries registered
   Get request - http://localhost:8000/api/register/
7. To register a search query
   Post request - http://localhost:8000/api/register/
   Input Data - {"query" : "football"}
8. To view videos
    Request type - GET
    http://localhost:8000/api/video/
    Get params supported- 'page' , 'query'
    'page' will contain the page number
    'query' will contain the query_id to view the results related to a single search query
    Not providing 'query' would show the results of all search queries registerd with descending published dates
9. Tasks status is seen in the terminal in which python manage.py process_tasks is executed

How to admin use:-
1. python manage.py createsuperuser
2. Login to http://localhost:8000/admin/
3. All the models/users/task info are stated here

Additional Features:-
1. Supports multiple keys for Youtube API if one of them exhausts daily limit.
2. Django Rest Framework Dashboard to view Api requests
