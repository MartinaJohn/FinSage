
# FINSAGE- AI for solving economic downturns

The goal of our project is to apply AI to forecast and lessen the effects of economic downturns. 

# Sceenshots
<img src='Screenshot 2023-11-21 003121.png'>





## API Reference

#### Forecaster

```http
  POST api_name: /forecaster
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Ticker` | `Character` | **Required** |
| `Date` | `Int` | **Required** |
| `n_weeks` | `Int` | **Required** |
| `Use Latest Basic Financials` | `Character` | **Required** |





#### Predict health cost

```http
  POST GET /predict
```



| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Age`      | `Int` | **Required** |
| `Gender ` | `Character` | **Required** |
| `BMI` | `Int` | **Required** |
| `Children` | `Int` | **Required** |
| `Smoke?` | `Int` | **Required** |
| `Region` | `Int` | **Required** |






## Installation

Run requirements.txt and start the project -
python app.py

# Tech Stack
Frontend: HTML, CSS and JavaScript

Backend: Flask, Python

## Authors

- [@suzandsouza](https://www.github.com/suzandsouza)
- [@martinajohn](https://www.github.com/martinajohn)
- [@shagun1202](https://www.github.com/shagun1202)
