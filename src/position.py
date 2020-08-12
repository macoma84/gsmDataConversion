import pandas as pd
import random

import soap

import gc

from openpyxl import load_workbook

import logging
import threading
import time

import concurrent.futures



class Clock():
    history = 100
    
    size = 0
    times = []
    
    totalWaitTime = 0
    elapsedTime=0
    executions=0
    waitTime = 0
    
    @classmethod
    def averageTime(cls):
        return sum(cls.history)/cls.size

    @classmethod
    def execute(cls, elapsedTime):
        if cls.size < cls.history:
            cls.size += 1
            cls.append(elapsedTime)
        else:
            cls.times.pop(0)
            cls.append(elapsedTime)
    
    @classmethod
    def setWait(cls, diff):
        
        if diff > 0:
            cls.totalWaitTime += diff
        cls.waitTime = cls.totalWaitTime/cls.executions
        
        
        
        
        
        
#         cls.waitTime += diff
#         if cls.waitTime < 0:
#             cls.waitTime = 0
#         elif cls.waitTime > cls.averageTime():
#             cls.waitTime = cls.averageTime()



def thread_function(position):
    
    
    logging.info("Thread %s: starting", position['REFERENCE_NBR'])
    
    
    time.sleep(Clock.waitTime)
    
    t = time.time() 
    try:
        soap.sendGSM(gsm=position)
    except Exception as e:
        print (e)
    elapsed_time = time.time() - t
    
    Clock.execute(elapsedTime=elapsed_time)
    
    average = Clock.averageTime()
    
    Clock.setWait(diff= elapsed_time-average )
    
    print(Clock.waitTime, average, elapsed_time, Clock.totalWaitTime/Clock.executions )
    #Clock.waitTime = elapsed_time
    
    #print(Clock.averageTime(elapsedTime=elapsed_time))
    
    logging.info("Thread %s: finishing", position['REFERENCE_NBR'])

    
    #print(Clock.waitTime)


df = pd.read_csv("C:\\gsmDataConversion\\resources\\export_cuenta.csv")
df_to_doct = df.to_dict(orient='records')

df = pd.read_csv("C:\\gsmDataConversion\\resources\\export.dsv", delimiter='|')
fondos = df.to_dict(orient='records')
fondos = [v for v in fondos if v['CLASS_NAME'] != 'A']


df = pd.read_excel("C:\\gsmDataConversion\\resources\\GSM_DC_TEMPLATE.xlsx")
GSM_DC_TEMPLATE = df.to_dict(orient='records')


df = pd.read_excel("C:\\gsmDataConversion\\resources\\GSM_WS_TEMPLATE.xlsx")
GSM_DC_TEMPLATE = df.to_dict(orient='records')



threadNum = 40

#maxPositions = 100000
maxPositions = 40
saveEach = 220000

reference = random.randint(0, 100000000)

positions = []


#writer = pd.ExcelWriter(str(reference)+"-"+str(maxPositions)+"_"+"data.xlsx", engine='openpyxl')

#df.to_excel(writer)
#writer.save()



line = 0
for i in range(1,  maxPositions+1):

    client = random.randint(0, len(df_to_doct)-1)
    qty = random.randint(5, 100)

    client_type = df_to_doct[client]['PERSON_TYPE']
    if client_type == 'PHYSICAL':
        tempFondos = [v for v in fondos if v['PHYSICAL_PERSONS'] == 1]
    elif client_type == 'LEGAL':
        tempFondos = [v for v in fondos if v['MORAL_PERSONS'] == 1]

    instrument = random.randint(0, len(tempFondos)-1)
    
##    position = dict({
##        'Legal Entity':'BCO ACTINVER',
##        'Type':'GEN.A.CTE.TITULOS',
##        'Pay/Recieve':'RECEIVE',
##        'Product':'FUNDSHARE',
##        'Instrument':''+str(tempFondos[instrument]['INSTRUMENTO']),
##        'Settlement Date':'2020-04-30',
##        'Settlement Mean':'DEPOSITO',
##        'Quantity':qty,
##        'Nominal / Residual':None,
##        'Price Type Convention':None,
##        'Reference Nbr':str(reference) + '_' + str(i),
##        'Comments':None,
##        'Party Type':'CLIENT',
##        'Party Name':df_to_doct[client]['CLIENT_ID'],
##        'Party Account': df_to_doct[client]['NUMBER_'],
##        'Counterparty Type':'EXTERNAL',
##        'Counterparty Name':df_to_doct[client]['CLIENT_ID'],
##        'Counterparty Account':None,
##        'Price':tempFondos[instrument]['BID']
##        })



    position = dict({
        'USER': 'LuminaAdmin',
        'PASSWORD': 'xxx',
        #'ENCRYPTION': 'OMITIR',
        #'ENCRYPTION_KEY': 'OMITIR',
        #'SOURCE_SYSTEM': 'OMITIR',
        'LEGAL_ENTITY': 'BCO ACTINVER',
        'TYPE': 'GEN.A.CTE.TITULOS',
        'PAY_RECIEVE': 'RECEIVE',
        'PRODUCT': 'FUNDSHARE',
        'INSTRUMENT': ''+str(tempFondos[instrument]['INSTRUMENTO']),
        'SETTLEMENT_DATE': '2020-04-30',
        'SETTLEMENT_MEAN': 'DEPOSITO',
        'QUANTITY': qty,
        'NOMINAL_RESIDUAL': 'N',
        #'PRICE_TYPE_CONVENTION': 'OMITIR',
        'REFERENCE_NBR': str(reference) + '_' + str(i),
        #'COMMENTS': 'OMITIR',
        'PARTY_TYPE': 'CLIENT',
        'PARTY_NAME': df_to_doct[client]['CLIENT_ID'],
        'PARTY_ACCOUNT': df_to_doct[client]['NUMBER_'],
        'COUNTER_PARTY_TYPE': 'EXTERNAL',
        'COUNTER_PARTY_NAME': 1204106,
        #'COUNTER_PARTY_ACCOUNT': 'OMITIR',
        'PRICE': tempFondos[instrument]['BID'],
        #'BRIDGE_ACCOUNT': 'OMITIR',
        #'ACQ_DATE': 'OMITIR',
        #'INSTRUMENT_FX_CCY': 'OMITIR',
        #'INSTRUMENT_FX_RATE': 'OMITIR',
        #'ADJUSTED_UNIT_COST': 'OMITIR',
        #'CLIENT_FEE': 'OMITIR',
        #'FEE_PERCENTAGE': 'OMITIR',
        #'FEE_AMOUNT': 'OMITIR',
        #'FEE_AMOUNT_CCY': 'OMITIR',
        #'FEE_FX_RATE': 'OMITIR'
        })


    

    positions.append(position)
    
##  if i % saveEach == 0 or i == maxPositions-1:
        
        

##        df = pd.DataFrame.from_dict(positions, orient="index")
##        positions = {}
##        #startrow = writer.book['Sheet1'].max_row
##        #df.to_excel(writer, startrow=startrow, header=False)
##        #writer.save()
##        #del [df]
##        #gc.collect()
##        #df=pd.DataFrame()
##        print(i)
##        df.to_csv(str(reference)+"-"+str(maxPositions)+"_"+"data.cvs")
        


        



if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")
       
    logging.info("Starting")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadNum) as executor:
        executor.map(thread_function, positions)
    
         



    
    






