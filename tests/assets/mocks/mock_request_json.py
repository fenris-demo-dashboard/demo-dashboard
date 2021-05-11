mock_headers = {
    "Content-Type": "application/json",
}

mock_pfr_json = {
    "requestId": "32b740cc-71f6-43f8-a0f0-3f672c5d26a9",
    "submissionId": "pfr-header-test-999999",
    "status": "Success",
    "modelVersion": "2.1",
    "trend": "Improving",
    "matchDescription": "Artificial match",
    "score": 650,
    "sequenceId": "ID3HoICovpKVaxCLgRMAfpyriySf+wLYAVcUdbZZGvg=",
    "addressUsed": 0,
    "message": "P|1|4|48|75246|1234|493|C095|013|EVERYWHERE|63724|||"
    "RAMSEY|WAY|||||DALLAS|TX|0|1|202002|4|S|1|S|1|S|1|S|"
    "6|S|C|H|X|4|H|5|S|2|H||0|H||||2||||||||||1|14|05|11"
    "00EC63030E0C005846AB|4|2|JENNY|P|1|S|1|202002|057|S|057"
    "|S|S|19621110|2|1|40.17304993|-105.07704926|1|||||||||"
    "||||Y|||||||||||C3|0560S|128|9|A1|A1|A1|A1|T||A|C||0000|"
    "0431|200610|0322|0258|0125|0258|0125|200610|0647|F|C|0|"
    "201107|1|113|G|1999|A|12|14|0255|4|07|||||||||||||N||I|"
    "202005|I|N||N||N||N||N||N||C|I|201712|N||I|202001|A1|||"
    "||||||||||||||||||||||||||||||||||||||||||||||||||||Y|"
    "|||||||||||||||||||||||||||||||||||||008550|001600|||||"
    "2||2|09|06|||||201312|201506|||||G|G|||||201608|201910|"
    "||||ACURA|ACURA|||||H|H|||||A||||||ILX|TL|||||1|1|0|0|0|"
    "0|22|22|||||2014|2004|||||1481130016002034",
    "censusInfo": None,
    "decile": 4,
    "insuranceTier": "Non-standard",
    "financeTier": "Near Prime",
    "creditLevel": "Good",
    "first_name": "Jenny",
    "middle_name": "J",
    "last_name": " Everywhere",
    "date_of_birth": " 11/10/1962",
    "other_addresses": None,
    "address_line1": " 63724 Ramsey Way",
    "city": " Dallas",
    "state": " TX",
    "zip_code": "75246",
}

mock_life_events_json = {
    "requestId": "5eda452c-7347-43b3-92be-96ae236d72ed",
    "submissionId": "pfr-header-test-999999",
    "status": "SUCCESS",
    "matchDescription": "Artificial match",
    "events": [
        {
            "eventType": "NEWLY ENGAGED",
            "eventDate": "2021-03-31",
            "processDate": "2021-04-11",
        }
    ],
    "fenrisId": "ID3HoICovpKVaxCLgRMAfpyriySf+wLYAVcUdbZZGvg=",
    "first_name": "Jenny",
    "middle_name": "J",
    "last_name": " Everywhere",
    "date_of_birth": " 11/10/1962",
    "other_addresses": None,
    "address_line1": " 63724 Ramsey Way",
    "city": " Dallas",
    "state": " TX",
    "zip_code": "75246",
}

long_key = "document_buildingCharacteristics_ownerOccupied"
long_value = "Owner-occupied property (SFR/Condo)"

mock_property_details_json = {
    "requestId": "68cb5c3e-cdbd-4954-9f06-e0c94617c78d",
    "submissionId": "pfr-header-test-999999",
    "status": "SUCCESS",
    "document_buildingCharacteristics_useType": "Single Family Residential",
    "document_buildingCharacteristics_airConditioning": "Yes",
    "document_buildingCharacteristics_basement": "B",
    "document_buildingCharacteristics_totalArea": 2288.0,
    "document_buildingCharacteristics_buildingClass": "null",
    "document_buildingCharacteristics_buildingCondition": "Average",
    "document_buildingCharacteristics_buildingQuality": "C+",
    "document_buildingCharacteristics_garageType": "Garage",
    "document_buildingCharacteristics_garageNumCars": 2.0,
    "document_buildingCharacteristics_lotSize": 450410.0,
    "document_buildingCharacteristics_bathrooms": 2,
    "document_buildingCharacteristics_partialBathrooms": 0,
    "document_buildingCharacteristics_bedrooms": 3,
    "document_buildingCharacteristics_totalRooms": 5,
    "document_buildingCharacteristics_stories": 0,
    "document_buildingCharacteristics_pool": None,
    "document_buildingCharacteristics_roofType": None,
    "document_buildingCharacteristics_roofCovering": None,
    "document_buildingCharacteristics_yearBuilt": 1988,
    "document_buildingCharacteristics_heatingType": "Yes",
    "document_buildingCharacteristics_heatingFuelType": None,
    "document_buildingCharacteristics_construction": "Frame",
    "document_buildingCharacteristics_units": 1,
    long_key: long_value,
    "document_buildingCharacteristics_ownerName": "ROBERT E SIMS & JOY K SIMS",
    "document_valuation_apn": "51-80-19-08-000",
    "document_valuation_marketValueMin": 309072.0,
    "document_valuation_marketValueMax": 402305.0,
    "document_valuation_landValue": 13370.0,
    "document_valuation_improvementValue": 90440.0,
    "document_valuation_assessmentYear": 2020,
    "document_valuation_assessedValue": 103810.0,
    "document_valuation_assessedMarketValue": 296600.0,
    "document_mortgage_loanToValue": 42.1717,
    "document_mortgage_totalLienBalance": 150000.0,
    "document_mortgage_loanAmount": 150000.0,
    "document_mortgage_lender": "THE HUNTINGTON NATIONAL BANK",
    "document_mortgage_loanType": "Credit Line (Revolving)",
    "document_mortgage_titleCompany": "NONE AVAILABLE",
    "address_line1": "7745 E Wheeling Rd",
    "city": "Zanesville",
    "state": "OH",
    "zip_code": "43701",
}
