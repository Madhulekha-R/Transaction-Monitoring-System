## TRANSACTION MONITORING SYSTEM

![image](https://github.com/user-attachments/assets/67a25f71-23b6-4c0d-ba79-8a22ecaa6bc7)

## TABLE OF CONTENTS

- [About the Project](#about-the-project)
- [Dataset Description](#dataset-description)
- [Model Implementation](#model-implementation)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Libraries Used](#libraries-used)
- [Contact](#contact)

### ABOUT THE PROJECT : 

The project 'Transaction Monitoring System' is designed behind the main theme of monitorization of fund transfers. With this software, Banks can identify the illegal funds transfers between Indian banks or between Abroad to India and vice versa. The functional requirements are quite implemented using
software in the system.
The backend comprises the space to store details of people indulged themselves
in illegal fund transfers. While front end comprises the space for capturing
mandatory details to carry out transactions. When a Bank receives funds from
another account, the software matches the details of remitter with in-built
database created using the backend. Thus, the software will allow or disallow
the transactions based on the matches from database.
### DATASET DESCRIPTION:

The dataset is been taken from **Kaggle** for the research paper. And the dataset incudes following attributes within it.</br>

- **id** : Personal identification number (Unique)</br>
- **age** : Age of the patient (Continuous)</br>
- **gender** : Male or Female (Nominal)</br>
- **height** : Height of the patient (Continuous)</br>
- **weight** : Weight of the patient (Continuous)</br>
- **ap_hi** : Systolic blood pressure of the patient</br>
- **ap_lo** : Diastolic blood pressure of the patient</br>
- **cholesterol** : Cholestral of the patient</br>
- **gluc** : Glucose level of the patient</br>
- **smoke** : Smoking status of the patient</br>
- **alco** :  Alcohol consumption of the patient</br>
- **active** : Physical activity level of the patient</br>
- **cardio** : Cardio metrics of the patient</br>

### MODEL IMPLEMENTATION:

**Five** models were implemented on the scaled data. The models were:

Logistic Regression
Decision Tree
K-Nearest Neighbours
Support Vector Machine
Random Forest

### MODEL EVALUATION:

Here's the flowchart that represents the flow of the project:

![image](https://github.com/user-attachments/assets/6f045626-48f1-45fd-b1b7-12822a9b5c84)

## RESULTS:

On implementing various machine learning algorithms over the dataset, ended up with the following output.

**LOGISTIC REGRESSION** : Logistic Regression is a machine learning algorithm that measures the relationship between the dependent variable and one or more independent variable by estimating probabilities using logistic function</br>

 Classification report:</br>
 ![image](https://github.com/user-attachments/assets/d54e2730-cf6b-46fd-a535-0bbd15d0f937)</br>
 
 Accuracy Rate:</br>
 ![image](https://github.com/user-attachments/assets/2190b3d3-ef95-42f0-ae89-f381997921f3)</br>

**SUPPORT VECTOR MACHINE**: The Support Vector Machine training algorithm builds a model that assigns new test samples to one category or other, making it a non-probabilistic binary linear classification.</br>

 Classification report:</br>
 ![image](https://github.com/user-attachments/assets/d5e45069-e452-44f4-adfb-f9b066713c9c)</br>
 
 Confusion matrix:</br>
 ![image](https://github.com/user-attachments/assets/2bd4ddeb-0c86-4ecc-aaf4-4aaab9cb3afb)</br>
 
 Accuracy Rate:</br>
 ![image](https://github.com/user-attachments/assets/a3cb86f0-609a-4099-aae8-c6a9761d2a0a)</br>

 **K-NEAREST NEIGHBORS**: Used for classification and regression.</br>

 Plot representation:</br>
 ![image](https://github.com/user-attachments/assets/7fedcd66-ed3a-45a2-bafd-b81803221f73)</br>
 
 Accuracy Rate:</br>
 ![image](https://github.com/user-attachments/assets/cf7ca84e-f410-4bac-b6dd-788acb6bd256)</br>

 **DECISION TREE CLASSIFIER**: Decision Tree Classifier acts as a predictive model which amps features to conclusions about the target value.</br>

 Classification report:</br>
 ![image](https://github.com/user-attachments/assets/b63e4913-1a86-4b53-bb24-143535f2fc1e)</br>
 
 Accuracy Rate:</br>
 ![image](https://github.com/user-attachments/assets/39ac5bc9-4e7f-4492-ae44-4decf4d647bf)</br>

 **RANDOM FOREST**: Random Forest is a machine learning algorithm that output the mode of classes and the mean prediction of individual trees.</br>
 Accuracy Rate:</br>
 ![image](https://github.com/user-attachments/assets/1abe17ec-55ce-49b1-a3b5-2e630a9529e8)</br>

### CONCLUSION:</br>

![Screenshot 2024-08-05 194727](https://github.com/user-attachments/assets/52d0a16b-fad2-4b0a-883f-a439e4408d60)

The blue line represents the training accuracy and red line represents the test accuracy. Thus, it is concluded that the model is overfitted where the model excels in its performance on the training data but lacks the ability to generalize effectively to novel, unseen data.

## LIBRARIES USED:</br>

### For handling and manipulating data:
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)](https://numpy.org/)

### For Visualization
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=python)](https://matplotlib.org/)

### For Hypothesis testing, Pre-processing and Model training
[![Statsmodels](https://img.shields.io/badge/Statsmodels-3776AB?style=for-the-badge&logo=python)](https://www.statsmodels.org/)
[![Scikit Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/madhulekha-r-4b981b256/)
