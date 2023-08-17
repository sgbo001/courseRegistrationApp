# courseRegistrationApp - Course Module Application

Cloud-Based Project for Group 4

The Course-Module application is an application that facilitate various aspects of course and module management. Its primary functionalities include the seamless addition of courses, the association of courses with specific modules, and the provision for registered users to enroll or withdraw from modules.

# Development Environment

Home Page : <https://c2063081.azurewebsites.net/>

Admin Page : <https://c2063081.azurewebsites.net/admin/>

Azure Function to generate report : <https://func-report-4.azurewebsites.net/api/report?> . This can also be acess via Generate Report navigation bar when logged in as super user on the website.

Django REST API : <https://c2063081.azurewebsites.net/book_api/>. This can also be access via E-Library in Navigation bar of the website.

Admin Username : admin

Admin Password : password123@

# Environment Variables

AZURE_DB_NAME='moduleapp'

AZURE_DB_HOST='c2063081.mysql.database.azure.com'

AZURE_DB_PORT='3306'

AZURE_DB_USER='c2063081'

AZURE_DB_PASSWORD='June0620@'

SECRET_KEY = ZgJIlR5ZhB


# Models Implemented 

Course : This model is reponsible for course registration

Module : This model handles module registration

RegisteredUser : This model handles registered user of a module

Student : This model handles student profile

Learning : This model handles learning material for each module


# Features

User Registration and Account Creation:
The application allows students to conveniently create user accounts, providing a streamlined process for user registration.

Admin Dashboard:
An administrative dashboard is available to super user, enabling efficient oversight and management of the application's functionalities.

Course-Module Association:
Users can easily view and access modules that are associated with specific courses, enhancing the clarity and accessibility of educational content.

Login and Logout Mechanism:
The application features a robust login system, ensuring secure user authentication and facilitating seamless logout procedures.

Student Profile Page:
Students are presented with personalized profile pages that display  details and profile pictures as outlined within the Student model.

Module Enrollment and Withdrawal:
Upon successful login, registered users gain the ability to enroll in or withdraw from modules.

Password Reset Functionality:
Users are equipped with the capability to reset their passwords through secret key created when creating an account.

Enhanced Learning Model:
The application incorporates a  learning model that showcases learning materials specific to modules in which a user is enrolled.

Django REST API: 
Book Finder API to find books by title, author, in Computing. This can be access when you clicked on "E-Library" on the navigation bar

Azure Functions Functionality: 
This functionality queries the Azure MySQL database to gather detailed information about each registered user, including their username, first name, last name, email address, the specific module they are registered for, registration date, and export to excel. This is triggered when user logged in as super user, and click generate report on the naviagation bar. By executing this Azure Function, Administrator can efficiently obtain a consolidated view of registered users, their associated modules, and the corresponding registration dates, streamlining data analysis and reporting processes.


## Installation

1. Open Terminal
2. Check whether Python and Django-admin is installed
    
     ```sh
     python --version
     ```
     ```sh
     django-admin --version
     ```
3. If you don't have them installed, Visit the official Python website at <https://www.python.org/downloads/> to download the latest version of Python. After installing Python, open your treminal and type the below:
     ```sh
     python -m pip install Django
     ```
4. Clone the Repository
    ```sh
     git clone https://github.com/sgbo001/courseRegistrationApp.git
     ```
5. Create a Virtual Environment
    ```sh
     python -m venv myenv
     ```
6. Activate the virtual environment
   - On Windows
   ```sh
     myenv\Scripts\activate
     ```
   - On Windows
   ```sh
     myenv\Scripts\activate
     ```
8. Install Dependencies
   - cd your_project_directory
   ```sh
     pip install -r requirements.txt
     ```
9. Run Migrations
   ```sh
     python manage.py makemigrations
     ```
   ```sh
     python manage.py migrate
     ```
10. Create Superuser
    ```sh
     python manage.py createsuperuser
     ```
11. Run Development Server
    ```sh
     python manage.py runserver
     ```
12. Open your web browser and navigate to http://127.0.0.1:8000/ to access your Django application. You can also access the admin panel at http://127.0.0.1:8000/admin/.

# Contributors

- [Adetoyese Olaide](https://github.com/sgbo001)
- [Oluwole Tobi](https://github.com/metobi1)
- [Ekpedo, Obianuju](https://github.com/Cyngith33)
- [Omire-oluedo, Chinenye](https://github.com/chinnyo)
