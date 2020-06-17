import json

def dataset_list_dummy():
    dummy_response = json.dumps({
        "datasets": [
            
            {
                "id": "9c9c8a71-a2cb-44b8-83a4-250db2a2f7f5",
                "dataset_name": "COSD Bladder Cancer",
                "author": "Gary McGilvary"
            },
            {
                "id": "e7d059e9-f9b6-4701-89ba-62644e6f35b8",
                "dataset_name": "Trial Phenotyping Data",
                "author": "Rodrigo Barnes"
            }
        ]
    }, separators=(',', ':'), indent=None)
    return dummy_response

def dataset_catalogue_dummy():
    dummy_response = json.dumps({
        "id": "test_id",
        "title": "test_title",
        "description": "test_description",
    }, separators=(',', ':'), indent=None)
    return dummy_response
    
    
def dataset_dictionary_dummy():
    dummy_response = json.dumps({
        "fields": [
            {
                "constraints": "ETH",
                "description": "Ethnic background: Aboriginal or Not, ('A' or 'N').",
                "name": "Eth",
                "label":"Ethnicity",
                "type": "text"
            },
            {
                "constraints": "SEX",
                "description": "Sex: factor with levels ('F' or 'M').",
                "name": "sex",
                "label":"Sex",
                "type": "text"
            },
            {
                "constraints": "AGE",
                "description": "Age group: Primary ('F0'), or forms 'F1', 'F2' or 'F3'.",
                "name": "age_grp",
                "label":"Age Group",
                "type": "text"
            },
            {
                "constraints": "LRN",
                "description": "Factor with levels Average or Slow learner, ('AL' or 'SL').",
                "name": "Lrn",
                "label":":Learner Status",
                "type": "text"
            },
            {
                "description": "Days absent from school in the year.",
                "name": "days_absent",
                "label": "Days Absent",
                "type": "numeric"
            }
        ],
        "id": "absenteeism",
        "lookups": {
            "AGE": [
                {
                    "description": "Form 3",
                    "name": "F3"
                },
                {
                    "description": "Form 1",
                    "name": "F1"
                },
                {
                    "description": "Primary",
                    "name": "F0"
                },
                {
                    "description": "Form 2",
                    "name": "F2"
                }
            ],
            "ETH": [
                {
                    "description": "Aboriginal",
                    "name": "A"
                },
                {
                    "description": "Not Aboriginal",
                    "name": "N"
                }
            ],
            "LRN": [
                {
                    "description": "Average Learner",
                    "name": "AL"
                },
                {
                    "description": "Slow Learner",
                    "name": "SL"
                }
            ],
            "SEX": [
                {
                    "description": "Female",
                    "name": "F"
                },
                {
                    "description": "Male",
                    "name": "M"
                }
            ]
        }
    }, separators=(',', ':'), indent=None)
    return dummy_response
