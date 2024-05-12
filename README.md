Tribute to the team members under this project:
Muhammad Subhan 
Hamza Asad
# Streaming Data Insights for Audio Features Analysis

## Introduction

This report outlines the design, implementation, and evaluation of a streaming data analysis system developed for analyzing audio features extracted from music files. The system consists of a data preprocessing pipeline, feature extraction, and storage mechanism using MongoDB.

### Producer Application

The producer application is responsible for reading audio files, extracting features, and streaming the preprocessed data to MongoDB. Audio files are processed to extract Mel-frequency cepstral coefficients (MFCCs) and other relevant features.

### Consumer Application

The consumer application involves connecting to MongoDB, retrieving the preprocessed audio features, and storing them in the database. Each audio file's features, including MFCCs, are stored as documents in the MongoDB collection.

## Code Overview

The provided Python code performs the following tasks:

1. **Data Preprocessing and Feature Extraction**: 
    - Audio files are read from a specified directory.
    - MFCCs, log filter bank energies, and other features are extracted using the Librosa library and Python Speech Features.

2. **Database Connection**:
    - The code establishes a connection to a MongoDB instance running on localhost:27017.

3. **Feature Extraction and Insertion into MongoDB**:
    - Extracted audio features, including MFCCs and log filter bank energies, are inserted into a MongoDB collection named 'audio_features' within the 'MusicModel' database.
    - Each document in the collection represents an audio file, with its associated features stored as fields.

4. **Verification and Monitoring**:
    - The code includes verification steps to ensure successful extraction and insertion of audio features into MongoDB.
    - Monitoring mechanisms are implemented to track the number of documents inserted into the collection for quality assurance.

## Usage

To run the code:

1. Ensure MongoDB is installed and running on your system.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Update the `dataset_path` variable with the path to your audio files directory.
4. Execute the Python script to preprocess audio files, extract features, and insert them into MongoDB.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Librosa
- Python Speech Features
- pymongo

## Conclusion

The developed system demonstrates an effective approach to extract and store audio features in MongoDB for further analysis. By utilizing MFCCs, log filter bank energies, and other relevant features, the system enables insights extraction and pattern recognition from music files, facilitating various downstream applications such as music recommendation systems, genre classification, and audio content analysis.

For any issues or inquiries, please contact [Your Name] at [Your Email].

