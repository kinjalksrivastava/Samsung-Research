from tabulate import tabulate
import math
se = [0.2344,0.3066,0.377,0.4902,0.6016,0.7402,0.877,1.0273,1.1758,1.3262,1.3281,1.4766,1.6953,1.9141,2.1602,2.4063,2.5703,2.7305,3.0293,3.3223,3.6094,3.9023,4.2129,4.5234,4.8164,5.1152,5.332,5.5547,'reserved','reserved','reserved','reserved']
tcr=['240/q','314/q',193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,910,948,'reserved','reserved','reserved','reserved']
mo=['q','q',2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,1,2,4,6]
def format01(test_string,fdr,ccs,ulsul,bwp,bw,tdr,fhf,has,dla,srs,pin,dmrsconfig,dmrsmaxlen,sulstatus,csi,cgb,ulptrsstats,puschtpstats,boi):
    print('Format01')
    #test_string = '0x2584A800'
    #test_string=str(input("\nEnter UL-DCI HexValue-->: "))
    fdr=int(math.floor(math.log2(fdr*(fdr+1)/2)))
    scale = 16
    num_of_bits = 32
    diff=0
    a=list(bin(int(test_string, scale))[2:].zfill(num_of_bits))
    a.reverse()
    if a[0]=='0':
        print('Format01')

