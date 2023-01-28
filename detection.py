from scipy.spatial.distance import cosine
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.applications.resnet50 import preprocess_input
import librosa
from librosa.display import specshow
import matplotlib.pyplot as plt
import numpy as np
import os

curr_dir = os.getcwd()
static_folder = os.path.join(curr_dir, "static")
upload_folder= os.path.join(static_folder, 'uploads')

model = load_model('resnet50_weights_multi_e20_bs4_st50')
comparator = Model(inputs= model.input, outputs= model.layers[-2].output)

def detect(filename):
    if filename:
        f = os.path.join(upload_folder, filename)
        file_name = filename.split('.')[0]
        samples, sampling_rate = librosa.load(os.path.join(upload_folder, filename), sr = 25000, mono = True, offset = 0.0, duration = 1)
        D = librosa.stft(samples, n_fft=512)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        fig, ax = plt.subplots()
        img = specshow(S_db, sr=sampling_rate, x_axis='time', y_axis='log', ax=ax)
        plt.axis('off')
        stft_file = os.path.join(upload_folder, file_name + '_stft.png')
        plt.savefig(stft_file, bbox_inches='tight', pad_inches = 0)

        audio_sample_mfcc = librosa.power_to_db(librosa.feature.mfcc(y = samples, sr = sampling_rate, n_mfcc = 26))
        fig, ax = plt.subplots()
        img = specshow(audio_sample_mfcc, x_axis = 'time', y_axis = 'mel', ax = ax)
        plt.axis('off')
        mfcc_file = os.path.join(upload_folder, file_name + '_mfcc.png')
        plt.savefig(mfcc_file, bbox_inches='tight', pad_inches = 0)

        plt.close('all')
        img = load_img(stft_file,
                color_mode='rgb',
                target_size=(224,224,3))
        arr1 = img_to_array(img)
        arr1 = preprocess_input(arr1)
        arr1 = np.array([arr1])
        img = load_img(mfcc_file,
                    color_mode='rgb',
                    target_size=(224,224,3))
        arr2 = img_to_array(img)
        arr2 = preprocess_input(arr2)
        arr2 = np.array([arr2])
        res = model.predict([arr1, arr2])[0][0]
        if res >= 0.60:
            return (res, 'Pathological')
        else:
            return (res, 'Normal')

def compare(filename1, filename2):
    if filename1 and filename2:
        f1 = os.path.join(upload_folder, filename1)
        f2 = os.path.join(upload_folder, filename2)
        file_name1 = filename1.split('.')[0]
        file_name2 = filename2.split('.')[0]
        samples, sampling_rate = librosa.load(os.path.join(upload_folder, filename1), sr = 25000, mono = True, offset = 0.0, duration = 1)
        D = librosa.stft(samples, n_fft=512)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        fig, ax = plt.subplots()
        img = specshow(S_db, sr=sampling_rate, x_axis='time', y_axis='log', ax=ax)
        plt.axis('off')
        stft_file = os.path.join(upload_folder, file_name1 + '_stft.png')
        plt.savefig(stft_file, bbox_inches='tight', pad_inches = 0)

        audio_sample_mfcc = librosa.power_to_db(librosa.feature.mfcc(y = samples, sr = sampling_rate, n_mfcc = 26))
        fig, ax = plt.subplots()
        img = specshow(audio_sample_mfcc, x_axis = 'time', y_axis = 'mel', ax = ax)
        plt.axis('off')
        mfcc_file = os.path.join(upload_folder, file_name1 + '_mfcc.png')
        plt.savefig(mfcc_file, bbox_inches='tight', pad_inches = 0)

        plt.close('all')
        img = load_img(stft_file,
                color_mode='rgb',
                target_size=(224,224,3))
        arr1 = img_to_array(img)
        arr1 = preprocess_input(arr1)
        arr1 = np.array([arr1])
        img = load_img(mfcc_file,
                    color_mode='rgb',
                    target_size=(224,224,3))
        arr2 = img_to_array(img)
        arr2 = preprocess_input(arr2)
        arr2 = np.array([arr2])
        vector1 = comparator.predict([arr1,arr2])[0]

        samples, sampling_rate = librosa.load(os.path.join(upload_folder, filename2), sr = 25000, mono = True, offset = 0.0, duration = 1)
        D = librosa.stft(samples, n_fft=512)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
        fig, ax = plt.subplots()
        img = specshow(S_db, sr=sampling_rate, x_axis='time', y_axis='log', ax=ax)
        plt.axis('off')
        stft_file = os.path.join(upload_folder, file_name2 + '_stft.png')
        plt.savefig(stft_file, bbox_inches='tight', pad_inches = 0)

        audio_sample_mfcc = librosa.power_to_db(librosa.feature.mfcc(y = samples, sr = sampling_rate, n_mfcc = 26))
        fig, ax = plt.subplots()
        img = specshow(audio_sample_mfcc, x_axis = 'time', y_axis = 'mel', ax = ax)
        plt.axis('off')
        mfcc_file = os.path.join(upload_folder, file_name2 + '_mfcc.png')
        plt.savefig(mfcc_file, bbox_inches='tight', pad_inches = 0)

        plt.close('all')
        img = load_img(stft_file,
                color_mode='rgb',
                target_size=(224,224,3))
        arr1 = img_to_array(img)
        arr1 = preprocess_input(arr1)
        arr1 = np.array([arr1])
        img = load_img(mfcc_file,
                    color_mode='rgb',
                    target_size=(224,224,3))
        arr2 = img_to_array(img)
        arr2 = preprocess_input(arr2)
        arr2 = np.array([arr2])
        vector2 = comparator.predict([arr1,arr2])[0]
        print(vector1, vector2)
        sim = 1 - cosine(vector1, vector2)
        print(sim)
        res1 = detect(filename1)
        res2 = detect(filename2)
        return (sim, res1, res2)
        