from tabulate import tabulate
import math
se = [0.2344,0.3066,0.377,0.4902,0.6016,0.7402,0.877,1.0273,1.1758,1.3262,1.3281,1.4766,1.6953,1.9141,2.1602,2.4063,2.5703,2.7305,3.0293,3.3223,3.6094,3.9023,4.2129,4.5234,4.8164,5.1152,5.332,5.5547,'reserved','reserved','reserved','reserved']
tcr=['240/q','314/q',193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,910,948,'reserved','reserved','reserved','reserved']
mo=['q','q',2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,1,2,4,6]
def format11(test_string,bw,ccs,fdr,bwp,tdr,vrb,prb,rmi,zp,dai,pdsch,dmrsconfig,dmrsmaxlen,tci,sulstatus,cgbt,cgbf):
    print('Format11')
    #test_string = '0x2584A800'
    #test_string=str(input("\nEnter UL-DCI HexValue-->: "))
    scale = 16
    num_of_bits = 32
    diff=0
    fdr=int(math.ceil(math.log2(fdr*(fdr+1)/2)))
    #print(str(bin(int(test_string, scale))[2:].zfill(num_of_bits)))
    a=list(bin(int(test_string, scale))[2:].zfill(num_of_bits))
    a.reverse()
    if a[0]=='1':
