import numpy as np
import pandas as pd
import matplotlib.pylot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,
cross_val_score
from slearn.preprocessing import standard scaler
from sklearn.linear_model import LogisticRegression
from sklearn.discriminantAnalysis
import LinearDiscriminantAnalysis
from sklearn.neighbors,import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import svc
from sklearn.metrices import accuracy_score

#2.load the dataset
iris=load_iris()
x=iris.data
y=iris.target
feature_names = iris.feature_names
target_names=iris.target_names
#convert to pandas DataFrame for easier handling
data=pd.DataFrame(data=x,columns=feature_names)
data['species']=[target_names[i] for i in y]

#3.Summarize the dataset
print("Dimensions of the dataset:")
print(data.shape)
print("\n Peek at the data.")
print(data.head())
print("\n Statistical summary of all the attributes.")
print(data.describe())
print("\n Breakdown of the data by the class variable.")
print(data['species'].value_counts())

#4. Visualize the dataset
# Univariate plots
fig,axes=plt.subplots(nrows=2,ncols=2,figsize= for i,feature in enumerate (feature_names):(12,8)) sns.histplot(data(feature),kde=True,
ax=axes[i//2,i%2])
axes[i//2,i%2].set_title(f' distribution of {feature}')
plt.tight_layout()
plt.show()
#Multivariate plots
sns.pairplot(data,hue='species')
plt.show()

#5. Evaluate some algorithms
# Separate out a validation dataset
x_train,x_test,y_train,y_test=train_test_split
(x,y,test_size=0.3,random_size=4.2)
#set up models
models={'Logistic Regression':Logistic Regression(max_iter=200),
        'Linear Discriminant Analysis': KNeighborsClassifier(),
        'Decision Tree': DecisionTreeClassifier(),
        'Gaussian Naive Bayes': GaussianNB(),
        'Support Vector Machine':svc()
        }
#cross-validation and evaluation
results={}
for name,model in models.items():
# 10-fold cross-validation
cv_scores = cross_val_score(model,x_train,y_train,cv=10)
results[name]={'Mean Accuracy'=np.mean(cv_scores),
               'Standard Deviation': np.std(cv_scores)
               }
#Print results
print("\n Algorithm Performance:")
for name,metrics in result.items():
print(f{name}: Mean_Accuracy ={metrics['Mean Accuracy']:3f},std Dev={metrics ['Standard Deviation']:3f}")

#6. Making some predictions
# Fit all models and make predictions on test set for name,model in models.items():
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f" \n{name} Test Accuracy:{accuracy:.3f}")
      
      
      

      


