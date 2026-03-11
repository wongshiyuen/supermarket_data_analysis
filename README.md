# Supermarket Sales Dataset Analysis
Data analysis on Supermarket Sales Dataset via SQL and hypothesis testing.

## Executive Summary
Branch C leads in sales, with Health & Beauty, Home & Lifestyle, and Electronic Accessories as its top product lines. Membership program impact is negligible, and branch differences are statistically insignificant.

## Problem Statement
The Supermarket Sales Dataset is a dataset containing 100 observations with data on customer gender, invoice ID, supermarket branch at which a sale occurred, city (supermarket location), product line, unit price, (sale) quantity, and tax. This work aims to achieve the following objectives:
1)  Determine and rank total sales for each branch.
2)  Identify and ranked product lines with highest sales with respect to branch.
3)  Determine if there is a significant difference in sales between normal customers and members.
4) Determine if there are significant differences in sales between all branches.

## Methodology
- Total sales for each branch, as well as bestseller product lines for each branch, were determined and ranked using SQL.
- A **one-tailed t-test** with **5% significance level** was used to determine if there is a significant difference in sales between normal customers and members.
- **ANOVA** testing with **5% significance level** was used to determine if there are statistically significant differences in sales between all supermarket branches.

## Results
> Table 1: Total sales and taxes of each branch in descending order.

|Branch	|Total Sales|Total Taxes
|:------|:----------|:----------
|C	    |105303.50  |16047.90
|A	    |101143.20  |15224.12
|B      |101140.60	|12640.56

> Table 2: Product lines with highest sales with respect to branch ranked in descending order.

|Branch|Product Line		      	|Total Sales|Total Taxes
|:-----|:-----------------------|:----------|:----------
|C	   |Health and beauty	    	|15824.12		|2189.02
|C	   |Home and lifestyle	  	|13233.86		|2202.37
|C	   |Electronic accessories	|18065.69		|2619.73
|B	   |Food and beverages	  	|14490.37		|1603.89
|B	   |Electronic accessories	|16239.47		|2235.4
|A	   |Electronic accessories	|17444.87		|1348.68
|A	   |Home and lifestyle	  	|21349.71		|3668.13
|A	   |Sports and travel		    |18450.19		|3435.73
|C	   |Fashion accessories		  |20533.4		|4669.1
|B	   |Home and lifestyle	  	|16713.49		|1780.84
|B	   |Health and beauty	    	|19029.2		|2977.49
|C	   |Sports and travel	    	|15011.36		|2251.63
|A	   |Food and beverages	  	|16345.81		|1627.39
|A	   |Health and beauty	    	|11997.86		|1725.83
|C	   |Food and beverages  		|22635.1		|2116.05
|B	   |Sports and travel	    	|19036.38		|1794.19
|A	   |Fashion accessories	  	|15554.77		|3418.36
|B	   |Fashion accessories	  	|15631.73		|2248.75

> Table 3: Mean and standard deviation for sales based on customer type.

|Customer Type	|Mean	  |Standard Deviation
|:--------------|:------|:-----------------
|Normal		    	|55.14	|26.24
|Member		    	|56.21	|26.71

> Table 4: ANOVA results

|		      	|sum_sq	|df	  	|F	  	|PR(>F)
|:----------|:------|:------|:------|:-----
|C(Branch)	|558.1	|2.0  	|0.3970	|0.6724
|Residual	  |700705	|997.0	|NaN  	|NaN

Based on Table 1, Branch C had the highest total sales, while Branch B had the least. Furthermore, Table 2 shows that the ‘Health and Beauty’, ‘Home and Lifestyle’, and Electronic Accessories’ product lines of Branch C were the top 3 most lucrative branch-specific product lines. Improvement in revenue can most likely be best achieved by focusing on these 3 product lines in Branch C.

Table 3 shows that members had slightly higher mean sales compared to normal customers. However, based on the one-tailed test results, **t-statistic = -0.6395** and **p-value = 0.2613**. Since the p-value obtained was above the 5% significance level, any difference in sales between 'normal' and 'member' customers could be considered negligible. An assessment of membership benefits could be considered to encourage customer spending. For example, benefits could be made more attractive by introducing a more lucrative point-based system for purchases.

Table 4 shows residual variation (700,705) was far larger than branch variation (558), indicating that customer level differences dominate sales outcomes. Furthermore, PR(>F) had a value of 0.6724, which was larger than the 5% significance level. Hence, differences in sales between branches could be deemed random noise.

## Conclusion
- Branch C had the highest sales, followed by A, and lastly B.
- ‘Health and Beauty’, ‘Home and Lifestyle’, and Electronic Accessories’ product lines of Branch C were the top 3 most lucrative branch-specific product lines.
- Negligible difference in sales between 'normal' and 'member' customers.
- Negligible difference in sales between supermarket branches.

## Data Attribution
The Supermarket Sales Dataset is a dataset licensed under **CC0: Public Domain**. It is available on Kaggle at:
(https://www.kaggle.com/datasets/ismatkhan121/supermarket-sales-dataset)
