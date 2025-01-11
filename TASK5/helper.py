
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


class Helper():

    @staticmethod

    def prepare_and_train_reg_model(X,y,model,):
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        
        model = model
        model.fit(X_train_scaled, y_train)
        
    
        train_predictions = model.predict(X_train_scaled)
        test_predictions = model.predict(X_test_scaled)
        
        # 6. Calculate metrics
        train_mse = mean_squared_error(y_train, train_predictions)
        test_mse = mean_squared_error(y_test, test_predictions)
        train_mae = mean_absolute_error(y_train, train_predictions)
        test_mae = mean_absolute_error(y_test, test_predictions)
        
        print(f'Train MSE: {train_mse:.2f}')
        print(f'Test MSE: {test_mse:.2f}')

        print(f'Train MAE: {train_mae:.2f}')
        print(f'Test MAE: {test_mae:.2f}')
    

    @staticmethod
    def prepare_and_train_class_model(X,y,model):
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = model
        model.fit(X_train_scaled, y_train)

        train_predictions = model.predict(X_train_scaled)
        test_predictions = model.predict(X_test_scaled)

        print("Training ")
        print(f"No of correct predictions {np.sum(y_train == train_predictions)} out of {len(y_train)}")


        print("Testing")
        print(f"No of correct predictions {np.sum(y_test == test_predictions)} out of {len(y_test)}")
        
        # 6. Calculate metrics
        train_accuracy = accuracy_score(y_train, train_predictions)
        test_accuracy = accuracy_score(y_test, test_predictions)

        print("Train accuracy: ", train_accuracy)
        print("Test accuracy: ", test_accuracy)

    

    @staticmethod
    def prepare_and_train_knn_model(X,y,model):

        X=np.array(X)
        y=np.array(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        
        model = model
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        total_samples = len(y_test)
        correct_predictions = np.sum(y_test == predictions)
        print(f"{correct_predictions} out of {total_samples}")

   
   
    @staticmethod
    def compare_reg_models(X,y,models):
        for model in models:
            print(model.__class__.__name__)
            Helper.prepare_and_train_reg_model(X,y,model)
            print("\n")

    @staticmethod
    def compare_class_models(X,y,models):
        for model in models:
            print(model.__class__.__name__)
            Helper.prepare_and_train_class_model(X,y,model)
            print("\n")

    @staticmethod
    def compare_knn(X,y,models):
        for model in models:
            print(model.__class__.__name__)
            Helper.prepare_and_train_knn_model(X,y,model)
            print("\n")


    @staticmethod

    def plot_model(model):
        plt.figure(figsize=(10, 5))
        plt.plot(range(model.epochs),model.cost_history)
        plt.title('Cost Function')
        plt.xlabel('Epochs')
        plt.ylabel('Cost')
        plt.grid(True)
        plt.show()

