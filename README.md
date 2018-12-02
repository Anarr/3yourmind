# 3yourmind
3YOURMIND company technical task

Enter project root directory and run the command below:

<b>docker-compose up</b>


# Api doc

<b>Retrieve cats list by tag</b>

* **URL**

  http://localhost:8000/api/cats/black

* **Method:**

  `GET`
  
*  **URL Params**

   limit

   **Required:**
 
   `tag=[string]`
   
   **Optional:**
 
   `limit=[int]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `data: [{ id : 1, url: 'https://cdn2.thecatapi.com/images/83r.gif' }]`

<b>Retrieve available categories</b>
* **URL**

  http://localhost:8000/api/categories

* **Method:**

  `GET`
  
*  **URL Params**

   limit
   
   **Optional:**
 
   `limit=[int]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `data: [{ id : 1, name: 'boxes' },{ id : 2, name: 'hats' }]`
    

<b>Run tests</b>
  - docker-compose run web python manage.py test



