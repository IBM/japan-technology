---
completed_date: '2021-07-17'
draft: false
excerpt: Learn about working with the different types of geospatial data using Python.
menu_order: 4
meta_description: Learn about working with the different types of geospatial data
  using Python.
meta_keywords: data science, data science topics, beginner, geospatial data
meta_title: Explore other data science topics
primary_tag: data-science
subtitle: Learn about working with the different types of geospatial data using Python
title: Explore other data science topics
---

## Geospatial data

Geospatial data refers to any data set that includes information about the geographic location of the record in addition to other features. For example, a data set that contains information about several cities with their population size that also includes two extra columns with the latitude and longitude coordinates is considered geospatial data. Geospatial information is helpful with inferring a lot of extra information, for example, to find the distance between cities, calculate average household incomes by neighborhood, and to create maps.

Typically, geospatial data is represented in two ways: vector data and raster data.

### Vector data

 _Vector data_ is a representation of a spatial element through its x and y coordinates. The most basic form of vector data is a _point_. Two or more points form a _line_, and three or more lines form a _polygon_. As an example, you can define the location of a city by a point (x and y coordinates), but in reality the shape of the city contains much more information. There are roads that can be represented by lines, which consist of the two points that represent the start and the end of the line. Also, there are many polygons that represent shapes of any form such as buildings, regions, and city boundaries.

### Raster data

Raster data is a type of geospatial data that contains information about the geometric location in the form of grids and matrices. Depending on the type and number of attributes, these matrices can be multidimensional, with each dimension representing a feature and each pixel within it containing a value that represents a feature. For example, a data set that contains weather information for a city represented as a multidimensional array can include details about temperature, relative humidity, and wind velocity. Satellite images or any images representing geographical locations are forms of raster data.

netCDF, PNG, JPEG, TIFF, and binary files are examples of raster data types. An extensive list of the data types can be found in a <a href="https://www.igismap.com/raster-data-file-format/" target="_blank" rel="noopener noreferrer">raster data file formats</a> list.

## Learn more

To learn more about working with geospatial data using Python, look at the [Data analysis using Python](/learningpaths/data-analysis-using-python/) learning path.