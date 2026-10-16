import csv


def save_results(filename, results):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Technique",
            "Output",
            "Detected"
        ])

        for row in results:
            writer.writerow(row)
