# AMD
Age Related Macular Degeneration from Genetic Biomarkers
Age Related Macular Degneration(AMD) is an eye disease that causes vision loss. Macular degneeration causes loss in teh cnter of the field of vision. The center of the retine deterioates, and as a result, the vision becomes blurred.n It affects more than 200,000 people per year.

From 130 inputs of patients and their respective gene biomarkerks, we are able to predict the stage of AMD:
1. Cucconi and KS Test in R to determine which genes follow a normal distrubution and whos distribution are similar accross positive/negative cases
2. Choosing a model that has the best performearnce(Random Forest)
3. Syntehtic sampling using SMOTE KNN oversampling algoirthm to generate 4x more data for model training.
3. Hyperparameter tuning on a validation test set using GridsearchCV and Bayesian Search Optimization
