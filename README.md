# Interview Management System

![Project Logo](/path/to/your/logo.png) <!-- Replace with your project's logo or image -->

A modern and efficient system for managing interviews and candidates in your organization.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Interview Management System is a web application designed to streamline the interview process, making it easier to manage candidates, interviewers, and interview schedules. It offers a user-friendly interface to help HR personnel and interviewers efficiently conduct interviews.

## Features

- User authentication and authorization system.
- Interviewer management for assigning and managing interviewers.
- Scheduling and tracking interviews with status updates.
- RESTful API to provide external systems and user interfaces access to core system functionalities. The API includes proper documentation and versioning and offers endpoints for various actions
- Cool API Documentation

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Django (latest version)
- PostgreSQL (or your preferred database)
- Git (optional, for cloning the repository)

<h2> Installation </h2>
<ol>
  <li>Clone the repository: <br/>https://github.com/GalkaKG/interview_management_system.git </li>
  <li>Set up a virtual environment (optional, but recommended) <br/>pip install virtualenv<br/>cd interview_management_system<br/>virtualenv venv
  <br/>- On Windows:<br/>venv\Scripts\activate<br/>- On macOS and Linux:<br/>source venv/bin/activate
  <li>Install project dependencies: <br /> pip install -r requirements.txt
  </li>
  <li>Set up environment variables</li>
  <li> Apply database migrations: <br /> python manage.py makemigrations <br> python manage.py migrate
  </li>
  <li>Create a superuser (optional) <br /> python manage.py createsuperuser </li>
  <li>Run the development server: <br />python manage.py runserver</li>
</ol>


<h2> Technologies Used </h2>
<ul>
  <li>Django</li>
  <li>Django Rest Framework</li>
  <li>PostgreSQL </li>
  <li>RabbitMQ</li>
  <li>HTML, CSS, JavaScript</li>
</ul>
