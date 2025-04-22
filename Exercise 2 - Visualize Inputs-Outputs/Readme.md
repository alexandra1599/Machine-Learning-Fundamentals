# Exercise 2 : Visualize Input and Output :

In the previous exercise, we loaded some data and fit a model to it. Several aspects of this were simplified, particularly that the data was hard-coded into our python script, and we didn't spend any time really looking at the data itself.

Here, we load data from a file, filter it, and graph it. Doing so is a very important first step in order to build proper models or to understand their limitations.

There are various libraries that help you work with data. In Python, one of the most common libraries is Pandas. We used pandas briefly in the previous exercise. Pandas can open data saved as text files and store it in an organized table called a DataFrame.

When you load the data, it is stored as **columns and rows**, similar to a table you might see in Excel.

Data is easy to **filter by columns**. We can either type this directly, like dataset.my_column_name, or like so: dataset["my_column_name"].
We can use this to either ***extract data***, or to delete data.

Data can also be **filtered by rows**. We can get data from the top of the table by using the ***head()*** function, or from the bottom of the table by using the ***tail()*** function.
Both functions make a shallow copy of a section of our dataframe. Here, we're sending these copies to the print() function. We can also use the head and tail views for other purposes, such as for use in analyses or graphs

We can also add and delete rows and columns.
