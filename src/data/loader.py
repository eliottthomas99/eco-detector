import fiftyone as fo
import os
import argparse
import sys

def load_taco_to_fiftyone(data_dir: str, labels_path: str, dataset_name: str = "taco-labeled"):
    """Loads TACO dataset into FiftyOne for visualization.

    Args:
        data_dir: Directory containing the images.
        labels_path: Path to the COCO annotations JSON.
        dataset_name: Name for the FiftyOne dataset.

    Returns:
        fo.Dataset: The loaded FiftyOne dataset.
    """
    # Create or Load Dataset
    if dataset_name in fo.list_datasets():
        print(f"Dataset '{dataset_name}' already exists. Overwriting...")
        fo.delete_dataset(dataset_name)

    print(f"Loading TACO dataset from {data_dir}...")
    dataset = fo.Dataset.from_dir(
        dataset_type=fo.types.COCODetectionDataset,
        data_path=data_dir,
        labels_path=labels_path,
        label_types=["detections", "segmentations"],
        name=dataset_name,
    )
    
    # Add some metadata (optional but helpful for engineers)
    dataset.description = "TACO Official Labeled Dataset"
    dataset.persistent = True
    
    return dataset

if __name__ == "__main__":
    # Fixed paths for our current setup
    DATA_PATH = "data/raw/taco_images"
    LABELS_PATH = "data/raw/taco_images/annotations.json"
    
    # Ensure FiftyOne is running in a way that works for WSL
    os.environ["FIFTYONE_DATABASE_DIR"] = "/home/eliott/.fiftyone/db"
    
    try:
        dataset = load_taco_to_fiftyone(DATA_PATH, LABELS_PATH)
        
        # Launch the FiftyOne App
        print("\nLaunching FiftyOne App at http://localhost:5151")
        session = fo.launch_app(dataset, port=5151, remote=True) # remote=True for WSL/headless
        
        print("\nPress Ctrl+C to stop the session.")
        session.wait()
    except KeyboardInterrupt:
        print("\nFiftyOne session stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError loading dataset: {e}")
        sys.exit(1)