##        ccs=int(input("\nEnter Cross-Carrier scheduling configuration--> 0/1: "))
##        ulsul=int(input("\nEnter SupplementaryUplink Configuration--> 0/1: "))
##        bwp=int(input("\nEnter the number of UL BWPs configured by RRC--> 0/1/2: "))
##        fdr=math.floor(math.log2(bw(bw+1)/2))
##        tdr=int(input("\nEnter Number of elements in PUSCH allocationList in RRC--> 0-15: "))
##        fhf=int(input("\nEnter Frequency Hoping flag status--> 0/1: "))
##        has=int(input("\nEnter HARQ-ACK codebook status: semi-static=0, dynamic=1--> 0/1: "))
##        dla=int(input("\nEnter number of HARQ-ACK sub-codebook status--> 0/2: "))
##        srs=int(input("\nEnter bit length of SRS resource indicator-->: "))
##        pin=int(input("\nEnter TPMI bit length--> 0-6: "))
##        dmrsconfig=int(input("\nEnter DMRS-config-type--> 1-2: "))
##        dmrsmaxlen=int(input("\nEnter DMRS-config-max-len--> 1-2: "))
##        sulstatus=int(input("\nEnter supplementaryUplink status--> 0/1: "))
##        csi=int(input("\nEnter CSI request bit length--> 0-6: "))
##        cgb=int(input("\nEnter CBG transmission information bit length--> 0/2/4/6/8: "))
##        ulptrsstats=int(input("\nEnter UL-PTRS-present status: ON/OFF--> 0/1: "))
##        puschtpstats=int(input("\nEnter PUSCH-tp ststus: Enabled/Dissabled--> 0/1: "))
##        boi=int(input("\nEnter RRC parameter betaOffset status: semiStatic=0, dynamic=1--> 0/1: "))
        if dmrsconfig==1:
            puschstats=int(input("\nEnter PUSCH-tp status: enabled=1, dissabled=0--> 0/1: "))
        tdr= math.ceil(math.log2(tdr))
       
        #print(str(bin(int(test_string, scale))[2:].zfill(num_of_bits)))
        a=list(bin(int(test_string, scale))[2:].zfill(num_of_bits))
        print("\nBinary value-->",' '.join(a))
        for i in range (20):
            a.append(0)
        a.reverse()

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
        p1=0
        p2=0
        new=""
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

        p1msg='N/A'
        p2msg='N/A'
        p3msg='N/A'
        p4msg='N/A'
        p5msg='N/A'
        p6msg='N/A'
        p7msg='N/A'
        p8msg='N/A'
        p9msg='N/A'
        p10msg='N/A'
        p11msg='N/A'
        p12msg='N/A'
        p13msg='N/A'
        p14msg='N/A'
        p15msg='N/A'
        p16msg='N/A'
        p17msg='N/A'
        p18msg='N/A'
        p19msg='N/A'
        p20msg='N/A'
        p21msg='N/A'
        p22msg='N/A'
        p23msg='N/A'
        p24msg='N/A'
       

        p1=int(a[diff])#Identifier for DCI formats
        b1.append(a[diff])
        diff=diff+1
        
        if ccs==1:
            for i in range(diff,diff+3):
                b2.append(a[i])
            p2=int("".join(str(x) for x in b2), 2)  #Carrier indicator
            diff=diff+3
        if ulsul==1:
            p3=int(a[diff])
            b3.append(a[diff])
            diff=diff+1
            if p3==1:
                p3msg="1 - bit for UEs configured with SUL in the cell"
            if p3==0:
                p3msg="0 - bit for UEs not configured with SUL in the cell"

        if bwp==1:
                p4=int(a[diff])
                if p4==0:
                    p4msg="First bandwidth part configured by higher layers"
                if p4==1:
                    p4msg="Second bandwidth part configured by higher layers"
                b4.append(a[diff])
                diff=diff+1

        if bwp==2:
                for i in range(diff,diff+2):
                    b4.append(a[i])
                diff=diff+2
                p4=str("".join(str(x) for x in b4))
                if p4=='00':
                    p4msg="First bandwidth part configured by higher layers"
                if p4=='01':
                    p4msg="Second bandwidth part configured by higher layers"
                if p4=='10':
                    p4msg="Third bandwidth part configured by higher layers"
                if p4=='11':
                    p4msg="Fourth bandwidth part configured by higher layers"
        
        if fdr!=0:
                for i in range(diff,diff+fdr):
                    b5.append(a[i])
                p5=int("".join(str(x) for x in b5), 2)
                diff=diff+fdr
        if tdr!=0:
                for i in range(diff,diff+tdr):
                     b6.append(a[i])
                p6=int("".join(str(x) for x in b6), 2)
                diff=diff+tdr
        if fhf==1:
                p7=int(a[diff])
                b7.append(a[diff])
                diff=diff+1
                if p7==1:
                    fhfmsg="Enabled"
                if p7==0:
                    fhfmsg="Dissabled"
        
        for i in range(diff,diff+5):
                     b8.append(a[i])
        p8=int("".join(str(x) for x in b8), 2)
        p8msg='Modulation Order--> '+str(mo[diff])+'\nTarget code Rate--> '+str(tcr[diff])+'\nSpectral efficiency--> '+str(se[diff])
        diff=diff+5

        p9=int(a[diff])
        diff=diff+1
        if p9==1:
            p9msg="Re-transmission is triggerd"
        if p9==0:
            p9msg="New transmission"
        
        for i in range(diff,diff+2):
            b10.append(a[i])
        p10=int("".join(str(x) for x in b10), 2)
        diff=diff+2

        for i in range(diff,diff+4):
            b11.append(a[i])
        p11=int("".join(str(x) for x in b11), 2)
        diff=diff+4

        if has==0:
            p12=int(a[diff])
            b12.append(a[diff])
            diff=diff+1
        if has==1:
            for i in range(diff,diff+2):
                b12.append(a[i])
            p12=int("".join(str(x) for x in b12), 2)
            diff=diff+2

        if dla==2:
            for i in range(diff,diff+2):
                b13.append(a[i])
            p13=int("".join(str(x) for x in b13), 2)
            diff=diff+2
        for i in range(diff,diff+2):
            b14.append(a[i])
        p14=str("".join(str(x) for x in b14))
        diff=diff+2
        if p14=='00':
            p14msg="Accumulated PUSCH,b,f,c[dB] (Accumulation enabled)=-1\nAbsolute PUSCH,b,f,c[dB] (Accumulation dissabled) =-4"
        if p14=='01':
            p14msg="Accumulated PUSCH,b,f,c[dB] (Accumulation enabled)=-0\nAbsolute PUSCH,b,f,c[dB] (Accumulation dissabled) =-1"    
        if p14=='10':
            p14msg="Accumulated PUSCH,b,f,c[dB] (Accumulation enabled)=1\nAbsolute PUSCH,b,f,c[dB] (Accumulation dissabled) =1"
        if p14=='11':
            p14msg="Accumulated PUSCH,b,f,c[dB] (Accumulation enabled)=3\nAbsolute PUSCH,b,f,c[dB] (Accumulation dissabled) =4"

        if srs!=0:
            for i in range(diff,diff+srs):
                b15.append(a[i])
            p15=int("".join(str(x) for x in b15), 2)
            diff=diff+srs
        if pin!=0:
            for i in range(diff,diff+pin):
                b16.append(a[i])
            p16=int("".join(str(x) for x in b16), 2)
            diff=diff+pin

        if dmrsconfig==1 and dmrsmaxlen==1 and puschtpstats==1:
            bl=2
        if dmrsconfig==1 and dmrsmaxlen==2 and puschtpstats==1:
            bl=4
        if dmrsconfig==1 and dmrsmaxlen==1 and puschtpstats==0:
            bl=3
        if dmrsconfig==1 and dmrsmaxlen==2 and puschtpstats==0:
            bl=4
        if dmrsconfig==2 and dmrsmaxlen==1 and puschtpstats==0:
            bl=4
        if dmrsconfig==2 and dmrsmaxlen==2 and puschtpstats==0:
            bl=5
        for i in range(diff,diff+bl):
            b17.append(a[i])
        p17=int("".join(str(x) for x in b17), 2)
        diff=diff+bl

        if sulstatus==0:
            for i in range(diff,diff+2):
                b18.append(a[i])
            p18=str("".join(str(x) for x in b18))
            diff=diff+2
            if p18=='00':
                p18msg="No aperiodic SRS resource set triggered"
            if p18=='01':
                p18msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p18=='10':
                p18msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p18=='11':
                p18msg="SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"
        if sulstatus==1:
            for i in range(diff,diff+3):
                b18.append(a[i])
            p18=str("".join(str(x) for x in b18))
            diff=diff+3
            if p18=='000':
                p18msg="non-SUL: No aperiodic SRS resource set triggered"
            if p18=='001':
                p18msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p18=='010':
                p18msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p18=='011':
                p18msg="non-SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"
            if p18=='100':
                p18msg="SUL: No aperiodic SRS resource set triggered"
            if p18=='101':
                p18msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 1"
            if p18=='110':
                p18msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 2"
            if p18=='111':
                p18msg="SUL: SRS resource set(s) configured with higher layer parameter \naperiodicSRS-ResourceTrigger set to 3"        

        if csi!=0:
            for i in range(diff,diff+csi):
                b19.append(a[i])
            p19=int("".join(str(x) for x in b19),2)
            diff=diff+csi
        if cgb!=0:
            for i in range(diff,diff+cgb):
                b20.append(a[i])
            p20=int("".join(str(x) for x in b20),2)
            diff=diff+cgb

        if ulptrsstats==0 and puschtpstats==1:
            for i in range(diff,diff+2):
                b21.append(a[i])
            p21=str("".join(str(x) for x in b21))
            diff=diff+2
            if p21=='00':
                p21msg="UL PTRS port=0 | UL-PTRS-ports=0"
            if p21=='01':
                p21msg="UL PTRS port=0 | UL-PTRS-ports=1"
            if p21=='10':
                p21msg="UL PTRS port=0 | UL-PTRS-ports=2"
            if p21=='11':
                p21msg="UL PTRS port=1 | UL-PTRS-ports=2"

        if boi==1:
            for i in range(diff,diff+2):
                b22.append(a[i])
            p22=int("".join(str(x) for x in b22),2)
            diff=diff+2    

        if puschtpstats==1:
            p23=a[diff]
            b23.append(a[diff])
            diff=diff+1

        p24=a[31]
        b24.append(a[31])
        new=str(mo[p8])+' '+str(tcr[p8])+' '+str(se[p8])
        
        lst = [(1,'Identifier for DCI formats',len(b1),''.join(str(b1)),str(p1),'DCI Format 0_1'),
               (2,'Carrier indicator ',len(b2),''.join(str(b2)),str(p2),'Variable with UL BWP N_RB.\nIndicate PRB location within the BWP.'),
               (3,'UL/SUL Indicator ',len(b3),''.join(str(b3)),str(p3),p3msg),
               (4,'Bandwidth part indicator ',len(b4),''.join(str(b4)),str(p4),p4msg),
               (5,'Frequency domain resource assignment ',len(b5),''.join(str(b5)),str(p5),'Variable with Resource Allocation Type'),
               (6,'Time domain resource assignment ',len(b6),''.join(str(b6)),str(p6),'Carries the row index of the items in \npusch_allocationList in RRCNumber of Bit Length is \ndetermined by log(I,2), where I is the number of \nelements in pusch_allocationList in RRC'),
               (7,'Frequency Hopping Flag',len(b7),''.join(str(b7)),str(p7),p7msg),
               (8,'Modulation and coding scheme',len(b8),''.join(str(b8)),str(p8),p8msg),
               (9,'New data indicator',len(b9),''.join(str(b9)),str(p9),p9msg),
               (10,'Redundancy versionx',len(b10),''.join(str(b10)),str(p10),'0,1,2,3'),
               (11,'HARQ process number',len(b11),''.join(str(b11)),str(p11),),
               (12,'1st Downlink assignment index',len(b12),''.join(str(b12)),str(p12),),
               (13,'2nd Downlink assignment index',len(b13),''.join(str(b13)),str(p13),),
               (14,'TPC command for scheduled PUSCH',len(b14),''.join(str(b14)),str(p14),p14msg),
               (15,'SRS resource indicator',len(b15),''.join(str(b15)),str(p15),'Determined by RRC Parameter SRS-SetUse'),
               (16,'Precoding information and number of layers\n(TPMI)',len(b16),''.join(str(b16)),p16,'Determined by RRC Parameter SRS-SetUse'),
               (17,'Antenna ports',len(b17),''.join(str(b17)),str(p17),'Determined by PUSCH-tp, DL-DMRS-config-type,\nDL-DMRS-config-max-len,Rank'),
               (18,'SRS request',len(b18),''.join(str(b18)),str(p18),p18msg),
               (19,'CSI request',len(b19),''.join(str(b19)),str(p19),'Determined by ReportTriggerSize in RRC message.\nSee Configure Aperiodic Trigger section for the details.'),
               (20,'CBG transmission information',len(b20),''.join(str(b20)),str(p20),'Determined by maxCodeBlockGroupPerTransportblock in RRC message'),
               (21,'PTRS - DMRS Association',len(b21),''.join(str(b21)),str(p21),p21msg),
               (22,'beta_offsetr Indicator',len(b22),''.join(str(b22)),str(p22),'0 - if uci-on-PUSCH.dynamic = Not Configured\n2 - otherwise, see Table 7.3.1.1.2-27'),
               (23,'DMRS Sequence Initialization',len(b23),''.join(str(b23)),str(p23),'0 - if PUSCH-tp=Disabled\n1 - if PUSCH-tp=Enabled'),
               (24,'UL-SCH Indicator',len(b24),''.join(str(b24)),str(p24),'0 - UL-SCH shall not be transmitted on the PUSCH\n1 - UL-SCH shall be transmitted on the PUSCH"')
               ]
        col_names = ["Index", "DCI Fields","No of bits","Bits","Decimal Value","Refrence" ]
        print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))

