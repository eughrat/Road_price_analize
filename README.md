
# ROAD COST ANALYSIS

### PROJECT BRIEFING

In this data analysis project we will look Itat the cost of road construction in Poland. is said that road construction in Poland is much more expensive than in neighboring countries and the quality of the new routes does not meet the requirements of the users.

We will check the list of elements of newly build or rebuilt roads and what road elements contribute the most to the high cost of roads in Poland and what does it look like from the inside.

The analysis will be carried out on the basis of real data for which the names of the roads covered by the analysis have been changed.

The input material are pdf files obtained from a reputable polish construction company, the explanation of which is presented below.

The original data contains the following columns:

* 'Lp.': Ordinal number
* 'CPV': Central Product Classification code
* 'Numer Specyfikacji Technicznej': Technical Specification code
* 'Elementy rozliczeniowe': Billing elements
* 'Jednostka': Measure unit
* 'Ilosc': Quantity
* 'Cena jedn': Unit price
* 'Wartosc calkowita': Total value
* 'Droga': Road number
* 'Rok': Year of construction
* 'Kategoria': Category of construction works

### PROJECT OVERVIEW

The project consists of three parts:

* Data preparation - This part contains data cleansing and validation of existing calculations. Adding new columns with values needed for further analysis.
* Cost analysis - This part of the project includes checking the costs of individual and aggregated  road elements, depending on the road categories and road lengths. An analysis of the projected increase in road construction costs was also carried out
* Quantity analysis- The result of the analysis is the cheatsheet with the amount of materials for 1 km of road category. It can be used by construction and design companies for quick cost and quantity calculations in an initial phase of road projects and in the auction process.

### INSTALATION

Short guide to get startd with sofware:

1. Clone the repo or donwload zip file.
2. Open the folder with IDE editor.
3. Create conda virtual environment.4
4. Download and install Ghostscript - https://ghostscript.com/releases/gsdnld.html
5. Install all the libraries form requirements.txt
6. Make migrations

Thats's all. 

This analysis may be augmented with additional data to increase its accuracy so feel free to use it.

### AUTHOR

Michał Piernicki 
