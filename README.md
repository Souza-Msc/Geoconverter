# Geoconverter


## What's about?

This python script is useful to transform GSM coordinates into decimal coordinates. This program was made to facilitade coodinates conversion for map making and nich modelling in our laboratory, since most of the commom softwares need the data to be in decimal mode and the information available in the literature does not have a standard. Our software can convert coordinates in english and in portuguese to decimal and have a high precision.

## Quick guide

To use the Geoconverter you need to have Python installed. You can download it from here https://www.python.org/. After you donwload and install the software just download the Geoconverter.py file and put it in the same folder that your dataframe and open de command prompt. If you have the columns identifiyed as Latidude and Longitude and don't mind the name of the output file, just run the following code:


```
python Geoconverter.py -i Name_of_your_file
```

If your Latitude and Longitude columns have different names you can add the **-lon** and **-lat** parameters followed by the name of your columns. Exemple:

```
python Geoconverter.py -i Name_of_your_file -lon Long -lat Lat
```

You can save your file with the name and format (.xlsx, .csv or .txt) you wish as well. You need only to add the parameter **-o** followed by the name you pick . the format you want. Exemple:

```
python Geoconverter.py -i Name_of_your_file -lon Long -lat Lat -o Converted_coordinates.xlsx
```

By default the name of the file will be Geoconverter_out.csv, since most of the Geoprocessing softwares prefer data in .csv. 

## Contact me

Questions, suggestions, comments, etc? Just send a e-mail to pedromsouza0@gmail.com or souza.pedro@ecologia.ufjf.br
