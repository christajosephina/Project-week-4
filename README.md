
# Project-week-4

### The idea
For this project, my inspiration was the [OECD database focused on family](https://www.oecd.org/els/family/database.htm). 
I saw here that they have excel files for actual number of children, ideal number of children as well as maternal employement, and I wanted to combine these two.
I downloaded the excel files and created a jupyter notebook in the folder with files. Opening the excel files in the notebook, I could see that a lot of 
columns were unnamed. Because of this, I opened up the excel file in excel to see what's wrong. However, when I went in I saw that the data was old (2011) and not very interesting
That's why I switched to data from Dutch statistical organisation CBS, using datasets on [childbirth](https://www.cbs.nl/nl-nl/visualisaties/dashboard-bevolking/levensloop/kinderen-krijgen), average mother age at childbirth (same link) and amount of babies born yearly. 

### Cleaning data
I loaded the files into the notebook. They turned out to be semicolon separated. I renamed the variables into English names. It doesn't seem like there is missing data, but the commas need to be turned into periods.
Uploading the dataset on babies born each year, this table needed to be transposed.

### Merging
I merged the three datasets. 

### questions
What is the average number of kids a Dutch woman gets?
Do women who get more babies, start earlier with having them?

### Analysis
I made several graphs:
- How has the amount of babies a woman gets changed over time (2 variations: one with average nr of children, one split up)
- What is the average age a women has her children, and how has this changed over time
- scatterplot to answer the question: Do women who get more babies, start earlier with having them?

