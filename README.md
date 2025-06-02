# likert-R-examples
Holds sample code for "[On Likert Scales In R](https://jakec007.github.io/2021-06-23-R-likert/)" blog post. 

For best viewing check out the [PDF here!](https://jakec007.github.io/assets/files/2021-06-23-R-likert.pdf)



See the June 2025 update blog post.



### Get The Sample Code Working With `renv`

This project (now, as of 6 1, 2025) uses [`renv`](https://rstudio.github.io/renv/) to ensure package versions are reproducible.

To restore the required R packages 

1. Open the Project in RStudio 
   - Go to `File → Open Project...`
   - Select the `.Rproj` file in `/data`
2. Run the following in the RStudio Console
   - `install.packages("renv")`      
   -  `renv::restore()`

### Get The Sample Code Working Manually 

If you don't want to use `renv` to get the project environment you can manually install the packages I used to build this tutorial back in '21. The package versions are in the table below; to install them simply do:

```R
install.packages("remotes")
remotes::install_version("likert", version = "1.3.5")
remotes::install_version("HH", version = "3.1.43")
```



| Package      | Version |
| ------------ | ------- |
| knitr        | 1.31    |
| foreign      | 0.8.72  |
| ggplot2      | 3.3.3   |
| colorspace   | 2.0.0   |
| tidyverse    | 1.3.0   |
| dplyr        | 1.0.4   |
| RColorBrewer | 1.1.2   |
| grid         | 3.6.2   |
| HH           | 3.1.43  |
| likert       | 1.3.5   |







