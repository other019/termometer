README
---

Termometer aplication wich generates web sites with cool looking graph :smile:

Works on rasppbery pi using DS18B20 connected to GPIO4. 

Generates line charts by using dygraphs lib from dygraphs.com.

other019

---
Tips:

While creating data.csv make sure if the first name is:
'''
Date, Temperature
'''
---
The chart is a bit jagged if measurment take place every 60 second, so few test:
1. Mesurment every 60 sec:

2. Mesurment every 10 sec:

3. Mesurment every 600 sec:

4. Mesurment is mean of 3 last measurments(60 seconds):

5. Mesurment is mean of 3 last measurments(10 seconds):

6. Mesurment is less precise (60 seconds):



---

to do list:
* add new device search
