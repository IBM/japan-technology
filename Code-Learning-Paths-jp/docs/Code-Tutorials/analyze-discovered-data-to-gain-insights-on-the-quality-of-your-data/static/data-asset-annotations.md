---
{}
---

<!-- Convert and save this file as a pdf:

1. Make changes locally
2. Install grip if not installed already: pip install grip
3. Run grip, which renders the .md file on localhost : grip data-asset-annotations.md
4. Open the localhost link in a browser and Save as PDF.
-->

# Data asset annotations

This file specifies annotation information for each data asset in the HealthcareAnalysis project. This includes:

* the governance term for each data asset
* the primary key for each data asset
* the data class for each column in the data asset
* the business term for each column in the data asset

## ALLERGIES

Governance term: Allergy

Primary key: None

| Column      | Data class   | Business term       |
|-------------|--------------|---------------------|
| Start       | Date         | Allergy Start Date  |
| Stop        | Date         | Allergy Stop Date   |
| Patient     | UUID         | Patient ID          |
| Encounter   | UUID         | Encounter ID        |
| Code        | Allergy code | Allergy Code        |
| Description | Text         | Allergy Description |

## CAREPLANS

Governance term: Careplan

Primary key: ID

| Column            | Data class     | Business term               |
|-------------------|----------------|-----------------------------|
| ID                | UUID           | Careplan ID                 |
| Start             | Date           | Careplan Start Date         |
| Stop              | Date           | Careplan Stop Date          |
| Patient           | UUID           | Patient ID                  |
| Encounter         | UUID           | Encounter ID                |
| Code              | Careplan code  | Careplan Code               |
| Description       | Text           | Careplan Description        |
| ReasonCode        | Condition code | Condition Code              |
| ReasonDescription | Text           | Condition Description       |

## CONDITIONS

Governance term: Condition

Primary key: None

| Column      | Data class     | Business term         |
|-------------|----------------|-----------------------|
| Start       | Date           | Condition Start Date  |
| Stop        | Date           | Condition Stop Date   |
| Patient     | UUID           | Patient ID            |
| Encounter   | UUID           | Encounter ID          |
| Code        | Condition code | Condition Code        |
| Description | Text           | Condition Description |

## ENCOUNTERS

Governance term: Encounter

Primary key: ID

| Column              | Data class      | Business term                |
|---------------------|-----------------|------------------------------|
| ID                  | UUID            | Encounter ID                 |
| Start               | Timestamp       | Encounter Start Date         |
| Stop                | Timestamp       | Encounter Stop Date          |
| Patient             | UUID            | Patient ID                   |
| Organization        | UUID            | Organization ID              |
| Provider            | UUID            | Provider ID                  |
| Payer               | UUID            | Payer ID                     |
| EncounterClass      | Encounter class | Encounter Class              |
| Code                | Encounter code  | Encounter Code               |
| Description         | Text            | Encounter Description        |
| Base_Encounter_Cost | Quantity        | Base Encounter Cost          |
| Total_Claim_Cost    | Quantity        | Encounter Total Claim Cost   |
| Payer_Coverage      | Quantity        | Encounter Payer Coverage     |
| ReasonCode          | Condition code  | Condition Code               |
| ReasonDescription   | Text            | Condition Description        |

## IMMUNIZATIONS

Governance term: Immunization

Primary key: None

| Column      | Data class        | Business term            |
|-------------|-------------------|--------------------------|
| Date        | Timestamp         | Immunization Date        |
| Patient     | UUID              | Patient ID               |
| Encounter   | UUID              | Encounter ID             |
| Code        | Immunization code | Immunization Code        |
| Description | Text              | Immunization Description |
| Base Cost   | Quantity          | Immunization Base Cost   |

## MEDICATIONS

Governance term: Medication

Primary key: None

| Column             | Data class      | Business term                 |
|--------------------|-----------------|-------------------------------|
| Start              | Timestamp       | Medication Start Date         |
| Stop               | Timestamp       | Medication Stop Date          |
| Patient            | UUID            | Patient ID                    |
| Payer              | UUID            | Payer ID                      |
| Encounter          | UUID            | Encounter ID                  |
| Code               | Medication code | Medication Code               |
| Description        | Text            | Medication Description        |
| Base_Cost          | Quantity        | Medication Base Cost          |
| Payer_Coverage     | Quantity        | Medication Payer Coverage     |
| Dispenses          | Numeric         | Medication Dispenses          |
| Total Cost         | Quantity        | Medication Total Cost         |
| Reason Code        | Condition code  | Condition Code                |
| Reason Description | Text            | Condition Description         |

## OBSERVATIONS

Governance term: Observation

Primary key: None

| Column      | Data class       | Business term           |
|-------------|------------------|-------------------------|
| Date        | Timestamp        | Observation Date        |
| Patient     | UUID             | Patient ID              |
| Encounter   | UUID             | Encounter ID            |
| Code        | Observation code | Observation Code        |
| Description | Text             | Observation Description |
| Value       | Text             | Observation Value       |
| Units       | Code             | Observation Units       |
| Type        | Indicator        | Observation Value Type  |

## ORGANIZATIONS

Governance term: Organization

Primary key: ID

