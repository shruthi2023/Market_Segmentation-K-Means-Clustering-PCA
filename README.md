# Market_Segmentation-K-Means-Clustering-PCA
Market Segmentation in Superstore
Objective :
This case requires to develop a Superstore Market segmentation to support marketing strategy 
development and planning.
Steps Involved ---->
•	Import ‘super_store_data’ csv file
•	Look at the shape and distribution to understand the data
•	Creating heatmap
•	Feature Selection, Drop feature using Pearson Correlation
•	Outlier detection and removel using IQR
•	Standardize the data
•	Create an K-MEANS, Start with 6 clusters for Exploration
•	Running K-MEANS on a range of clusters to find optimal number 
•	Creating scree plot to visualize inertia - Elbow Method
•	Understanding that the inertia score start to drop drastically between 4 - 5 number of cluster. Thefore, I have decided to choose 4 number of cluster to grain granularity on our study
•	Re-Running K-MEANS on 4 clusters 
•	Create Principal Component Analysis(PCA)
•	Running PCA to visualize data 
•	Percentage of variance explained for each component 
•	Identifying the "BEST" number of components: Trying with dimensionality reduction and K-MEANS
•	2 eigenvectors can be used to represent 95% variance
•	Running PCA again with 2 component
•	Running K-MEANS
•	Creating Scree plot to visualize inertia - Elbow Method
•	Running PCA with 2 component
•	Saving Scikitlearn model using joblib
•	Training and Testing the model accuracy using decision tree
•	Saving the Decision tree model for future prediction
•	created a Streamlit Application based on this clustering technique, where we are taking the store details & identifying which cluster the store belongs to.

