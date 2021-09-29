# SmallCase

This the assignment project for the SmallCase QA Engineer, based on Selenum webdriver with Python.

## Project Structure
Here you can find a short description of main directories and it's content
- [locators](locators) - there are locators of web elements in locators.py grouped in classes
- [pages](pages) - there are sets of method for each test step 
- [tests](tests) - there are sets of tests for main functionalities of website
- [log_listener](log_listener) - all the logs generated are kept here.

## Project Features
- framework follows page object pattern
- logger has been implemented in each step of test cases.

## Run Automated Tests

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow.

## Getting Started

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Bugs Doc

The Bugs for the SmallCase has also been uploaded.
