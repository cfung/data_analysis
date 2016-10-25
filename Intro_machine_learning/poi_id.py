#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, test_classifier
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import tree

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
#features_list = ['poi','salary'] # You will need to use more features

#feature list with total_compensation and total_messages
'''
features_list = ['poi','salary','to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
	'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value',
    'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'director_fees',
    'deferred_income', 'long_term_incentive', 'from_poi_to_this_person', 'total_compensation', 'total_messages']
'''
# feature list without total_compensation and total_messages

features_list = ['poi','salary','to_messages', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
	'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value',
    'expenses', 'loan_advances', 'from_messages', 'other', 'from_this_person_to_poi', 'director_fees',
    'deferred_income', 'long_term_incentive', 'from_poi_to_this_person']

# picked by selectkbest
'''
features_list = ['poi', 'salary', 'total_payments', 'exercised_stock_options', 'bonus', 'restricted_stock', 'shared_receipt_with_poi', 'total_stock_value',
'loan_advances' ,'deferred_income', 'long_term_incentive']
'''

# 8 features, produced recall - 0.229
'''
features_list = ['poi', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
'bonus', 'restricted_stock', 'restricted_stock_deferred', 'director_fees']
'''

# 9 features, produced recall = 0.326
'''
features_list = ['poi', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
'restricted_stock','restricted_stock_deferred', 'expenses', 'director_fees', 
'deferred_income']
'''

# 10 features, produced recall = 0.279
'''
features_list = ['poi', 'deferral_payments', 'total_payments', 'exercised_stock_options', 'bonus', 
'restricted_stock', 'restricted_stock_deferred', 'expenses', 'director_fees', 'deferred_income']
'''
'''
# feature list with "total compensation" and "total"
features_list = ['poi', 'deferral_payments', 'total_payments', 'exercised_stock_options', 
'restricted_stock','restricted_stock_deferred', 'expenses', 'director_fees', 
'deferred_income', 'total_compensation', 'total_messages']
'''

#features_list = ['poi', 'salary', 'bonus']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# convert data_dict to numpy arrays(necessary???)
#data_dict = numpy.reshape( numpy.array(data_dict), (len(data_dict), 1))

### Task 2: Remove outliers
data_dict.pop("TOTAL", None)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", None)



### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

print "length of data set...", len(my_dataset)

poi_count = 0

salary_nan = 0
tomessage_nan = 0
defer_nan = 0
total_nan = 0
exercised_nan = 0
bonus_nan = 0
restricted_stock_nan = 0
shared_receipt_nan = 0
restricted_s_def_nan = 0
total_stock_nan = 0
expenses_nan = 0
loan_nan = 0
from_messages_nan = 0
other_nan = 0
from_this_person_nan = 0
director_nan = 0
defer_income_nan =0
long_term_nan = 0
from_poi_nan = 0


for item in my_dataset:
	#print "name ...", item
	#print "what's in data set...", my_dataset[item]
	# "\n"
	data_dict[item]['total_compensation'] = 0
	data_dict[item]['total_messages'] = 0

	if my_dataset[item]['deferral_payments'] == 'NaN':
		my_dataset[item]['deferral_payments'] = 0
		defer_nan += 1
	if my_dataset[item]['total_payments'] == 'NaN':
		my_dataset[item]['total_payments'] = 0
		total_nan += 1
	if my_dataset[item]['exercised_stock_options'] == 'NaN':
		my_dataset[item]['exercised_stock_options'] = 0
		exercised_nan += 1
	if my_dataset[item]['bonus'] == 'NaN':
		my_dataset[item]['bonus'] = 0
		bonus_nan += 1
	if my_dataset[item]['restricted_stock'] == 'NaN':
		my_dataset[item]['restricted_stock'] = 0
		restricted_stock_nan += 1
	if my_dataset[item]['restricted_stock_deferred'] == 'NaN':
		my_dataset[item]['restricted_stock_deferred'] = 0
		restricted_s_def_nan += 1
	if my_dataset[item]['total_stock_value'] == 'NaN':
		my_dataset[item]['total_stock_value'] = 0
		total_stock_nan += 1
	if my_dataset[item]['expenses'] == 'NaN':
		my_dataset[item]['expenses'] = 0
		exercised_nan += 1
	if my_dataset[item]['loan_advances'] == 'NaN':
		my_dataset[item]['loan_advances'] = 0
		loan_nan += 1
	if my_dataset[item]['director_fees'] == 'NaN':
		my_dataset[item]['director_fees'] = 0
		director_nan += 1
	if my_dataset[item]['deferred_income'] == 'NaN':
		my_dataset[item]['deferred_income'] = 0
		defer_nan += 1
	if my_dataset[item]['long_term_incentive'] == 'NaN':
		my_dataset[item]['long_term_incentive'] = 0
		long_term_nan += 1
	if my_dataset[item]['salary'] == 'NaN':
		my_dataset[item]['salary'] = 0
		salary_nan += 1

	if my_dataset[item]['poi'] == True:
		poi_count += 1

	if my_dataset[item]['to_messages'] == 'NaN':
		tomessage_nan += 1

	if my_dataset[item]['from_messages'] == 'NaN':
		from_messages_nan += 1

	if my_dataset[item]['other'] == 'NaN':
		other_nan += 1

	if my_dataset[item]['from_this_person_to_poi'] == 'NaN':
		from_this_person_nan += 1

	if my_dataset[item]['long_term_incentive'] == 'NaN':
		long_term_nan += 1

	if my_dataset[item]['from_poi_to_this_person'] == 'NaN':
		from_poi_nan += 1

	

	if my_dataset[item]['to_messages'] and my_dataset[item]['from_messages'] != 'NaN':

		my_dataset[item]['total_compensation'] = my_dataset[item]['salary'] + my_dataset[item]['total_stock_value']
		my_dataset[item]['total_messages'] = my_dataset[item]['to_messages'] + my_dataset[item]['from_messages']

	print "my_dataset...total_compensation", my_dataset[item]['total_compensation']

