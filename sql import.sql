BULK INSERT dbo.CTC_FACT_OMC
FROM 'D:\DRIVE\MS CS UCU\Intro to DS\competition\CT\QUIC_FACT_OMC.csv'
WITH
(
    FIRSTROW = 1,
    FIELDTERMINATOR = '0x09',  --CSV field delimiter
    ROWTERMINATOR = '0x0a'
)