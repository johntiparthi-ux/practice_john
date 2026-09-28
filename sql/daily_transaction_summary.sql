-- Daily transaction summary
SELECT
    DATE(transaction_timestamp) AS transaction_date,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM `project.dataset.transactions`
GROUP BY transaction_date
ORDER BY transaction_date;
