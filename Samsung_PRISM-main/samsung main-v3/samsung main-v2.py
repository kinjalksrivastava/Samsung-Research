from s00 import *
from s01 import *
from s10 import *
from s11 import *
from configurator import *
from tabulate import tabulate
import math
import os

    
def runner():
    lst = [(1,'Load User Defined RRC Parameters'),
           (2,'Load Default RRC Parameters')
                   ]
    col_names = ["Index", "Operations"]
  
    print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
    act=int(input("Enter Your Option--> "))
    if act==1:
        f = open('config.txt', 'r')
        x = f.readlines()
        ccs	=int(x[0])
        bwp	=int(x[1])
        tdr	=int(x[2])
        dmrsconfig	=int(x[3])
        dmrsmaxlen= int(x[3])
        sulstatus	=int(x[5])
        ulsul	=int(x[6])
        fhf	=int(x[7])
        has	=int(x[8])
        dla	=int(x[9])
        srs	=int(x[10])
        pin	=int(x[11])
        csi	=int(x[12])
        cgb	=int(x[13])
        ulptrsstats	=int(x[14])
        puschtpstats	=int(x[15])
        boi	=int(x[16])
        vrb	=int(x[17])
        prb	=int(x[18])
        rmi	=int(x[19])
        zp	=int(x[20])
        dai	=int(x[21])
        pdsch	=int(x[22])
        tci	=int(x[23])
        cgbt	=int(x[24])
        cgbf	=int(x[25])
        f.close()
    if act==2:
        f = open('config_default.txt', 'r')
        x = f.readlines()
        ccs	=int(x[0])
        bwp	=int(x[1])
        tdr	=int(x[2])
        dmrsconfig	=int(x[3])
        dmrsmaxlen= int(x[3])
        sulstatus	=int(x[5])
        ulsul	=int(x[6])
        fhf	=int(x[7])
        has	=int(x[8])
        dla	=int(x[9])
        srs	=int(x[10])
        pin	=int(x[11])
        csi	=int(x[12])
        cgb	=int(x[13])
        ulptrsstats	=int(x[14])
        puschtpstats	=int(x[15])
        boi	=int(x[16])
        vrb	=int(x[17])
        prb	=int(x[18])
        rmi	=int(x[19])
        zp	=int(x[20])
        dai	=int(x[21])
        pdsch	=int(x[22])
        tci	=int(x[23])
        cgbt	=int(x[24])
        cgbf	=int(x[25])
        f.close()
    

    test_string=str(input("\nEnter UL-DCI HexValue-->: "))
    scale = 16


    num_of_bits = 326
    
    diff=0
    a=list(bin(int(test_string, scale))[2:].zfill(num_of_bits))
    a.reverse()
    p1=int(a[diff])
    bw=int(input("\nEnter NRB value--> "))
    fdr=int(math.floor(math.log2(bw*(bw+1)/2)))
    print(fdr)
    if p1==0:
        format00(test_string,bw)
        format01(test_string,fdr,ccs,ulsul,bwp,bw,tdr,fhf,has,dla,srs,pin,dmrsconfig,dmrsmaxlen,sulstatus,csi,cgb,ulptrsstats,puschtpstats,boi)
    if p1==1:
        format10(test_string,bw)
        format11(test_string,bw,ccs,fdr,bwp,tdr,vrb,prb,rmi,zp,dai,pdsch,dmrsconfig,dmrsmaxlen,tci,sulstatus,cgbt,cgbf)

