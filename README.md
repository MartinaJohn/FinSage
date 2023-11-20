
# AI for solving economic downturns

The project supports the following features,
The goal of our study is to apply AI to forecast and lessen the effects of economic downturns. AI, in our opinion, can offer insightful information and predictive powers that can better assist governments and companies in anticipating and responding to economic downturns.
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
## Authors

- [@suzandsouza](https://www.github.com/suzandsouza)
- [@martinajohn](https://www.github.com/martinajohn)
- [@shagun1202](https://www.github.com/shagun1202)
