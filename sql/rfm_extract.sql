 WITH rfm_base AS (
        SELECT 
            "Customer ID",
            MAX(CAST("InvoiceDate" AS TIMESTAMP)) as last_purchase_date,
            COUNT(DISTINCT "Invoice") as frequency,
            SUM(CAST("Quantity" AS NUMERIC) * CAST("Price" AS NUMERIC)) as monetary
        FROM online_retail_ii
        WHERE "Customer ID" IS NOT NULL 
          AND "Customer ID" != ''
          AND "Invoice" NOT LIKE 'C%%'
          AND CAST("Quantity" AS NUMERIC) > 0
        GROUP BY "Customer ID"
    )
    SELECT 
        "Customer ID",
        EXTRACT(DAY FROM (
            (SELECT MAX(CAST("InvoiceDate" AS TIMESTAMP)) FROM online_retail_ii) - last_purchase_date
        )) AS recency,
        frequency,
        monetary
    FROM rfm_base;
