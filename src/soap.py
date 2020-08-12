from suds.client import Client

from suds.plugin import MessagePlugin

from suds.xsd.doctor import ImportDoctor, Import

from jproperties import Properties


##imp = Import('http://services.interfaces.subsystem.lumina.lumina.com/')
##imp.filter.add('HEADER') 


#Import('http://services.interfaces.subsystem.lumina.lumina.com/', location='http://actinver-uat-02:8080/ApplicationInitializer/ws/CaptureGSMService?xsd=CaptureGSMService.xsd')

#imp.filter.add('http://services.interfaces.subsystem.lumina.lumina.com/') 

#imp = Import('http://services.interfaces.subsystem.lumina.lumina.com/', location = 'http://actinver-uat-02:8080/ApplicationInitializer/ws/CaptureGSMService?xsd=CaptureGSMService.xsd')


#imp = Import('http://schemas.xmlsoap.org/wsdl/soap/')
# Below is your targetNamespace presented in WSDL. Remember
# that you can add more namespaces by appending more imp.filter.add

##doctor = ImportDoctor(imp) 

#p = Properties()
#with open("app.file", "r") as f:
#    p.load(f, "utf-8")
#p["serviceURL"]

client = Client(url='http://localhost:8080/ApplicationInitializer/ws/CaptureGSMService?wsdl')



def sendGSM(gsm):

    HEADER = client.factory.create('HEADER')
    GSM = client.factory.create('GSM')


    HEADER.USER = gsm['USER']
    HEADER.PASSWORD = gsm['PASSWORD']
    ##HEADER.ENCRYPTION = gsm['ENCRYPTION']
    ##HEADER.ENCRYPTION_KEY = gsm['ENCRYPTION_KEY']
    ##HEADER.SOURCE_SYSTEM = gsm['SOURCE_SYSTEM']


    GSM.LEGAL_ENTITY = gsm['LEGAL_ENTITY']
    GSM.TYPE = gsm['TYPE']
    GSM.PAY_RECIEVE = gsm['PAY_RECIEVE']
    GSM.PRODUCT = gsm['PRODUCT']
    GSM.INSTRUMENT = gsm['INSTRUMENT']
    GSM.SETTLEMENT_DATE = gsm['SETTLEMENT_DATE']
    GSM.SETTLEMENT_MEAN = gsm['SETTLEMENT_MEAN']
    GSM.QUANTITY = gsm['QUANTITY']
    GSM.NOMINAL_RESIDUAL = gsm['NOMINAL_RESIDUAL']
    ##GSM.PRICE_TYPE_CONVENTION = gsm['PRICE_TYPE_CONVENTION']
    GSM.REFERENCE_NBR = gsm['REFERENCE_NBR']
    ##GSM.COMMENTS = gsm['COMMENTS']
    GSM.PARTY_TYPE = gsm['PARTY_TYPE']
    GSM.PARTY_NAME = gsm['PARTY_NAME']
    GSM.PARTY_ACCOUNT = gsm['PARTY_ACCOUNT']
    GSM.COUNTER_PARTY_TYPE = gsm['COUNTER_PARTY_TYPE']
    GSM.COUNTER_PARTY_NAME = gsm['COUNTER_PARTY_NAME']
    ##GSM.COUNTER_PARTY_ACCOUNT = gsm['COUNTER_PARTY_ACCOUNT']
    GSM.PRICE = gsm['PRICE']
    ##GSM.BRIDGE_ACCOUNT = gsm['BRIDGE_ACCOUNT']
    ##GSM.ACQ_DATE = gsm['ACQ_DATE']
    ##GSM.INSTRUMENT_FX_CCY = gsm['INSTRUMENT_FX_CCY']
    ##GSM.INSTRUMENT_FX_RATE = gsm['INSTRUMENT_FX_RATE']
    ##GSM.ADJUSTED_UNIT_COST = gsm['ADJUSTED_UNIT_COST']
    ##GSM.CLIENT_FEE = gsm['CLIENT_FEE']
    ##GSM.FEE_PERCENTAGE = gsm['FEE_PERCENTAGE']
    ##GSM.FEE_AMOUNT = gsm['FEE_AMOUNT']
    ##GSM.FEE_AMOUNT_CCY = gsm['FEE_AMOUNT_CCY']
    ##GSM.FEE_FX_RATE = gsm['FEE_FX_RATE']
    ##GSM.CLEAN_PRICE = gsm['CLEAN_PRICE']

   


    response = client.service.captureGsmService(HEADER=HEADER, GSM=GSM)
        
