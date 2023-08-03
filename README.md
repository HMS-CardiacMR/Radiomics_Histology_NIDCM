# Unveiling the Hidden Insights: Radiomics Signature of the Non-Ischemic Dilated Heart Using Cardiovascular Magnetic Resonance

## Description of Code

This python/R code implements our logistic regression models for the association between radiomic features and histological features.
First, radiomic features should be extracted using compute_radiomic_features.py in myradiomics. This requires the installation of pyradiomics library.
The data should be in .mat format with:
-First matrix reprensts the image
-Second matrix represents the mask
-The pixel spacing should be stored in px_size variable.

The code will read the images and masks and return the computed radiomic features. Note that the shape features are excluded due to the nature of the study. Since the region of interest near the biopsy regino does not provide any useful information about the shapes.
The code will loop over all sequences and return all radiomic features per sequence.

The next step is to run Data_Analysis.py to check the correlation between the features and keep only the non-correlated ones. 

Run Clustering.R to determine the number of clusters. The code runs consensus clustering to determine the optimal number of clusters. An alternative implementation in python is provided under Consensus_clustering_python folder.

Once the number of clsuters is determined for each sequence, run Hierarchical_clustering.py to create the clusters.

Run then Calculate_medoid to determine a single representative feature per cluster.

Finally, run Create_LG_models.py to create logistic regression models to study the association between each medoid and histological features.

![Figure1](https://github.com/HMS-CardiacMR/Radiomics_Histology_NIDCM/assets/9512423/c4c2cc50-7ee1-4e8b-80bb-3ead622746ae)

## Abstract

Background: There is a growing interest in CMR radiomic signatures as novel imaging biomarkers of cardiac diseases. The relationship between CMR radiomic signatures and myocardial tissue composition is unknown. 

Purpose: To investigate the association of CMR myocardial radiomic signatures to histological features in patients with non-ischemic dilated cardiomyopathy (DCM).

Materials and Methods: CMR images from 132 DCM patients (71% male; 54±15 years) who underwent CMR and endomyocardial biopsy within 6 [2-15] days were used to investigate the association between myocardial radiomic signatures measured from native T1, extra-cellular volume (ECV), LGE and histological features. Radiomic first-order and textural features were computed for each sequence from the mid-septal myocardium near the biopsy region. We applied hierarchical consensus clustering to identify distinct radiomic clusters. A single representative feature, the medoid, was identified within each cluster based on its minimal dissimilarity from other features. We built logistic regression models using one medoid per model to assess the association between each medoid and histological features. Association with determined using odds-ratio (OR) with 95% confidence interval.

Results: Clustering analysis unveiled three radiomic clusters for each sequence. For native T1, the medoids were textural features and were associated with histology. The three medoids were associated with myocyte hypertrophy (OR=3.87[1.40-14.68]; OR=0.45[0.21-0.95]; OR=2.12[1.03-4.39]; respectively). While Medois 1 and 2 were also associated with fibrosis (OR=2.81[1.65-5.17]; OR=0.44[0.22-0.80]), medoid 3 was associated with inflammation and vacuolization (OR=2.52[1.37-5.12]; OR=3.08[1.66-6.28]). ECV medoids included first-order and textural features. The first-order medoid was associated with myocyte hypertrophy (OR=2.33[1.04-5.64]), while medoid 3 (texture) was associated with fat replacement (OR=0.19[0.04-0.64]). LGE medoid 1 (first-order) was associated with fibrosis (OR=2.30[1.25-4.80]) and vacuolization (OR=1.99[1.12-3.96]), while medoid 3 (texture), associated with fibrosis (OR=0.25[0.06-0.68]).

Conclusions: In DCM patients, CMR radiomic features were associated with myocardial tissue composition, as assessed by invasive biopsy.
