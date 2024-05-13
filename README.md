
# Climate Health Data Workshop 

Developed by Eqi Luo, Andrew Zimmer, and Cascade Tuholske, Montana State University  

While specifically developed for the Climate Health Data Science workshop, this course leverages materials from [UCSB EDS2017](https://github.com/environmental-data-science/eds217_2023), developed by Prof. [Kelly Caylor](https://github.com/kcaylor), and from [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html), developed by Prof. [Ryan Abernathey](https://github.com/rabernat), as well as [GPHY-491-591](https://github.com/cascadet/GPHY-491-591) developed by Cascade Tuholske. 



## How to use this repository

1. Fork this repository to create a local copy in your github account. Do this by clicking the "Fork" button in the upper right corner of the [repository home page](https://github.com/EqiLuo/Climate-Health-Data-Science-Workshop).

1. Clone the forked repository to your local computer

	* Open your `Terminal`.

	* Type `git clone` and the the url for your forked copy of this repository, which is `https://github.com/<your username>/Climate-Health-Data-Science-Workshop`, where <your username> is your github user id.

	     The entire command will look like this:

		`$ git clone https://github.com/<your username>/Climate-Health-Data-Science-Workshop`

		**Note:** In the line above, the `$` is your terminal prompt. On other systems, the command prompt is something like `>`, or `[username]$`. To keep these directions more general, I will just use `$` to represent the command prompt throughout our docs. The key point is that you *don't* need to type this as part of the command.

	* Press **Enter**. A local clone of the class repository will be created on your local computer.

		```
		$ git clone https://github.com/<your username>/Climate-Health-Data-Science-Workshop
		Cloning into 'GPHY-491-591'...
	remote: Enumerating objects: 4, done.
		remote: Counting objects: 100% (4/4), done.
		remote: Compressing objects: 100% (4/4), done.
		remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
		Receiving objects: 100% (4/4), done.
		```

	     You will now have a new local directory in your instance called `Climate-Health-Data-Science-Workshop`, which contains all of the course materials. We will download and practice using all of the required software to use these course materials on Day 0 of the course.


## Data Preprocessing for DHS houesehold survey

One of the example datasets used in this tutorial is the filtered household survey data collected in 2014 by The Demographic and Health Surveys (DHS) Program in Ghana. Due to user license agreements and data sensitivity, specific measures have been implemented to ensure that the information remains confidential and is used in compliance with DHS data usage policies.

In the preprocessing of the 2014 DHS household survey data from Ghana, geographical coordinates were randomly shifted by approximately 2.5 km and rounded to six decimal places to anonymize locations. Identifiers for 'mother_id', 'household_id', and 'cluster_id' were reassigned to maintain data confidentiality. The dataset was balanced by selecting 500 urban and 500 rural records, ensuring equitable representation. After processing, the sampled data was appended back to the original dataset and sorted by the newly assigned identifiers to maintain structured data integrity for further analysis.