##        ccs=int(input("\nEnter Cross-Carrier scheduling configuration--> 0/1: "))
##        bwp=int(input("\nEnter the number of UL BWPs configured by RRC--> 0/1/2: "))
##        fdr=math.floor(math.log2(bw(bw+1)/2))
##        tdr=int(input("\nEnter Number of elements in PUSCH allocationList in RRC--> 0-15: "))
##        vrb=int(input("\nEnter resource allocation Type: Type0/Type1--> 0/1: "))
##        prb=int(input("\nEnter prb-BundlingType configuration: Static=0, Dynamic=1--> 0/1: "))
##        rmi=int(input("\nEnter Rate matching indicator: 0, 1, or 2 bits according to higher layer parameters-->: "))
##        zp=int(input("\nEnter the number of aperiodic ZP CSI-RS resource set by the RRC-->: "))
##        dai=int(input("\nEnter HARQ codebook type: None=0 Static=1, Dynamic=2--> 0/1/2: "))
##        pdsch=int(input("\nEnter No. of entries in RRC parameter dl-DataToUL-ACK configured under PUCCH-Config-->: "))
##        dmrsconfig=int(input("\nEnter DMRS-config-type--> 1-2: "))
##        dmrsmaxlen=int(input("\nEnter DMRS-config-max-len--> 1-2: "))
##        tci=int(input("\nEnter tci-PresentInDCI status--> 0/1: "))
##        sulstatus=int(input("\nEnter supplementaryUplink status--> 0/1: "))
##        cgbt=int(input("\nEnter CBG transmission information bit length--> 0/2/4/6/8: "))
##        cgbf=int(input("\nEnter CBG flush information bit length--> 0/1: "))

        if tdr!=0:
            tdr= math.ceil(math.log2(tdr))
        if zp!=0:
            zp= math.ceil(math.log2(zp+1))
        if pdsch!=0:
            pdsch= math.ceil(math.log2(pdsch))

        
        print("\nBinary value-->",' '.join(a))
        for i in range (40):
            a.append(0)
        
        b1=[]
        b2=[]
        b3=[]
        b4=[]
        b5=[]
        b6=[]
        b7=[]
        b8=[]
        b9=[]
        b10=[]
        b11=[]
        b12=[]
        b13=[]
        b14=[]
        b15=[]
        b16=[]
        b17=[]
        b18=[]
        b19=[]
        b20=[]
        b21=[]
        b22=[]
        b23=[]
        b24=[]
        b25=[]
        b26=[]
        p1=0
        p2=0
        p3=0
        p4=0
        p5=0
        p6=0
        p7=0
        p8=0
        p9=0
        p10=0
        p11=0
        p12=0
        p13=0
        p14=0
        p15=0
        p16=0
        p17=0
        p18=0
        p19=0
        p20=0
        p21=0
        p22=0
        p23=0
        p24=0
        p25=0
        p26=0

        p1msg='Always set to 1, indicating a DL DCI format'
        p2msg='3-bits if Cross-carrier scheduling is configured,\n0-bits otherwise'
        p3msg='N/A'
        p4msg='Variable with Resource Allocation Type'
        p5msg='Carries the row index of the items in pdsch_allocationList in RRC'
        p6msg='0 bit if only resource allocation type 0 is configured or \nif interleaved VRB-to-PRB mapping is not configured by high layers;\n1 bit according to Table 7.3.1.1.2-33 otherwise,\nonly applicable to resource allocation type 1"'
        p7msg='0 bit if the higher layer parameter prb-BundlingType is not \nconfigured or is set to static 1 bit if the higher layer \nparameter prb-BundlingType is set to dynamic'
        p8msg='Bit size is determined by higher layer parameters \nrateMatchPatternGroup1 and rateMatchPatternGroup2.'
        p9msg='[log2(Nzp+1)] bits, where Nzp is the number of\naperiodic ZP CSI-RS resource set by the RRC'
        p10msg='This value points to the row number within the MCS table'
        p11msg='N/A'
        p12msg='rVid values 0,1,2 and 3'
        p13msg='This value points to the row number within the MCS table'
        p14msg='N/A'
        p15msg='rVid values 0,1,2 and 3'
        p16msg='For downlink, 16 HARQ processes per cell is supported by the UE'
        p17msg='4 bits if more than one serving cell are configured in the DL and \nthe higher layer parameter pdsch-HARQACK-Codebook=dynamic,\nwhere the 2 MSB bits are the counter DAI and the 2 LSB bits are the \ntotal DAI; 2 bits if only one serving cell is configured in the DL and \nthe higher layer parameter pdsch-HARQ-ACKCodebook= dynamic,\nwhere the 2 bits are the counter DAI; 0 bits otherwise.'
        p18msg='N/A'
        p19msg='Used to select PUCCH resource from ResourceList within PUCCH-ResourceSet'
        p20msg='Row number(index) of K1\nNumber of bit is determined by log2(I).\nI is the number of elements in the IE\nPUCCH-Config.dl-DataToUL-ACK'
        p21msg='Indicates antenna ports on which \ndata is transmitted.'
        p22msg='0 bit if higher layer parameter tci-PresentInDCI \nis not enabled; 3 bits otherwise'
        p23msg='2 bits as defined by Table for UEs not configured \nwith SUL in the cell;\n3 bits for UEs configured SUL in the cell where \nthe first bit is the non-SUL/SUL indicator'
        p24msg='Determined by the higher layer parameters \nmaxCodeBlockGroupsPerTransportBlock \nand Number-MCS-HARQDL-DCI for the PDSCH'
        p25msg='No. of bits depends upon the RRC parameter \ncodeBlockGroupFlushIndicator'
        p26msg='N/A'
       

        p1=int(a[diff])#Identifier for DCI formats
        b1.append(a[diff])
        diff=diff+1
        

        if ccs==1:
            for i in range(diff,diff+3):
                b2.append(a[i])
            p2=int("".join(str(x) for x in b2), 2)  #Carrier indicator
            diff=diff+3
      

        if bwp==1:
                p3=int(a[diff])
                if p3==0:
                    p3msg="First bandwidth part configured by higher layers"
                if p3==1:
                    p3msg="Second bandwidth part configured by higher layers"
                b3.append(a[diff])
                diff=diff+1
        if bwp==2:
                for i in range(diff,diff+2):
                    b3.append(a[i])
                diff=diff+2
                p3=str("".join(str(x) for x in b3))
                if p3=='00':
                    p3msg="First bandwidth part configured by higher layers"
                if p3=='01':
                    p3msg="Second bandwidth part configured by higher layers"
                if p3=='10':
                    p4msg="Third bandwidth part configured by higher layers"
                if p3=='11':
                    p3msg="Fourth bandwidth part configured by higher layers"

        if fdr!=0:
                for i in range(diff,diff+fdr):
                    b4.append(a[i])
                p4=int("".join(str(x) for x in b4), 2)
                diff=diff+fdr

        if tdr!=0:
                for i in range(diff,diff+tdr):
                     b5.append(a[i])
                p5=int("".join(str(x) for x in b5), 2)
                diff=diff+tdr              

        if vrb!=0:
                for i in range(diff,diff+1):
                     b6.append(a[i])
                p6=int("".join(str(x) for x in b6), 2)
                diff=diff+1

        if prb!=0:
                for i in range(diff,diff+1):
                     b7.append(a[i])
                p7=int("".join(str(x) for x in b7), 2)
                diff=diff+1

        if rmi!=0:
                for i in range(diff,diff+rmi):
                     b8.append(a[i])
                p8=int("".join(str(x) for x in b8), 2)
                diff=diff+rmi
        if zp!=0:
                for i in range(diff,diff+zp):
                     b9.append(a[i])
                p9=int("".join(str(x) for x in b9), 2)
                diff=diff+zp

        

        for i in range(diff,diff+5):
                b10.append(a[i])
        p10=int("".join(str(x) for x in b10), 2)
        diff=diff+5

        p11=int(a[diff])
        diff=diff+1

        for i in range(diff,diff+2):
                b12.append(a[i])
        p12=int("".join(str(x) for x in b12), 2)
        diff=diff+2

        for i in range(diff,diff+5):
                b13.append(a[i])
        p13=int("".join(str(x) for x in b13), 2)
        diff=diff+5

        p14=int(a[diff])
        diff=diff+1

        for i in range(diff,diff+2):
                b15.append(a[i])
        p15=int("".join(str(x) for x in b15), 2)
        diff=diff+2

        for i in range(diff,diff+4):
            b16.append(a[i])
        p16=int("".join(str(x) for x in b16), 2)
        diff=diff+4

        if dai==1:
                for i in range(diff,diff+2):
                     b17.append(a[i])
                p17=int("".join(str(x) for x in b17), 2)
                diff=diff+2
        if dai==2:
                for i in range(diff,diff+4):
                     b17.append(a[i])
                p17=int("".join(str(x) for x in b17), 2)
                diff=diff+4

        for i in range(diff,diff+2):
                b18.append(a[i])
        p18=int("".join(str(x) for x in b18), 2)
        diff=diff+2

        for i in range(diff,diff+3):
                b19.append(a[i])
        p19=int("".join(str(x) for x in b19), 2)
        diff=diff+3

        if pdsch!=0:
            for i in range(diff,diff+pdsch):
                b20.append(a[i])
            p20=int("".join(str(x) for x in b20), 2)
            diff=diff+pdsch

        if dmrsconfig==1 and dmrsmaxlen==1:
            bl=4
        if dmrsconfig==1 and dmrsmaxlen==2:
            bl=5
        if dmrsconfig==2 and dmrsmaxlen==1:
            bl=5
        if dmrsconfig==2 and dmrsmaxlen==2:
            bl=6
        for i in range(diff,diff+bl):
            b21.append(a[i])
        p21=int("".join(str(x) for x in b21), 2)
        diff=diff+bl

        if tci!=0:
            for i in range(diff,diff+3):
                b22.append(a[i])
            p22=int("".join(str(x) for x in b22), 2)
            diff=diff+3

        if sulstatus==0:
            for i in range(diff,diff+2):
                b23.append(a[i])
            p23=str("".join(str(x) for x in b23))
            diff=diff+2
            if p23=='00':
                p23msg="No aperiodic SRS resource set triggered"
            if p23=='01':
                p23msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p23=='10':
                p23msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p23=='11':
                p23msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"
        if sulstatus==1:
            for i in range(diff,diff+3):
                b23.append(a[i])
            p23=str("".join(str(x) for x in b23))
            diff=diff+3
            if p23=='000':
                p23msg="non-SUL: No aperiodic SRS resource set triggered"
            if p23=='001':
                p23msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p23=='010':
                p23msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p23=='011':
                p23msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"
            if p23=='100':
                p23msg="SUL: No aperiodic SRS resource set triggered"
            if p23=='101':
                p23msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p23=='110':
                p23msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p23=='111':
                p23msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"        
        if cgbt!=0:
            for i in range(diff,diff+cgbt):
                b24.append(a[i])
            p24=str("".join(str(x) for x in b24))
            diff=diff+cgbt
        if cgbf!=0:
            b25.append(a[diff])
            p25=int(a[diff])
            diff=diff+1

        b26.append(a[diff])
        p26=int(a[diff])
        diff=diff+1
        
        lst = [(1,'Identifier for DCI formats',len(b1),''.join(str(b1)),str(p1),str(p1msg)),
               (2,'Carrier indicator ',len(b2),''.join(str(b2)),str(p2),str(p2msg)),
               (3,'Bandwidth part indicator ',len(b3),''.join(str(b3)),str(p3),str(p3msg)),
               (4,'Frequency domain resource assignment ',len(b4),''.join(str(b4)),str(p4),str(p4msg)),
               (5,'Time domain resource assignment ',len(b5),''.join(str(b5)),str(p5),str(p5msg)),
               (6,'VRB-to-PRB mapping ',len(b6),''.join(str(b6)),str(p6),str(p6msg)),
               (7,'PRB bundling size indicator ',len(b7),''.join(str(b7)),str(p7),str(p7msg)),
               (8,'Rate matching indicator ',len(b8),''.join(str(b8)),str(p8),str(p8msg)),
               (9,'ZP CSI-RS Trigger ',len(b9),''.join(str(b9)),str(p9),str(p9msg)),   
               (10,'TB1: Modulation and coding scheme',len(b10),''.join(str(b10)),str(p10),str(p10msg)),
               (11,'TB1: New data indicator',len(b11),''.join(str(b11)),str(p11),p11msg),
               (12,'TB1: Redundancy versions',len(b12),''.join(str(b12)),str(p12),str(p12msg)), 
               (13,'TB2: Modulation and coding scheme',len(b13),''.join(str(b13)),str(p13),str(p13msg)),
               (14,'TB2: New data indicator',len(b14),''.join(str(b14)),str(p14),p14msg),
               (15,'TB2: Redundancy versions',len(b15),''.join(str(b15)),str(p15),str(p15msg)),
               (16,'HARQ process number',len(b16),''.join(str(b16)),str(p16),str(p16msg)),
               (17,'Downlink assignment index',len(b17),''.join(str(b17)),str(p17),str(p17msg)),
               (18,'TPC command for scheduled PUSCH',len(b18),''.join(str(b18)),str(p18),p18msg),
               (19,'PUCCH resource indicator',len(b19),''.join(str(b19)),str(p19),str(p9msg)),
               (20,'PDSCH-to-HARQ_feedback timing indicator',len(b20),''.join(str(b20)),str(p20),str(p20msg)),
               (21,'Antenna ports',len(b21),''.join(str(b21)),str(p21),str(p20msg)),
               (22,'Transmission configuration indication',len(b22),''.join(str(b22)),str(p22),str(p22msg)),
               (23,'SRS request',len(b23),''.join(str(b23)),str(p23),p23msg),
               (24,'CBG transmission information(CBGTI)',len(b24),''.join(str(b24)),str(p24),str(p24msg)),
               (25,'CBG flushing out information(CBGFI)',len(b25),''.join(str(b25)),str(p25),str(p25msg)),
               (26,'DMRS Sequence Initialization',len(b26),''.join(str(b26)),str(p26),str(p26msg))
               ]

        
        col_names = ["Index", "DCI Fields","No of bits","Bits","Decimal Value","Refrence" ]
        print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
