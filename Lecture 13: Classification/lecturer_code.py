import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

# Function to calculate evaluation metrics
def get_stats(TP, FP, TN, FN):
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    accuracy = (TP + TN) / (TP + FP + TN + FN)
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'Accuracy: {accuracy:.2f}')
    print(f'F1 Score: {f1_score:.2f}')


# Split the data into training and test sets
def split_8020(examples):
    sample_indices = random.sample(range(len(examples)), len(examples) // 5)
    training_set, test_set = [], []

    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set

# k-NN classification method
def knn_classification(training_set, test_set):
    X_train, y_train = zip(*training_set)
    X_test, y_test = zip(*test_set)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    return tp, fp, tn, fn

# Random splits evaluation
def random_splits(examples, method, num_splits, to_print=True):
    TP, FP, TN, FN = 0, 0, 0, 0
    random.seed(0)
    for t in range(num_splits):
        training_set, test_set = split_8020(examples)
        results = method(training_set, test_set)
        TP += results[0]
        FP += results[1]
        TN += results[2]
        FN += results[3]
    
    get_stats(TP/num_splits, FP/num_splits, TN/num_splits, FN/num_splits)
    return TP/num_splits, FP/num_splits, TN/num_splits, FN/num_splits

