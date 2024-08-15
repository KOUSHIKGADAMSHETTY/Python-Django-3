Simple Interest Calculator
Overview
This Django project is designed to calculate simple interest based on user input. It provides a straightforward web interface where users can input the principal amount, rate of interest, and time period. The project then calculates the simple interest using the formula:

Simple Interest
=
𝑃
×
𝑅
×
𝑇
100
Simple Interest= 
100
P×R×T
​
 

where 
𝑃
P is the principal amount, 
𝑅
R is the rate of interest, and 
𝑇
T is the time period in years.

Features
User Input: Users can input the principal amount, annual interest rate, and time period.
Calculation: The project performs the simple interest calculation based on the provided inputs.
Results Display: The calculated simple interest is displayed on the result page.
Implementation
Django Setup:

The project includes a Django app with a form for user input.
URLs are configured to handle requests for both the input form and result display.
URL Configuration:

The project includes a URL pattern to direct users to the form for input and another to display the calculated result.
Views and Templates:

A view handles the form submission and performs the interest calculation.
Templates are used to render the form and display results in a user-friendly manner.
Usage
Navigate to the input form page.
Enter the principal amount, interest rate, and time period.
Submit the form to see the calculated simple interest displayed on the results page.
This project demonstrates the basics of form handling, URL routing, and simple arithmetic operations in Django, making it an ideal starting point for beginners looking to learn Django fundamentals.

