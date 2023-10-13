import numpy as np
import pandas as pd

def analyze_ecg_data(ecg_data):
    ecg_data = np.array(ecg_data)[0]  # Convert input to numpy array for easier manipulation
    classes = ['A', 'N', 'O', '~']

    results = {"Class": [], "Avg Probability": [], "Max Probability": [], "Min Probability": []}

    # Loop over each class
    for i, class_ in enumerate(classes):
        # Extract the data for this class
        class_data = ecg_data[:, i]

        # Compute metrics
        avg_prob = np.mean(class_data)
        max_prob = np.max(class_data)
        min_prob = np.min(class_data)

        # Store the results
        results["Class"].append(class_)
        results["Avg Probability"].append(f"{avg_prob * 100:.2f}%")
        results["Max Probability"].append(f"{max_prob * 100:.2f}%")
        results["Min Probability"].append(f"{min_prob * 100:.2f}%")

    # Convert the dictionary to a pandas DataFrame for a nicer tabular display
    results_df = pd.DataFrame(results)

    # Find the class with the highest average probability
    most_probable_class = results_df.loc[results_df['Avg Probability'].idxmax()]['Class']

    # Print the results
    print(results_df)
    print(f"The most probable class is: {most_probable_class}")

    return results_df, most_probable_class
