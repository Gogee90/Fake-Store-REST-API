# Fake Store REST API
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<p>
  <p align="center">
    Fake Store based on the "Fake Store API"
    <br />
    <a href="https://github.com/Gogee90/-"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Gogee90/-/issues">Report Bug</a>
    <a href="https://github.com/Gogee90/-/pulls">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

I built this API because i was not satisfied with other other api's found on the internet
due to the limitations.
I needed to be able to create, update and remove records from database.
!!!<strong>WARNING</strong>!!! As it's still work in progress!

### Demo
At the moment you can add new products, update and delete those but you need to be authorized.
Just head to the login page.
<strong>Login: testuser</strong>
<strong>Password: fakestore</strong>
You can use as you like but don't overstay your welcome :)
[Demo](https://distracted-easley-826ab7.netlify.app/)

### Built With
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Dj-Rest-Auth](https://github.com/jazzband/dj-rest-auth)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


## Usage
Don't forget to create and activate virtual environment.
If you want to deploy it on your server you need to do the following steps:
* [download](https://github.com/Gogee90/Fake-Store-REST-API) or clone this repo:
  - Clone with SSH:
  ```
    git@github.com:Gogee90/Fake-Store-REST-API.git
  ```
  - Clone with HTTPS
  ```
    https://github.com/Gogee90/Fake-Store-REST-API.git
  ```
- Install requirements:
If you're on linux:
``` pip3 install -r requirements.txt ```
On windows:
``` pip install -r requirements.txt ```
- Then:
```python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser your_username
To get things up and running:
python manage.py runserver
```
Now get to the interesting part.

It's up to you what you're going to use to manipulate data.
I used axios and i'm 100% sure you can use fetch if you feel more comfortable with it.

- To get all products
```https://gogee90.pythonanywhere.com/api/products/```
- To get a single product for example:
```https://gogee90.pythonanywhere.com/api/products/47```
- All product categories:
```https://gogee90.pythonanywhere.com/api/category/```
- A single product category:
```https://gogee90.pythonanywhere.com/api/category/1```
- Get comments to the corresponding products:
```https://gogee90.pythonanywhere.com/api/comments/15```
- Get a list of users and products added by them:
```https://gogee90.pythonanywhere.com/api/users/```
- Get a single user:
```https://gogee90.pythonanywhere.com/api/users/2```
- Get all carts:
```https://gogee90.pythonanywhere.com/api/carts/```
- Get a single cart:
```https://gogee90.pythonanywhere.com/api/carts/single/1```
- Get all carts added by user:
```https://gogee90.pythonanywhere.com/api/carts/1```
- In order to perform actions on the database you need to be authorized:
```https://gogee90.pythonanywhere.com/api/'dj-rest-auth/login```
To login you need to provide username and password, the response will return a token.
You can store it in, for instance, in the localStorage.
Use that token to use methods PUT, DELETE and POST.

The example of usage.
- To perform a simple GET request:
```
axios.get(`https://gogee90.pythonanywhere.com/api/products/47`)
  .then(response => {
      console.log(response)
  })
```
- To perform a POST request:
``` 
#To upload an image you need to use FormData();
let formData = new FormData()
formData.append('category', category)
formData.append('description', description)
formData.append('id', product_id)
formData.append('image', image)
formData.append('price', price)
formData.append('title', title)
axios.post('https://gogee90.pythonanywhere.com/api/products/', formData, {
  headers: {
    'Authorization': 'Token your_token',
  },
}).then((response) => {
    console.log(response)
}).catch(err => {
    console.log(err)
})
```
- To perform a PUT request:
```
let formData = new FormData()
formData.append('category', category)
formData.append('description', description)
formData.append('id', product_id)
formData.append('image', image)
formData.append('price', price)
formData.append('title', title)
axios.put(`https://gogee90.pythonanywhere.com/api/products/47`,formData, {
  headers: {
    'Authorization': 'Token your_token',
  },
 }).then((response) => {
      console.log(response)
  }).catch(err => {
      console.log(err)
  })
```
- To perform a DELETE:
```
axios({
  method: 'delete',
  url: `https://gogee90.pythonanywhere.com/api/products/47`,
  headers: {
    'Authorization': `Token your_token`
  },
}).then(response => {
  console.log(response)
})    
```            

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Igor Nikolaev - [linkedin-url](https://www.linkedin.com/in/igor-nikolaev-orenburg/) - gogee09@gmail.com

Project Link: [https://github.com/Gogee90/Fake-Store-REST-API/blob/master/README.md](https://github.com/Gogee90/Fake-Store-REST-API/blob/master/README.md)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Dj-Rest-Auth](https://github.com/jazzband/dj-rest-auth)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/Gogee90/Fake-Store-REST-API/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/igor-nikolaev-orenburg/
[product-screenshot]: https://skr.sh/i/280920/xIs13n58.jpg?download=1

