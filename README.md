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
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `data: [{ id : 1, url: 'https://cdn2.thecatapi.com/images/83r.gif' }]`

<b>Retrieve available categories</b>
  - http://localhost:8000/api/categories/
