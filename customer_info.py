import pandas as pd

customer_id = 1

with open('.data/customer/'+customer_id+'.csv', 'a') as f:
    c = pd.read_csv('./data/QUIC_Dim_Customer_clean.csv', sep='\t')
    c_info = c[c.CUSTOMER_ID == customer_id]
    c_info.to_csv(f, sep='\t', index=False)
    del c, c_info

    days = pd.read_csv('./data/QUIC_Dim_Day.csv', sep='\t')

    ctp = pd.read_csv('./data/QUIC_Fact_CTP_clean.csv', sep='\t').merge(days, on='DAY_ID')
    ctp_info = ctp[ctp.CUSTOMER_ID == customer_id]
    ctp_info.to_csv(f, sep='\t', index=False)
    del ctp, ctp_info

    ctr = pd.read_csv('./data/QUIC_Fact_CTR_clean.csv', sep='\t').merge(days, on='DAY_ID')
    ctr_info = ctr[ctr.CUSTOMER_ID == customer_id]
    ctr_info.to_csv(f, sep='\t', index=False)
    del ctr, ctr_info

    omc = pd.read_csv('./data/QUIC_Fact_OMC_clean.csv', sep='\t').merge(days, on='DAY_ID')
    omc_info = omc[omc.CUSTOMER_ID == customer_id]
    omc_info.to_csv(f, sep='\t', index=False)
    del omc, omc_info