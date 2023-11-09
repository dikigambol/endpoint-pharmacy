const express = require('express');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.use(express.json());

app.post('/forecast', (req, res) => {
    try {
        const pythonProcess = spawn('python', ['sales_forecast.py']);
        let dataToSend = JSON.stringify(req.body.salesData);

        pythonProcess.stdin.write(dataToSend);
        pythonProcess.stdin.end();

        let forecastResults = '';

        pythonProcess.stdout.on('data', data => {
            forecastResults += data.toString();
        });

        pythonProcess.on('close', code => {
            res.send(forecastResults);
        });
    } catch (error) {
        res.status(500).send('An error occurred during forecast processing.');
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
