from tabulate import tabulate
import math
se = [0.2344,0.3066,0.377,0.4902,0.6016,0.7402,0.877,1.0273,1.1758,1.3262,1.3281,1.4766,1.6953,1.9141,2.1602,2.4063,2.5703,2.7305,3.0293,3.3223,3.6094,3.9023,4.2129,4.5234,4.8164,5.1152,5.332,5.5547,'reserved','reserved','reserved','reserved']
tcr=['240/q','314/q',193,251,308,379,449,526,602,679,340,378,434,490,553,616,658,466,517,567,616,666,719,772,822,873,910,948,'reserved','reserved','reserved','reserved']
mo=['q','q',2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,1,2,4,6]

def format00(test_string, fdr):
    print('Format00')
    #test_string = '0x2584A800'
    #test_string=str(input("\nEnter UL-DCI HexValue-->: "))
    scale = 16
    num_of_bits = 32
    diff=0
    a=list(bin(int(test_string, scale))[2:].zfill(num_of_bits))
    fdr=int(math.ceil(math.log2(fdr*(fdr+1)/2)))
    a.reverse()
    if a[0]=='0':
        
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

        p1=int(a[diff])#Identifier for DCI formats
        b1.append(a[diff])
        diff=diff+1
     ######################################### 
        for i in range(diff,diff+fdr):
            b2.append(a[i])
        p2=int("".join(str(x) for x in b2), 2)
        diff=diff+fdr
     ##########################################
        for i in range(diff,diff+4):
             b3.append(a[i])
        p3=int("".join(str(x) for x in b3), 2)
        diff=diff+4
     ##########################################
        p4=int(a[diff])
        b4.append(a[diff])
        if p4==1:
            p4msg="Enabled"
        if p4==0:
            p4msg="Dissabled"
        diff=diff+1
     ##########################################       
        for i in range(diff,diff+5):
             b5.append(a[i])
        p5=int("".join(str(x) for x in b5), 2)
        p5msg='Modulation Order--> '+str(mo[diff])+'\nTarget code Rate--> '+str(tcr[diff])+'\nSpectral efficiency--> '+str(se[diff])
        diff=diff+5
     ##########################################
        p6=int(a[diff])
        b6.append(a[diff])
        if p6==1:
            p6msg="True"
        if p6==0:
            p6msg="False"
        diff=diff+1
     ##########################################
        for i in range(diff,diff+2):
             b7.append(a[i])
        p7=int("".join(str(x) for x in b7), 2)
        diff=diff+2
     ##########################################
        for i in range(diff,diff+4):
             b8.append(a[i])
        p8=int("".join(str(x) for x in b8), 2)
        diff=diff+4
     ##########################################
        for i in range(diff,diff+2):
             b9.append(a[i])
        p9=int("".join(str(x) for x in b9), 2)
        if p9 ==0:
             p9msg='Accumulated[dB]= -1 & Absolute[dB]= -4 '
        if p9 ==1:
             p9msg='Accumulated[dB]= 0 & Absolute[dB]= -1 '
        if p9 ==2:
             p9msg='Accumulated[dB]= 1 & Absolute[dB]= 1 '
        if p9 ==3:
             p9msg='Accumulated[dB]= 3 & Absolute[dB]= 4 '
        diff=diff+2
        
     ##########################################
        p10=int(a[diff])
        b10.append(a[diff])
        if p10==1:
            p10msg="Supplementary UL"
        if p10==0:
            p10msg="Normal UL"
        diff=diff+1
     ##########################################
                   
        lst = [(1,'Identifier for DCI formats',len(b1),''.join(str(p1)),str(p1),'The value of this bit field is always \nset to 0, indicating an UL DCI format.'),
               (2,'Frequency domain resource assignment ',len(b2),''.join(str(b2)),str(p2),''),
               (3,'Time domain resource assignment ',len(b3),''.join(str(b3)),str(p3),'Carries the row index of the items\nin pusch_allocationList in RRC'),
               (4,'Frequency Hopping Flag ',len(b4),''.join(str(b4)),str(p4),p4msg),
               (5,'Modulation and coding scheme ',len(b5),''.join(str(b5)),str(p5),p5msg),
               (6,'New data indicator ',len(b6),''.join(str(b6)),str(p6),p6msg),
               (7,'Redundancy version ','2',''.join(str(b7)),str(p7),'0,1,2,3'),
               (8,'HARQ process number ',len(b8),''.join(str(b8)),str(p8),'This value points to 1 of 16 HARQ processes'),
               (9,'TPC command for scheduled PUSCH ',len(b9),''.join(str(b9)),str(p9),p9msg),
               (10,'UL/SUL indicator ',len(b10),''.join(str(b10)),str(p10),p10msg)
               ]
        col_names = ["Index", "DCI Fields","No of bits","Bits","Decimal Value","Refrence" ]
        print(tabulate(lst, headers=col_names, tablefmt="fancy_grid"))
