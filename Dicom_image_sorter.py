import os
import shutil
import pydicom

def organize_dicoms_by_size_and_id(input_root_folder, output_root_folder):
    if not os.path.exists(output_root_folder):
        os.makedirs(output_root_folder)

    for id_folder in os.listdir(input_root_folder):
        id_path = os.path.join(input_root_folder, id_folder)

        if os.path.isdir(id_path):
            for file in os.listdir(id_path):
                if file.lower().endswith(".dcm"):
                    dicom_path = os.path.join(id_path, file)

                    try:
                        dicom = pydicom.dcmread(dicom_path)
                        rows, cols = dicom.Rows, dicom.Columns
                        size_folder = f"{rows}x{cols}"

                        # Path to the target folder like output/512x512/ID_001/
                        target_folder = os.path.join(output_root_folder, size_folder, id_folder)
                        os.makedirs(target_folder, exist_ok=True)

                        # Copy the DICOM file
                        target_path = os.path.join(target_folder, file)
                        shutil.copy2(dicom_path, target_path)

                    except Exception as e:
                        print(f"⚠️ Skipping file {dicom_path} due to error: {e}")

    print("✅ DICOMs have been organized by size and ID.")

# Example usage
input_folder = "test"  # your folder containing ID_001, ID_002, etc.
output_folder = "output_dicoms_by_size"
organize_dicoms_by_size_and_id(input_folder, output_folder)
