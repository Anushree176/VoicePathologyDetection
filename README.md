# Voice Pathology Detection
The final year project of Anushree Kolhe, Ruchi Bheke and Aditya Borude for the course of B.E. Computer Engineering at S.I.E.S. Graduate School of Technology in the academic session 2018-2022.

<br>

### Abstract
A pathological voice is the result of disorders or damage to vocal organs by any means such
as tissue infection, systemic changes, mechanical stress, etc, and not limited to pathogens like
viruses, bacteria, fungus, and parasites. The main aim of our system is early detection and
diagnosis of pathological voice disorders using deep learning models, which will also be
easily accessible to the public. The previously proposed systems do not shed light on the
comparative similarity check for the same individual. This system consists of two different
processes, the first being a CNN classifier which is a binary classifier used for the
classification of pathological voice and normal voice, and the second is a voice discriminator
to compute the similarity of the inputs by comparing the feature vectors. Before this, the
signal is transformed as an image (spectrograms) with time and frequency in two dimensions.
The spectrograms can be effectively used to capture the characteristics of the signal. The
Comparator network is used to calculate the similarity score between two inputs based on
their feature vectors. Thus, if the historical audio data of the patient is available, the
Comparator network can be used as a discriminator. between two audio inputs, the current
voice and the previously recorded voice of the patient. According to our survey, there is much
research work for the proposed system but no-real world implementation. As we aim to
increase the accuracy of the healthcare system, the predicted result should be interpreted by a
specialist and then advised upon. Therefore, our system also provides prompt and appropriate
medical assistance to the patients detected with pathological voice disorders.