print "poi count..", poi_count

print "salary_nan", salary_nan 
print "tomessage_nan", tomessage_nan
print "defer_nan", defer_nan
print "total_nan", total_nan
print "exercised_nan", exercised_nan
print "bonus_nan", bonus_nan
print "restricted_stock_nan", restricted_stock_nan 
print "shared_receipt_nan ", shared_receipt_nan
print "restricted_s_def_nan", restricted_s_def_nan
print "total_stock_nan" , total_stock_nan
print "expenses_nan", expenses_nan
print "loan_nan" , loan_nan
print "from_messages_nan", from_messages_nan
print "other_nan", other_nan
print "from_this_person_nan", from_this_person_nan 
print "director_nan" , director_nan
print "defer_income_nan" , defer_income_nan
print "long_term_nan" , long_term_nan
print "from_poi_nan" , from_poi_nan

count_names = 0

for key, value in my_dataset.items():
    count_names += 1
    print(key, len([item for item in value if item]))

print "count_names", count_names
#print "# of features list", len(features_list_total)

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
#clf = GaussianNB()
#clf = linear_model.LinearRegression()  #TODO - use classifier, not regres
from sklearn.svm import SVC
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.metrics import classification_report, precision_recall_curve
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn import tree
from sklearn.grid_search import GridSearchCV
#clf = SVC(kernel='rbf', C = 1e8, gamma = 1e-3)
#clf = tree.DecisionTreeClassifier(min_samples_split=2)

pipe = make_pipeline(
	MinMaxScaler(), 
	SelectKBest(), 
	#AdaBoostClassifier()
	#RandomForestClassifier()
	#tree.DecisionTreeClassifier()
	#SVC()
	GaussianNB()
	)

params = {
	#'selectkbest__k' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
	#'selectkbest__k' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
	#'selectkbest__k' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
	'selectkbest__k' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	'selectkbest__score_func' :[f_classif],
}



#clf = AdaBoostClassifier(base_estimator=None, n_estimators=10, learning_rate=1.0, random_state=None)
#clf = AdaBoostClassifier(base_estimator=RidgeClassifierCV)
#clf = RandomForestClassifier(n_estimators=5)


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split, cross_val_score, StratifiedShuffleSplit, StratifiedKFold
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)


sss = StratifiedShuffleSplit(
	labels_train,
	n_iter = 20,
	test_size = 0.6,
	random_state = 0
	)

skf = StratifiedKFold(
	labels_train,
	n_folds = 20,

	random_state = 0

	)



clf = GridSearchCV (
	pipe,
	param_grid = params, 
	scoring = 'f1', 
	n_jobs = 1,
	cv = sss, 
	verbose = 1,
	error_score = 0, 
	pre_dispatch='2*n_jobs',
	)


clf.fit(features_train, labels_train)

print "best params returned ....", clf.best_params_

features_selected_bool = clf.best_estimator_.named_steps['selectkbest'].get_support()
features_selected_list = [x for x, y in zip(features_list[1:], features_selected_bool) if y]

print "what is features selected list...", features_selected_list



pipe.fit(features_train, labels_train)
print "selected features are:\n", pipe.named_steps['selectkbest'].get_support()

print "selectkbest score...", pipe.named_steps['selectkbest'].scores_
print "gird_scores_", clf.grid_scores_
print "best_estimator_", clf.best_estimator_

k_best_stage = pipe.named_steps['selectkbest']
print "k_best_stage", k_best_stage

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score

print ("classification_report:", classification_report(labels_test, pred))

test_classifier(clf.best_estimator_, my_dataset, features_list)


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf.best_estimator_, my_dataset, features_list)