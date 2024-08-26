## TRANSACTION MONITORING SYSTEM

![image](https://github.com/user-attachments/assets/67a25f71-23b6-4c0d-ba79-8a22ecaa6bc7)

## TABLE OF CONTENTS

- [Abstract](#abstract)
- [Requirement Analysis](#requirement-analysis)
- [About the Project](#about-the-project)
- [Flowchart](#flowchart)
- [Execution Screenshot](#execution-screenshot)
- [Conclusion](#conclusion)
- [Contact](#contact)

### ABSTRACT: 

The project **Transaction Monitoring System** is designed behind the main theme of monitorization of fund transfers. With this software, Banks can identify the illegal funds transfers between Indian banks or between Abroad to India and vice versa. The functional requirements are quite implemented using software in the system. The backend comprises the space to store details of people indulged themselves in illegal fund transfers. While front end comprises the space for capturing mandatory details to carry out transactions. When a Bank receives funds from another account, the software matches the details of remitter with in-built database created using the backend. Thus, the software will allow or disallow the transactions based on the matches from database.

### REQUIREMENT ANALYSIS:

- **Operating System**: Windows 11</br>
- **Frontend**: IDLE Python (3.8 32-bit)</br>
- **Backend**: MySQL 8.0 Command Line Client

### ABOUT THE PROJECT:

The frontend and backend comprises necessary information to monitor the fund transfers. The project developed is interwined with various several modules namely: 

- **Details of account holders**</br>
- **Interfacing python and MySQL**</br>
- **Authentication process**</br>

Of course, some the modules have many sub module in it too, to ensure the strong validation of authentication process. 

- In the module named **Details of account holders**, the data of account holders are been collected as input. 
- In the second module named **Interfacing Python and MySQL**, the Python and MySQL are interwined with each other using the necessary code. 
- And in the last module named **Authentication process**, the verification and acknowledgement process are done to verify the details. 

Finally, the approval message for fund transaction will be auditioned based on the reflection of matches between details taken in frontend and databases in backend. If the match is found, then the approval will not be provided. While if the match is not found, the approval will be provided for fund transfer and further processes will be in process.

#### SQL DATABASES:

A database named rbi and many tables are been created using the SQL commands. Some of the screenshots of the databases are given below:

![image](https://github.com/user-attachments/assets/7be3b4d6-5940-4f89-b2cc-9bf3819d3871)</br>

**Table 1: abc_holders**

![image](https://github.com/user-attachments/assets/5b437ec9-915a-42b7-ad4c-e94c7d57468e)</br>

**Table 2: blacklist**

![image](https://github.com/user-attachments/assets/61cda2b4-532f-4eb3-a92b-f2e0bcce4439)</br>

**Table 3: ifsccodes and swiftcode**

![image](https://github.com/user-attachments/assets/7bbae2c8-4fdb-4acd-bdc3-162d5f7adf99)</br>

### FLOWCHART:

![image](https://github.com/user-attachments/assets/40ae0048-f2c1-49fe-905b-181f8efcd576)</br>


### EXECUTION SCREENSHOT:</br>

**CONDITION: 01**</br>

If any of the account holder’s details is being matched with the default database named BLACK LIST, transaction gets denied. Here the details of people mentioned in blacklist is mentioned to show the execution of the program.</br>

![image](https://github.com/user-attachments/assets/2d166fbb-69f0-4b23-ab17-7d05e3a9143e)</br>

**CONDITION : 02**</br>

If any of the account holder’s details is not been matched with the default database named BLACK LIST, transaction gets to proceed. Here the appropriate details of account holders are mentioned to show the execution of the program.</br>

![image](https://github.com/user-attachments/assets/7d8acff1-1a14-4e88-8981-42997d24cea2)</br>

![image](https://github.com/user-attachments/assets/8846618e-4ae0-492a-9046-d47c861923e7)</br>


### CONCLUSION:</br>

The **Transaction Monitoring System** helps banks prevent illegal fund transfers by comparing transaction details with a backend database of flagged entities. The system ensures secure and compliant transactions by using a real-time matching process, enhancing the overall integrity of financial operations. </br>

## Contact:</br>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/madhulekha-r-4b981b256/)