##    GSM.LEGAL_ENTITY = gsm[]
##GSM.TYPE = 'GEN.A.CTE.TITULOS'
##GSM.PAY_RECIEVE = 'RECEIVE'
##GSM.PRODUCT = 'FUNDSHARE'
##GSM.INSTRUMENT = 'PROTEGE-E'
##GSM.SETTLEMENT_DATE = '2020-04-30'
##GSM.SETTLEMENT_MEAN = 'DEPOSITO'
##GSM.QUANTITY = 28
##GSM.NOMINAL_RESIDUAL = 'N'
####GSM.PRICE_TYPE_CONVENTION = None
##GSM.REFERENCE_NBR = '48862403_1'
####GSM.COMMENTS = None
##GSM.PARTY_TYPE = 'CLIENT'
##GSM.PARTY_NAME = '6786081'
##GSM.PARTY_ACCOUNT = '6786081 - CUSTODIA'
##GSM.COUNTER_PARTY_TYPE = 'EXTERNAL'
##GSM.COUNTER_PARTY_NAME = '1204106'
####GSM.COUNTER_PARTY_ACCOUNT = None
##GSM.PRICE = '7.651221'
####GSM.BRIDGE_ACCOUNT = None
####GSM.ACQ_DATE = None
####GSM.INSTRUMENT_FX_CCY = None
####GSM.INSTRUMENT_FX_RATE = None
####GSM.ADJUSTED_UNIT_COST = None
####GSM.CLIENT_FEE = None
####GSM.FEE_PERCENTAGE = None
####GSM.FEE_AMOUNT = None
####GSM.FEE_AMOUNT_CCY = None
####GSM.FEE_FX_RATE = None
####GSM.CLEAN_PRICE = 1
##
##        
##        'LEGAL_ENTITY': 'BCO ACTINVER',
##        'TYPE': 'GEN.A.CTE.TITULOS',
##        'PAY_RECIEVE': 'RECEIVE',
##        'PRODUCT': 'FUNDSHARE',
##        'INSTRUMENT': ''+str(tempFondos[instrument]['INSTRUMENTO']),
##        'SETTLEMENT_DATE': '2020-04-30',
##        'SETTLEMENT_MEAN': 'DEPOSITO',
##        'QUANTITY': qty,
##        'NOMINAL_RESIDUAL': 'N',
##        'PRICE_TYPE_CONVENTION': 'OMITIR',
##        'REFERENCE_NBR': str(reference) + '_' + str(i),
##        'COMMENTS': 'OMITIR',
##        'PARTY_TYPE': 'CLIENT',
##        'PARTY_NAME': df_to_doct[client]['CLIENT_ID'],
##        'PARTY_ACCOUNT': df_to_doct[client]['NUMBER_'],
##        'COUNTER_PARTY_TYPE': 'EXTERNAL',
##        'COUNTER_PARTY_NAME': 1204106,
##        'COUNTER_PARTY_ACCOUNT': 'OMITIR',
##        'PRICE': tempFondos[instrument]['BID'],
##        'BRIDGE_ACCOUNT': 'OMITIR',
##        'ACQ_DATE': 'OMITIR',
##        'INSTRUMENT_FX_CCY': 'OMITIR',
##        'INSTRUMENT_FX_RATE': 'OMITIR',
##        'ADJUSTED_UNIT_COST': 'OMITIR',
##        'CLIENT_FEE': 'OMITIR',
##        'FEE_PERCENTAGE': 'OMITIR',
##        'FEE_AMOUNT': 'OMITIR',
##        'FEE_AMOUNT_CCY': 'OMITIR',
##        'FEE_FX_RATE': 'OMITIR'
##        })
##
##
##HEADER.USER = 'LuminaAdmin'
##HEADER.PASSWORD = 'xxx'
####request[0].ENCRYPTION = None
####request[0].ENCRYPTION_KEY = None
####request[0].SOURCE_SYSTEM = None
##
##
##
##GSM.LEGAL_ENTITY = 'BCO ACTINVER'
##GSM.TYPE = 'GEN.A.CTE.TITULOS'
##GSM.PAY_RECIEVE = 'RECEIVE'
##GSM.PRODUCT = 'FUNDSHARE'
##GSM.INSTRUMENT = 'PROTEGE-E'
##GSM.SETTLEMENT_DATE = '2020-04-30'
##GSM.SETTLEMENT_MEAN = 'DEPOSITO'
##GSM.QUANTITY = 28
##GSM.NOMINAL_RESIDUAL = 'N'
####GSM.PRICE_TYPE_CONVENTION = None
##GSM.REFERENCE_NBR = '48862403_1'
####GSM.COMMENTS = None
##GSM.PARTY_TYPE = 'CLIENT'
##GSM.PARTY_NAME = '6786081'
##GSM.PARTY_ACCOUNT = '6786081 - CUSTODIA'
##GSM.COUNTER_PARTY_TYPE = 'EXTERNAL'
##GSM.COUNTER_PARTY_NAME = '1204106'
####GSM.COUNTER_PARTY_ACCOUNT = None
##GSM.PRICE = '7.651221'
####GSM.BRIDGE_ACCOUNT = None
####GSM.ACQ_DATE = None
####GSM.INSTRUMENT_FX_CCY = None
####GSM.INSTRUMENT_FX_RATE = None
####GSM.ADJUSTED_UNIT_COST = None
####GSM.CLIENT_FEE = None
####GSM.FEE_PERCENTAGE = None
####GSM.FEE_AMOUNT = None
####GSM.FEE_AMOUNT_CCY = None
####GSM.FEE_FX_RATE = None
####GSM.CLEAN_PRICE = 1






