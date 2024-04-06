# OB03_Zoo-Management-System

This project, dubbed the "Zoo Management System," is a Python-based application designed to facilitate comprehensive zoo operations.
This project involves creating a web application using the Flask framework to display data from a zoo_data.json file, which contains information about animals and staff in a zoo. The data is presented on a webpage using Bootstrap-styled cards that provide a visually appealing and organized view.

## Key Components:

- Flask Backend: The Flask app serves as the backend. It reads data from a JSON file and passes this data to the frontend.
- HTML and Bootstrap: The frontend utilizes HTML enhanced with Bootstrap for styling. Data about the zoo's animals and staff is displayed in individual cards, offering a clear and structured layout.
- Dynamic Data Rendering: Using the Jinja2 templating engine integrated with Flask, the application dynamically injects data into the HTML, allowing for real-time content updates without needing to reload the entire page.

## Functionality:

- Data Representation:Each animal and staff member is represented as a card that displays relevant information such as name, age, role, etc.
- Web Interface: The user interface is web-based, accessible through a browser, making it user-friendly and easy to navigate.

This approach not only makes the information easily accessible and readable but also allows for flexible updates to the zoo's database, which can be reflected immediately on the webpage without manual intervention.