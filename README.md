![enter image description here](https://travis-ci.com/Mcflan-7/P5_OpenFoodFacts.svg?branch=master) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# ✨ OpenFoodFacts ✨

Program that request data from the OpenFoodFacts API, parse and store into a database for offline use, you can then search for a product within different categories and find a substitute with a better nutriscore grade.

This project is in CLI also know as command-line interface, it will be available in a web app interface in the near future.

## Summary 📋

- [Getting started](#getting-started)
- [Installing](#installing)
- [Prerequisites](#prerequisites)
- [Built with](#built-with)
- [Authors](#authors)

## Getting Started 🚀

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure to have Python 3x installed on your computer
Run the following in your command prompt

```
python
```

I used **Python 3.8.0** to built this program, Python 3.0 to 3.8 will work.

### Installing

A step by step that tell you how to get my code up and running :

- Clone my repo

```
git clone https://github.com/Mcflan-7/P5_OpenFoodFacts.git
```

- Set up your virtual environnement (using venv for this example, any will do)

```
python -m venv venv
```

- Activate your virtual environement with

  ```
  Windows: source venv/Scripts/activate
  MacOS: source venv/bin/activate
  ```

- Install the requirement with

```
pip install -r requirements.txt
```

- Create database

```
CREATE DATABASE openfoodfacts CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
```

- Launch installation script

```
python -m install
```

- Launch the programme

```
python -m openfoodfacts
```

## Built With 🛠

- [Python](<[https://www.python.org/](https://www.python.org/)>) - The programming language that lets you work quicklyand integrate systems more effectively
- [VSCODE](<[https://code.visualstudio.com/](https://code.visualstudio.com/)>) - The code editing redefined

## Authors 💻

- **Gaëtan GROND** - _Initial work_ - [GITHUB](<[https://github.com/Mcflan-7](https://github.com/Mcflan-7)>)
