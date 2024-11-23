##ccs	=1
##bwp	=1
##tdr	=1
##dmrsconfig	=1
##dmrsmaxlen	=1
##sulstatus	=1
##ulsul	=1
##fhf	=1
##has	=1
##dla	=1
##srs	=1
##pin	=1
##csi	=1
##cgb	=1
##ulptrsstats	=1
##puschtpstats	=1
##boi	=1
##vrb	=1
##prb	=1
##rmi	=1
##zp	=1
##dai	=1
##pdsch	=1
##tci	=1
##cgbt	=1
##cgbf	=1
from tabulate import tabulate
def ack():
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
def writter():
    lst = [(1,'Edit User Defined RRC Parameters'),
           (2,'Edit Default RRC Parameters')
                   ]
    col_names = ["Index", "Operations"]
    print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
    act=int(input("Enter Your Option--> "))    
    ccs=int(input("\nEnter Cross-Carrier scheduling configuration--> 0/1: "))
    bwp=int(input("\nEnter the number of UL BWPs configured by RRC--> 0/1/2: "))
    tdr=int(input("\nEnter Number of elements in PUSCH allocationList in RRC--> 0-15: "))
    dmrsconfig=int(input("\nEnter DMRS-config-type--> 1-2: "))
    dmrsmaxlen=int(input("\nEnter DMRS-config-max-len--> 1-2: "))
    sulstatus=int(input("\nEnter supplementaryUplink status--> 0/1: "))

    ulsul=int(input("\nEnter SupplementaryUplink Configuration--> 0/1: "))
    fhf=int(input("\nEnter Frequency Hoping flag status--> 0/1: "))
    has=int(input("\nEnter HARQ-ACK codebook status: semi-static=0, dynamic=1--> 0/1: "))
    dla=int(input("\nEnter number of HARQ-ACK sub-codebook status--> 0/2: "))
    srs=int(input("\nEnter bit length of SRS resource indicator-->: "))
    pin=int(input("\nEnter TPMI bit length--> 0-6: "))
    csi=int(input("\nEnter CSI request bit length--> 0-6: "))
    cgb=int(input("\nEnter CBG transmission information bit length--> 0/2/4/6/8: "))
    ulptrsstats=int(input("\nEnter UL-PTRS-present status: ON/OFF--> 0/1: "))
    puschtpstats=int(input("\nEnter PUSCH-tp ststus: Enabled/Dissabled--> 0/1: "))
    boi=int(input("\nEnter RRC parameter betaOffset status: semiStatic=0, dynamic=1--> 0/1: "))
    vrb=int(input("\nEnter resource allocation Type: Type0/Type1--> 0/1: "))
    prb=int(input("\nEnter prb-BundlingType configuration: Static=0, Dynamic=1--> 0/1: "))
    rmi=int(input("\nEnter Rate matching indicator: 0, 1, or 2 bits according to higher layer parameters-->: "))
    zp=int(input("\nEnter the number of aperiodic ZP CSI-RS resource set by the RRC-->: "))
    dai=int(input("\nEnter HARQ codebook type: None=0 Static=1, Dynamic=2--> 0/1/2: "))
    pdsch=int(input("\nEnter Number of entries in RRC parameter dl-DataToUL-ACK configured under PUCCH-Config-->: "))
    tci=int(input("\nEnter tci-PresentInDCI status--> 0/1: "))
    cgbt=int(input("\nEnter CBG transmission information bit length--> 0/2/4/6/8: "))
    cgbf=int(input("\nEnter CBG flush information bit length--> 0/1: "))

    l = [ccs,bwp,tdr,dmrsconfig,dmrsmaxlen,sulstatus,ulsul,fhf,has,dla,srs,pin,csi,cgb,ulptrsstats,puschtpstats,boi,vrb,prb,rmi,zp,dai,pdsch,tci,cgbt,cgbf]
     
    # open file
    if act==1:
        with open('config.txt', 'w+') as f:
             
            # write elements of list
            for items in l:
                f.write('%s\n' %items)
             
            print("File written successfully")
    if act==2:
        with open('config_default.txt', 'w+') as f:
             
            # write elements of list
            for items in l:
                f.write('%s\n' %items)
             
            print("File written successfully")
     
     
    # close the file
    f.close()
    ack()
