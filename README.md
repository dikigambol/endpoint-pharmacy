# endpoint-pharmacy
Clone repository dahulu, lalu install python 3.x dan nodeJs 16.x

1. install lib untuk skrip forecast (python) running,
   ```pip install pandas scikit-learn``` di terminal

2. masih di dalam terminal, masuk ke folder endpoint-pharmacy, lalu running ```npm i```

3. untuk menjalankan project running ```node index.js```

Untuk kenyamanan dan kesehatan mata anda, lakukan pengujian endpoint di postman, pada lokal env

dengan alamat: http://localhost:3000/forecast

dengan request body seperti ini:
```json
{
    "salesData": [
        { "ds": "2022-01-01", "y": "100" },
        { "ds": "2022-02-01", "y": "150" },
        { "ds": "2022-03-01", "y": "120" },
        { "ds": "2022-04-01", "y": "200" },
        { "ds": "2022-05-01", "y": "180" },
        { "ds": "2022-06-01", "y": "250" },
        { "ds": "2022-07-01", "y": "300" },
        { "ds": "2022-08-01", "y": "280" },
        { "ds": "2022-09-01", "y": "330" },
        { "ds": "2022-10-01", "y": "270" },
        { "ds": "2022-11-01", "y": "320" },
        { "ds": "2022-12-01", "y": "310" }
    ]
}
```
