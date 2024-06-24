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


### Scope
The proposed framework focuses on early diagnosis and treatment of pathological voice
disorder with the aid to deep learning models. It also sheds light on a unique pathway to
develop a system which requires less computational complexity and provides faster
processing as compared to the traditional systems.

Deliverables of the project can be summarized as follows :
- Cost-effective and accurate diagnosis reports provided to the patients
- User-friendly & remotely accessible application for both, patients as well as medical
professionals
<br>

Exclusions and constraints of the proposed project can be elucidated as follows: 
- The focus of the system will be on the detection of functional dysphonia, limited to
physical damage only, and will not consider other pathologies. Other pathologies are
out of the scope of this project.
- The system will face a cold-start problem for discriminating the changes in the voice,
as the use of the Comparator network is possible only if previously recorded audio of
the patient is available.
- Exceptional cases might occur in the classification phase, as there is a possibility of
multiple pathologies (other than the one due to physical damage) having similar
characteristics and symptoms. In this case, the pathology will be detected but will be
misclassified and needs to be further investigated by the medical professional.

### Methodology


### Application
The application of the suggested system is in the biomedical field where it will provide an
individual, easy accessibility to medical assistance as well as cost effective and accurate
diagnosis of voice disorders caused due to physical detriment.
