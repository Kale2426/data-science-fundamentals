"""
python_basics.py
Demonstrates core Python building blocks used throughout data science work:
collections, control flow, and reusable functions.
"""

# ---- Core Python collections ----
scores = [88, 92, 76, 95]                     # list: ordered, mutable
coordinates = (12.9, 77.6)                    # tuple: ordered, immutable
student = {"name": "Riya", "age": 21}         # dict: key-value pairs
unique_ids = {101, 102, 103}                  # set: unordered, no duplicates

avg_score = sum(scores) / len(scores)
print(f"Average score: {avg_score:.2f}")


# ---- Control flow + reusable function ----
def categorize_age(age):
    """Bucket a numeric age into a simple life-stage category."""
    if age is None:
        return "Unknown"
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"


if __name__ == "__main__":
    sample_ages = [15, 24, 45, 67, None]
    for age in sample_ages:
        print(f"Age {age} -> {categorize_age(age)}")