| Column      | Data class        | Business term             |
|-------------|-------------------|---------------------------|
| ID          | UUID              | Organization ID           |
| Name        | Organization Name | Organization Name         |
| Address     | US Street Name    | Organization Address      |
| City        | City              | Organization City         |
| State       | US State Code     | Organization State        |
| Zip         | US Zip Code       | Organization Zip          |
| Lat         | Latitude          | Organization Latitude     |
| Lon         | Longitude         | Organization Longitude    |
| Phone       | US Phone Number   | Organization Phone Number |
| Revenue     | Quantity          | Organization Revenue      |
| Utilization | Numeric           | Organization Utilization  |

## PATIENTS

Governance term: Patient

Primary key: ID

| Column              | Data class                        | Business term               |
|---------------------|-----------------------------------|-----------------------------|
| ID                  | UUID                              | Patient ID                  |
| Birthdate           | Date of Birth                     | Patient Birth Date          |
| Deathdate           | Date                              | Patient Death Date          |
| SSN                 | US Social Security Number         | Patient SSN                 |
| Driver's License    | Driver's License                  | Patient Driver's License    |
| Passport            | Passport                          | Patient Passport            |
| Prefix              | Honorific                         | Patient Prefix              |
| First Name          | First Name                        | Patient First Name          |
| Last Name           | Last Name                         | Patient Last Name           |
| Suffix              | Name Suffix                       | Patient Suffix              |
| Maiden Name         | Last Name                         | Patient Maiden Name         |
| Marital             | Legal Marital/Civil Status.       | Patient Marital Status      |
| Race                | Race                              | Patient Race                |
| Ethnicity           | Ethnicity (hispanic/non-hispanic) | Patient Ethnicity           |
| Gender              | Gender                            | Patient Gender              |
| Birthplace          | Text                              | Patient Birthplace          |
| Address             | US Street Name                    | Patient Address             |
| City                | City                              | Patient City                |
| State               | US State Name                     | Patient State               |
| County              | US County                         | Patient County              |
| Zip                 | US Zip Code                       | Patient Zip                 |
| Lat                 | Latitude                          | Patient Latitude            |
| Lon                 | Longitude                         | Patient Longitude           |
| Healthcare_Expenses | Quantity                          | Patient Healthcare Expenses |
| Healthcare_Coverage | Quantity                          | Patient Healthcare Coverage |

## PAYERS

Governance term: Payer

Primary key: ID

| Column                  | Data class        | Business term                 |
|-------------------------|-------------------|-------------------------------|
| ID                      | UUID              | Payer ID                      |
| Name                    | Organization Name | Payer Name                    |
| Address                 | US Street Name    | Payer Address                 |
| City                    | City              | Payer City                    |
| State_Headquartered     | US State Code     | Payer State                   |
| Zip                     | US Zip Code       | Payer Zip                     |
| Phone                   | US Phone Number   | Payer Phone                   |
| Amount_Covered          | Quantity          | Payer Amount Covered          |
| Amount_Uncovered        | Quantity          | Payer Amount Uncovered        |
| Revenue                 | Quantity          | Payer Revenue                 |
| Covered_Encounters      | Numeric           | Payer Covered Encounters      |
| Uncovered_Encounters    | Numeric           | Payer Uncovered Encounters    |
| Covered_Medications     | Numeric           | Payer Covered Medications     |
| Uncovered_Medications   | Numeric           | Payer Uncovered Medications   |
| Covered_Procedures      | Numeric           | Payer Covered Procedures      |
| Uncovered_Procedures    | Numeric           | Payer Uncovered Procedures    |
| Covered_Immunizations   | Numeric           | Payer Covered Immunizations   |
| Uncovered_Immunizations | Numeric           | Payer Uncovered Immunizations |
| Unique_Customers        | Numeric           | Payer Unique Customers        |
| QOLS_AVG                | Quantity          | Payer QOLS Avg                |
| Member_Months           | Numeric           | Payer Member Months           |

## PROCEDURES

Governance term: Procedure

Primary key: None

| Column                       | Data class     | Business term                |
|------------------------------|----------------|------------------------------|
| Date                         | Timestamp      | Procedure Date               |
| Patient                      | UUID           | Patient ID                   |
| Encounter                    | UUID           | Encounter ID                 |
| Code                         | Procedure code | Procedure Code               |
| Description                  | Text           | Procedure Description        |
| Procedure Base Cost          | Quantity       | Procedure Base Cost          |
| Procedure Reason Code        | Condition code | Condition Code               |
| Procedure Reason Description | Text           | Condition Description        |

## PROVIDERS

Governance term: Provider

Primary key: ID

| Column       | Data class         | Business term        |
|--------------|--------------------|----------------------|
| ID           | UUID               | Provider ID          |
| Organization | UUID               | Organization ID      |
| Name         | Person Name        | Provider Name        |
| Gender       | Gender             | Provider Gender      |
| Specialty    | Provider specialty | Provider Specialty   |
| Address      | US Street Name     | Provider Address     |
| City         | City               | Provider City        |
| State        | US State Code      | Provider State       |
| Zip          | US Zip Code        | Provider Zip         |
| Lat          | Latitude           | Provider Latitude    |
| Lon          | Longitude          | Provider Longitude   |
| Utilization  | Numeric            | Provider Utilization |