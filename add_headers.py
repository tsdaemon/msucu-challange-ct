f = open("./data/QUIC_Fact_CTR.csv", "r")
contents = f.readlines()
f.close()

contents.insert(0, 'CUSTOMER_ID\tDAY_ID\tTRANSACTION_TM\tSTORE_CITY\tSTORE_PROV\tSTORE_ONSITE_PETRO\tDIVISION_CD\tDIVISION_NM\tAUTO_INVOICE\tREG_PROMO\tNET_POS_D\tTXN_COUNT]')

f = open("./data/QUIC_Fact_CTR.csv", "w")
contents = "".join(contents)
f.write(contents)
f.close()