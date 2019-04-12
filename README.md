# ReST API for the Nutrition Diary app

For the actual application's code, please see
[habiib4's nutrition-diary repository][1]. The ReST API served via this
repository aims to conform to the one provided by [Nutritionix][2] on a
freemium basis.

[1]: https://github.com/habiib4/nutrition-diary
[2]: https://www.nutritionix.com


## API endpoints

For the current version of the API (v1), the following endpoints are
available:

- *GET* `api/v1/list`:  
Lists all the nutrition data currently in the database.

- *GET* `api/v1/search/<term>/`:  
Lists all the nutrition data for the foods matched by the search term
`<term>`.

Note that both these endpoints support an additional parameter `limit`,
which limits the number of items listed. For example:

```
$ GET api/v1/list/?limit=5
```

```
$ GET api/v1/search/rice/?limit=5
```
