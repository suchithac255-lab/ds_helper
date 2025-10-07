import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from ds_helper.auto_visualizer import visualize
from ds_helper.column_detector import column_detector
from ds_helper.text_cleaner import TextCleaner

# Sample data
df = pd.DataFrame({
    "Age": [22, 25, 30, 28, 40, 35, 22],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Male"],
    "Comments": ["Good", "Excellent service", "Bad experience", "Okay", "Loved it", "Could be better", "Nice"]
})

# Test column_detector
types = column_detector(df)
expected = {'Age': 'numerical', 'Gender': 'categorical', 'Comments': 'text'}
assert types == expected, f"Expected {expected}, got {types}"
print("Column detector test passed.")

# Test text_cleaner
cleaner = TextCleaner()
sample_text = "Um, I think this product is, like, really good!!! But you know, it’s a bit pricey."
cleaned = cleaner.clean_text(sample_text)
expected_cleaned = "think product really good bit pricey"
assert cleaned == expected_cleaned, f"Expected '{expected_cleaned}', got '{cleaned}'"
print("Text cleaner test passed.")

# Test auto_visualizer (will generate plots but not show due to backend)
visualize(df)
print("Auto visualizer test completed (plots generated).")

print("All tests passed!")
