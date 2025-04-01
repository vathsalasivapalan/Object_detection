# Object_detection

## workflows
--constants 
 ------ create the folder -ARTIFACTS_DIR (its main folder name )
 ------ crrate the folder -DATA_INGESTION_DIR_NAME (download zip file)
 ------ create the folder -DATA_INGESTION_FEATURE_STORE_DIR (unzip operation)
 ------ -create the folder -DATA_DOWNLOAD_URL (from here download the url inside artifact folder)

--entity
---config_entity
 ------ creating TIMESTAMP folder 
 ------ creating the class use the constant path 
---artifact_entity
 ------ return the 1.data_file_path
                   2. feature_store_file_path

--components
-- data_ingestion
 ------ import os operating system 
 ------ import sys -its need to custom  package for reusable 
 ----- need 'urllib'--- help to download any kind of file from the internet
 ----- import zipfile -- easily unzip the data 
 ----- import logging and exception(With logging and exceptions, you’ll see detailed error tracking in logs.)
 ----- import config entity
 ----- import artifacts entity 
 ---- 1.create class -DataIngestion(it will have two function)
 ---------------1.download the data -download_data (first this method will run)
 ---------------2.extract the zip file- extract_zip_file(second this method will run)
 ---------------3.initiate/call the data -initiate_data_ingestion (calling the data)
          

--pipeline (flow-execution)/which component run first/last
   ---pipeline flow 1.run data ingestion
                    2.data validation
                    3.model trainer 
                    4.model pusher
--1. import -sys,os,logger , exception
--app.py --- endpoint


## how to run:



'''bash
conda create -n signlang python=3.13 -y

'''

'''bash
conda activate signlang
'''

'''bash
pip install -r requirements.txt
'''

