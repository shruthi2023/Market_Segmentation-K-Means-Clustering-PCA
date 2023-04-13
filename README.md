### Market_Segmentation-K-Means-Clustering-PCA

Market Segmentation in Superstore
Objective :
This case requires to develop a Superstore Market segmentation to support marketing strategy 
development and planning.

Steps Involved ---->

1. Import ‘super_store_data’ csv file

2. Look at the shape and distribution to understand the data

3. Creating heatmap

4. Feature Selection, Drop feature using Pearson Correlation

5. Outlier detection and removel using IQR

6. Standardize the data

7. Create an K-MEANS, Start with 6 clusters for Exploration

8. Running K-MEANS on a range of clusters to find optimal number 

9. Creating scree plot to visualize inertia - Elbow Method

10. Understanding that the inertia score start to drop drastically between 4 - 5 number of cluster. Thefore, I have decided to choose 4 number of cluster to grain granularity on our study

11. Re-Running K-MEANS on 4 clusters 

12. Create Principal Component Analysis(PCA)

13. Running PCA to visualize data 

14. Percentage of variance explained for each component 

15. Identifying the "BEST" number of components: Trying with dimensionality reduction and K-MEANS

16. 2 eigenvectors can be used to represent 95% variance

17. Running PCA again with 2 component

18. Running K-MEANS

19. Creating Scree plot to visualize inertia - Elbow Method

20. Running PCA with 2 component

21. Saving Scikitlearn model using joblib

22. Training and Testing the model accuracy using decision tree

23. Saving the Decision tree model for future prediction

24. created a Streamlit Application based on this clustering technique, where we are taking the store details & identifying which cluster the store belongs to.

