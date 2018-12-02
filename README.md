# 3yourmind
3YOURMIND company technical task

Enter project root directory and run the command below:

<b>docker-compose up</b>


# Api doc

<b>Retrieve cats list by tag</b>
  - http://localhost:8000/api/cats/:tag/

<b>Retrieve available categories</b>
  - http://localhost:8000/api/categories/


/**
 * @api {get} /user/:id Request User information
 * @apiName GetUser
 * @apiGroup User
 *
 * @apiParam {Number} id Users unique ID.
 *
 * @apiSuccess {String} firstname Firstname of the User.
 * @apiSuccess {String} lastname  Lastname of the User.
 */