while True:
    lst = [(1,'Enter New Test Data'),
           (2,'Edit RRC Parameters'),
           (3,'Read User Defined RRC Parameters'),
           (4,'Read Default RRC Parameters'),
           (5,'Exit')
                   ]
    col_names = ["Index", "Operations"]
    print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
    act=int(input("Enter Your Option--> "))
    if act==1:
        runner()
    if act==2:
        writter()
        
    if act==3:
        f = open('config.txt', 'r')
        x = f.readlines()
        f.close()
        lst = [(1,'Cross-Carrier scheduling configuration',x[0]),
               (2,'Number of UL BWPs configured by RRC',x[1]),
               (3,'Number of elements in PUSCH allocationList in RRC',x[2]),
               (4,'DMRS-config-type',x[3]),
               (5,'supplementaryUplink status',x[4]),
               (6,'SupplementaryUplink Configuration',x[5]),
               (7,'Frequency Hoping flag status',x[6]),
               (8,'HARQ-ACK codebook status: semi-static=0, dynamic=1',x[7]),
               (9,'Number of HARQ-ACK sub-codebook status',x[8]),
               (10,'Bit length of SRS resource indicator',x[9]),
               (11,'TPMI bit length',x[10]),
               (12,'CSI request bit length',x[11]),
               (13,'CBG transmission information bit length',x[12]),
               (14,'UL-PTRS-present status: ON/OFF',x[13]),
               (15,'PUSCH-tp ststus: Enabled/Dissabled',x[14]),
               (16,'RRC parameter betaOffset status: semiStatic=0, dynamic=1',x[15]),
               (17,'Resource allocation Type: Type0/Type1',x[16]),
               (18,'Prb-BundlingType configuration: Static=0, Dynamic=1',x[17]),
               (19,'Rate matching indicator: 0, 1, or 2 bits',x[18]),
               (20,'Number of aperiodic ZP CSI-RS resource',x[19]),
               (21,'HARQ codebook type: None=0 Static=1, Dynamic=2',x[20]),
               (22,'Number of entries in RRC parameter dl-DataToUL-ACK',x[21]),
               (23,'tci-PresentInDCI status',x[22]),
               (24,'CBG transmission information bit length',x[23]),
               (25,'CBG flush information bit length',x[24])]
        col_names = ["Index", "Parameter", "Value"]
        print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
    if act==4:
        f = open('config_default.txt', 'r')
        x = f.readlines()
        f.close()
        lst = [(1,'Cross-Carrier scheduling configuration',x[0]),
               (2,'Number of UL BWPs configured by RRC',x[1]),
               (3,'Number of elements in PUSCH allocationList in RRC',x[2]),
               (4,'DMRS-config-type',x[3]),
               (5,'supplementaryUplink status',x[4]),
               (6,'SupplementaryUplink Configuration',x[5]),
               (7,'Frequency Hoping flag status',x[6]),
               (8,'HARQ-ACK codebook status: semi-static=0, dynamic=1',x[7]),
               (9,'Number of HARQ-ACK sub-codebook status',x[8]),
               (10,'Bit length of SRS resource indicator',x[9]),
               (11,'TPMI bit length',x[10]),
               (12,'CSI request bit length',x[11]),
               (13,'CBG transmission information bit length',x[12]),
               (14,'UL-PTRS-present status: ON/OFF',x[13]),
               (15,'PUSCH-tp ststus: Enabled/Dissabled',x[14]),
               (16,'RRC parameter betaOffset status: semiStatic=0, dynamic=1',x[15]),
               (17,'Resource allocation Type: Type0/Type1',x[16]),
               (18,'Prb-BundlingType configuration: Static=0, Dynamic=1',x[17]),
               (19,'Rate matching indicator: 0, 1, or 2 bits',x[18]),
               (20,'Number of aperiodic ZP CSI-RS resource',x[19]),
               (21,'HARQ codebook type: None=0 Static=1, Dynamic=2',x[20]),
               (22,'Number of entries in RRC parameter dl-DataToUL-ACK',x[21]),
               (23,'tci-PresentInDCI status',x[22]),
               (24,'CBG transmission information bit length',x[23]),
               (25,'CBG flush information bit length',x[24])]
         
        col_names = ["Index", "Parameter", "Value"]
        print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))

