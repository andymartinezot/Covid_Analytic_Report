# Covid_Analytic_Report

![Screenshot from 2021-06-12 13-15-51](https://user-images.githubusercontent.com/77750560/121782553-6541de00-cb80-11eb-96b5-bc87f676d625.png)



First, I want to thanks to Keith Galli because the original code and idean was created by him. So, thanks man because you are such as an inspiration to improve at data analytics!
https://github.com/KeithGalli/generate-analytics-report

This repository shows the code to create a covid analytic report based on the actual data focused for Argentina. In this project uses the fpdf library to create the report like the image above.

## Setup

I suggest to download all of the code locally, recommended way is cloning the repository:

https://github.com/andymartinezot/Covid_Analytic_Report.git

If you have any trouble doing this, you can download the zip folder of this repo and then extract the files to a local file. Once you have all the files cloned locally, you should make sure you have all the necessary libraries installed.

$ pip install fpdf
$ pip install pandas numpy matplotlib
$ pip install plotly
$ pip install -U kaleido
If you run into an error with NumPy, changing the version to 1.19.3 fixed the issue for me

$ pip install numpy==1.19.3

To test if everything is set up properly, try running python new_report.py. You should get a fresh report file. You'll have to change helper.py to read from the online version of the data if you want to access the previous day (uncomment the BASE_PATH URL and comment BASE_PATH='./data'). You will also have to comment out the hard coded date at the bottom of new_report.py file. I saved it this way so not too many unneccesary requests to the GitHub server were made while testing.
