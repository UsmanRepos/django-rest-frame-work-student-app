# Students Management App
This is a Django web application that allows you to manage and view a collection of students.

## Features
* Register view for creating new student accounts
* Login view for existing student accounts
* StudentViewSet for viewing a list of students with pagination
* Custom action for setting a password for a student account
* Custom action for viewing recent users
* Serializers for data validation
* Authentication and permission classes for secure data access

## Prerequisites
You will need to have the following installed on your local machine:
* Python 3.x
* Django 
* Django Rest Framework

## Installation
1. Clone the repository <br>
``` git clone https://github.com/UsmanRepos/django-frame-work-student-app.git ``` <br><br>
2. Install the required packages <br>
``` pip install -r requirements.txt ``` <br><br>
3. Run migrations <br>
``` python manage.py migrate ``` <br><br>
4. Run the development server  
``` python manage.py runserver ``` <br><br>

## Views
The API includes the following views:
* Register: Allows users to register for the service.
* Login: Allows users to log in to the service.
* StudentViewSet: Allows users to view a list of students with pagination.

## Serializers
The API uses the following serializers:
* RegisterSerializer: Validates user registration data.
* LoginSerializer: Validates user login data.
* StudentSerializer: Validates student information.
* PasswordSerializer: Validates password change data.

## Pagination
The API uses the StandardResultsSetPagination class for pagination with a default page size of 3 and options for custom page size and max page size.

## Custom Actions
The StudentViewSet includes the following custom actions:
* set_password: Allows users to change their password.
* recent_users: Allows users to view a list of recent users.

## Authentication and Permission Classes
The API utilizes the IsAuthenticated permission class to ensure secure data access.

## Customizing
The code in this repository is meant to be a starting point for a more comprehensive student management system. To customize the API to meet your needs, you can:
* Add additional fields to the Person and Student models
* Add additional views and actions to the StudentViewSet
* Add additional serializers for data validation
* Customize the authentication and permission classes to better suit your needs

## Contributing
Contributions are welcome! If you would like to contribute to this project, you can start by forking the repository



