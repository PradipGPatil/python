from prescription_data import * 

trial_patient=["Denise","Eddie","Frank","Georgia"]

# remove warfaring and add Edoxaban

# # here we have 'patients' as dictionary
# for patient in trial_patient:
#     prescription=patients[patient]
#     prescription.remove(warfarin)
#     prescription.add(edoxaban)    # here all the patient have warfarin , so it will get replaced by edoxaban
#     print(patient, prescription, sep=": ")


trial_patient_2=["Denise","Eddie","Frank","Georgia","Kenny"]

for patient in trial_patient_2:
    prescription=patients[patient]
    # prescription.discard(warfarin)

    # change the code to remove to see
    try: 
        prescription.remove(warfarin)
        prescription.add(edoxaban)    # here all the patient have warfarin , so it will get replaced by edoxaban
    except:
        print(f" Patient {patient} is not taking warfaring"
            f" please remove {patient} from trial"
              )
    print(patient, prescription)